# PYTHONPATH=. uvicorn --reload-dir turbinia/api-server/ --app-dir turbinia/api-server/ turbiniaapi:api --reload
# curl -X POST --data '{"source_path":"$PWD/evidence/history.tgz"}' http://localhost:8000/create/request/compresseddirectory
# curl http://localhost:8000/status/requests
# curl http://localhost:8000/status/request/[request_id]
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import uuid
import os
from enum import Enum
import getpass

from turbinia import client as TurbiniaClientProvider
from turbinia import TurbiniaException
from turbinia.client import TurbiniaCeleryClient
from turbinia import config
from turbinia import evidence
from turbinia.processors import archive
from turbinia.message import TurbiniaRequest


class Generic(BaseModel):
  job_allowlist: Optional[List[str]]
  job_denylist: Optional[List[str]]
  source_path: str
  output_json: Optional[bool]


class GCP(BaseModel):
  disk_name: Optional[str]
  project_name: Optional[str]
  zone: Optional[str]


class RequestOptions(BaseModel):
  generic: Optional[Generic]
  GCP: Optional[GCP]


class Request(BaseModel):
  request_id: Optional[str]
  request_options: Optional[RequestOptions]


class Evidence(str, Enum):
  compresseddirectory = "compresseddirectory"
  rawdisk = "rawdisk"
  googleclouddisk = "googleclouddisk"
  config = "config"
  apfs = "apfs"
  bitlocker = "bitlocker"
  googleclouddiskembedded = "googleclouddiskembedded"
  rawmemory = "rawmemory"
  directory = "directory"
  gcplogs = "gcplogs"


client = TurbiniaClientProvider.get_turbinia_client(False)
config.LoadConfig()

region = config.TURBINIA_REGION

api = FastAPI()


@api.get("/")
async def root():
  return {"message": "Hello World"}


@api.get("/status/requests")
def statusrequests():
  return client.format_request_status(
      instance=config.INSTANCE_ID, project=config.TURBINIA_PROJECT,
      region=region, days=7, all_fields=True)


@api.get("/status/request/{request_id}")
def statusrequest(request_id: str):
  return client.format_task_status(
      instance=config.INSTANCE_ID, project=config.TURBINIA_PROJECT,
      region=region, request_id=request_id, full_report=True, output_json=True)


@api.post("/create/{evidence_type}")
def createrequest(evidence_type: Evidence, req: Request):
  request_id = uuid.uuid4().hex

  if evidence_type == Evidence.compresseddirectory:
    source_path = os.path.abspath(req.request_options.generic.source_path)
    evidence_ = evidence.CompressedDirectory(source_path=source_path)
  if evidence_type == Evidence.rawdisk:
    source_path = os.path.abspath(req.request_options.generic.source_path)
    evidence_ = evidence.RawDisk(
        name=evidence_type, source_path=source_path, source=None)
  if evidence_type == Evidence.googleclouddisk:
    evidence_ = evidence.GoogleCloudDisk(
        project=req.options.GCP.zone, zone=req.options.GCP.zone,
        disk_name=req.options.GCP.disk_name)

  try:
    evidence_.validate()
  except TurbiniaException as exception:
    print(exception)

  request = TurbiniaRequest(request_id=request_id, requester=getpass.getuser())
  request.evidence.append(evidence_)
  client.send_request(request)
  return request_id
