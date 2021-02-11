# Turbinia API server

## Introduction

This is the Turbinia API server based on FastAPI. A OpenAPI compatible REST API.

The Turbinia API server will connect with the Turbinia stack (GCP, local or hybrid)

## Running

Run the API server using uvicorn from the repository main folder.

```
$ PYTHONPATH=. uvicorn --reload-dir turbinia/api-server/ --app-dir turbinia/api-server/ turbiniaapi:api --reload
```

## API Documentation

The API server is OpenAPI compatible and exposes the API documentation using Swagger UI on

```
http://localhost:8000/docs
```

and using ReDoc on

```
http://localhost:8000/redocs
```

The API schema is available at

```
http://localhost:8000/openapi.json
```

## Exporing and using

You can interactivly use the API with the Swagger UI, curl from the commandline or any http rest compatible client library (eg requests).

## Python client library

A very simple Python API client library wrapper is available as well.

## Python client library generation

As the API server adheres to the OpenAPI v3 specification clients can be generated dynamically. It's easy to generate, for example, a Python client.

```
$ cd turbinia/api_client
$ docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
-i http://192.168.4.80:11111/openapi.json \
-g python \
-o /local/ \
 --additional-properties=packageName=turbinia_python_client
```
