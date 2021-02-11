# turbinia-python-client

## Requirements.

Python >= 3.6

## Installation & Usage

### pip install

```sh
pip install turbinia_python_client
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import turbinia_python_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import turbinia_python_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import turbinia_python_client
from pprint import pprint
from turbinia_python_client.api import default_api
from turbinia_python_client.model.evidence import Evidence
from turbinia_python_client.model.http_validation_error import HTTPValidationError
from turbinia_python_client.model.request import Request
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = turbinia_python_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with turbinia_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    evidence_type = Evidence("compresseddirectory") # Evidence |
request = Request(
        request_id="request_id_example",
        request_options=RequestOptions(
            generic=Generic(
                job_allowlist=[
                    "job_allowlist_example",
                ],
                job_denylist=[
                    "job_denylist_example",
                ],
                source_path="source_path_example",
                output_json=True,
            ),
            gcp=GCP(
                disk_name="disk_name_example",
                project_name="project_name_example",
                zone="zone_example",
            ),
        ),
    ) # Request |

    try:
        # Createrequest
        api_response = api_instance.createrequest_create_evidence_type_post(evidence_type, request)
        pprint(api_response)
    except turbinia_python_client.ApiException as e:
        print("Exception when calling DefaultApi->createrequest_create_evidence_type_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to _http://localhost_

| Class        | Method                                                                                                            | HTTP request                         | Description    |
| ------------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------------- |
| _DefaultApi_ | [**createrequest_create_evidence_type_post**](docs/DefaultApi.md#createrequest_create_evidence_type_post)         | **POST** /create/{evidence_type}     | Createrequest  |
| _DefaultApi_ | [**root_get**](docs/DefaultApi.md#root_get)                                                                       | **GET** /                            | Root           |
| _DefaultApi_ | [**statusrequest_status_request_request_id_get**](docs/DefaultApi.md#statusrequest_status_request_request_id_get) | **GET** /status/request/{request_id} | Statusrequest  |
| _DefaultApi_ | [**statusrequests_status_requests_get**](docs/DefaultApi.md#statusrequests_status_requests_get)                   | **GET** /status/requests             | Statusrequests |

## Documentation For Models

- [Evidence](docs/Evidence.md)
- [GCP](docs/GCP.md)
- [Generic](docs/Generic.md)
- [HTTPValidationError](docs/HTTPValidationError.md)
- [Request](docs/Request.md)
- [RequestOptions](docs/RequestOptions.md)
- [ValidationError](docs/ValidationError.md)

## Documentation For Authorization

All endpoints do not require authorization.
