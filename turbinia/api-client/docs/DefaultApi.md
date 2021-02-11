# turbinia_python_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createrequest_create_evidence_type_post**](DefaultApi.md#createrequest_create_evidence_type_post) | **POST** /create/{evidence_type} | Createrequest
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**statusrequest_status_request_request_id_get**](DefaultApi.md#statusrequest_status_request_request_id_get) | **GET** /status/request/{request_id} | Statusrequest
[**statusrequests_status_requests_get**](DefaultApi.md#statusrequests_status_requests_get) | **GET** /status/requests | Statusrequests


# **createrequest_create_evidence_type_post**
> bool, date, datetime, dict, float, int, list, str, none_type createrequest_create_evidence_type_post(evidence_type, request)

Createrequest

### Example

```python
import time
import turbinia_python_client
from turbinia_python_client.api import default_api
from turbinia_python_client.model.evidence import Evidence
from turbinia_python_client.model.http_validation_error import HTTPValidationError
from turbinia_python_client.model.request import Request
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = turbinia_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with turbinia_python_client.ApiClient() as api_client:
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

    # example passing only required values which don't have defaults set
    try:
        # Createrequest
        api_response = api_instance.createrequest_create_evidence_type_post(evidence_type, request)
        pprint(api_response)
    except turbinia_python_client.ApiException as e:
        print("Exception when calling DefaultApi->createrequest_create_evidence_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evidence_type** | **Evidence**|  |
 **request** | [**Request**](Request.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> bool, date, datetime, dict, float, int, list, str, none_type root_get()

Root

### Example

```python
import time
import turbinia_python_client
from turbinia_python_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = turbinia_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with turbinia_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Root
        api_response = api_instance.root_get()
        pprint(api_response)
    except turbinia_python_client.ApiException as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statusrequest_status_request_request_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type statusrequest_status_request_request_id_get(request_id)

Statusrequest

### Example

```python
import time
import turbinia_python_client
from turbinia_python_client.api import default_api
from turbinia_python_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = turbinia_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with turbinia_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    request_id = "request_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Statusrequest
        api_response = api_instance.statusrequest_status_request_request_id_get(request_id)
        pprint(api_response)
    except turbinia_python_client.ApiException as e:
        print("Exception when calling DefaultApi->statusrequest_status_request_request_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statusrequests_status_requests_get**
> bool, date, datetime, dict, float, int, list, str, none_type statusrequests_status_requests_get()

Statusrequests

### Example

```python
import time
import turbinia_python_client
from turbinia_python_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = turbinia_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with turbinia_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Statusrequests
        api_response = api_instance.statusrequests_status_requests_get()
        pprint(api_response)
    except turbinia_python_client.ApiException as e:
        print("Exception when calling DefaultApi->statusrequests_status_requests_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

