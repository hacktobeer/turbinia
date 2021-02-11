# PYTHONPATH=. uvicorn --reload-dir turbinia/api-server/ --app-dir turbinia/api-server/ turbiniaapi:api --reload
# curl -X POST --data '{"source_path":"$PWD/evidence/history.tgz"}' http://localhost:8000/create/request/compresseddirectory
# curl http://localhost:8000/status/requests
# curl http://localhost:8000/status/request/[request_id]
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uuid
import os
from enum import Enum
import getpass

from turbinia import client as TurbiniaClientProvider
from turbinia.client import TurbiniaCeleryClient
from turbinia import config
from turbinia import evidence
from turbinia.processors import archive
from turbinia.message import TurbiniaRequest


class Command(str, Enum):
  alexnet = "compresseddirectory"
  resnet = "rawdisk"
  lenet = "googleclouddisk"


class Request(BaseModel):
  source_path: str
  request_id: Optional[str]


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
def statusrequest(request_id: uuid.UUID):
  # return client.format_task_status(
  #         instance=config.INSTANCE_ID, project=config.TURBINIA_PROJECT,
  #         region=region, days=7, task_id="",
  #         request_id=request_id, user="",
  #         all_fields=False, full_report=False,
  #         priority_filter=20, output_json=False)
  return client.format_task_status(
      instance=config.INSTANCE_ID, project=config.TURBINIA_PROJECT,
      region=region, days=1, task_id=None, request_id=request_id, user=None,
      all_fields=False, full_report=False, priority_filter=20, output_json=True)
  # return client.format_task_statistics(
  #           instance=config.INSTANCE_ID, project=config.TURBINIA_PROJECT,
  #           region=region, days=1, task_id=None,
  #           request_id=request_id, user=None, csv=False)


@api.post("/create/request/{evidence_type}")
def createrequest(evidence_type: Command, request: Request):
  request_id = uuid.uuid4().hex

  #archive.ValidateTarFile(source_path)
  source_path = os.path.abspath(request.source_path)
  evidence_ = evidence.CompressedDirectory(
      name=evidence_type, source_path=source_path, source=None)

  request = TurbiniaRequest(request_id=request_id, requester=getpass.getuser())
  request.evidence.append(evidence_)
  client.send_request(request)
  return request_id
