"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from turbinia_python_client.api_client import ApiClient, Endpoint as _Endpoint
from turbinia_python_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from turbinia_python_client.model.evidence import Evidence
from turbinia_python_client.model.http_validation_error import HTTPValidationError
from turbinia_python_client.model.request import Request


class DefaultApi(object):
  """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

  def __init__(self, api_client=None):
    if api_client is None:
      api_client = ApiClient()
    self.api_client = api_client

    def __createrequest_create_evidence_type_post(
        self, evidence_type, request, **kwargs):
      """Createrequest  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.createrequest_create_evidence_type_post(evidence_type, request, async_req=True)
            >>> result = thread.get()

            Args:
                evidence_type (Evidence):
                request (Request):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
      kwargs['async_req'] = kwargs.get('async_req', False)
      kwargs['_return_http_data_only'] = kwargs.get(
          '_return_http_data_only', True)
      kwargs['_preload_content'] = kwargs.get('_preload_content', True)
      kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
      kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
      kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
      kwargs['_host_index'] = kwargs.get('_host_index')
      kwargs['evidence_type'] = \
          evidence_type
      kwargs['request'] = \
          request
      return self.call_with_http_info(**kwargs)

    self.createrequest_create_evidence_type_post = _Endpoint(
        settings={
            'response_type': (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),
            'auth': [],
            'endpoint_path': '/create/{evidence_type}',
            'operation_id': 'createrequest_create_evidence_type_post',
            'http_method': 'POST',
            'servers': None,
        }, params_map={
            'all': [
                'evidence_type',
                'request',
            ],
            'required': [
                'evidence_type',
                'request',
            ],
            'nullable': [],
            'enum': [],
            'validation': []
        }, root_map={
            'validations': {},
            'allowed_values': {},
            'openapi_types': {
                'evidence_type': (Evidence,),
                'request': (Request,),
            },
            'attribute_map': {
                'evidence_type': 'evidence_type',
            },
            'location_map': {
                'evidence_type': 'path',
                'request': 'body',
            },
            'collection_format_map': {}
        }, headers_map={
            'accept': ['application/json'],
            'content_type': ['application/json']
        }, api_client=api_client,
        callable=__createrequest_create_evidence_type_post)

    def __root_get(self, **kwargs):
      """Root  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.root_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
      kwargs['async_req'] = kwargs.get('async_req', False)
      kwargs['_return_http_data_only'] = kwargs.get(
          '_return_http_data_only', True)
      kwargs['_preload_content'] = kwargs.get('_preload_content', True)
      kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
      kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
      kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
      kwargs['_host_index'] = kwargs.get('_host_index')
      return self.call_with_http_info(**kwargs)

    self.root_get = _Endpoint(
        settings={
            'response_type': (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),
            'auth': [],
            'endpoint_path': '/',
            'operation_id': 'root_get',
            'http_method': 'GET',
            'servers': None,
        }, params_map={
            'all': [],
            'required': [],
            'nullable': [],
            'enum': [],
            'validation': []
        }, root_map={
            'validations': {},
            'allowed_values': {},
            'openapi_types': {},
            'attribute_map': {},
            'location_map': {},
            'collection_format_map': {}
        }, headers_map={
            'accept': ['application/json'],
            'content_type': [],
        }, api_client=api_client, callable=__root_get)

    def __statusrequest_status_request_request_id_get(
        self, request_id, **kwargs):
      """Statusrequest  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.statusrequest_status_request_request_id_get(request_id, async_req=True)
            >>> result = thread.get()

            Args:
                request_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
      kwargs['async_req'] = kwargs.get('async_req', False)
      kwargs['_return_http_data_only'] = kwargs.get(
          '_return_http_data_only', True)
      kwargs['_preload_content'] = kwargs.get('_preload_content', True)
      kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
      kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
      kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
      kwargs['_host_index'] = kwargs.get('_host_index')
      kwargs['request_id'] = \
          request_id
      return self.call_with_http_info(**kwargs)

    self.statusrequest_status_request_request_id_get = _Endpoint(
        settings={
            'response_type': (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),
            'auth': [],
            'endpoint_path': '/status/request/{request_id}',
            'operation_id': 'statusrequest_status_request_request_id_get',
            'http_method': 'GET',
            'servers': None,
        }, params_map={
            'all': ['request_id',],
            'required': ['request_id',],
            'nullable': [],
            'enum': [],
            'validation': []
        }, root_map={
            'validations': {},
            'allowed_values': {},
            'openapi_types': {
                'request_id': (str,),
            },
            'attribute_map': {
                'request_id': 'request_id',
            },
            'location_map': {
                'request_id': 'path',
            },
            'collection_format_map': {}
        }, headers_map={
            'accept': ['application/json'],
            'content_type': [],
        }, api_client=api_client,
        callable=__statusrequest_status_request_request_id_get)

    def __statusrequests_status_requests_get(self, **kwargs):
      """Statusrequests  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.statusrequests_status_requests_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool, date, datetime, dict, float, int, list, str, none_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
      kwargs['async_req'] = kwargs.get('async_req', False)
      kwargs['_return_http_data_only'] = kwargs.get(
          '_return_http_data_only', True)
      kwargs['_preload_content'] = kwargs.get('_preload_content', True)
      kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
      kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
      kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
      kwargs['_host_index'] = kwargs.get('_host_index')
      return self.call_with_http_info(**kwargs)

    self.statusrequests_status_requests_get = _Endpoint(
        settings={
            'response_type': (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),
            'auth': [],
            'endpoint_path': '/status/requests',
            'operation_id': 'statusrequests_status_requests_get',
            'http_method': 'GET',
            'servers': None,
        }, params_map={
            'all': [],
            'required': [],
            'nullable': [],
            'enum': [],
            'validation': []
        }, root_map={
            'validations': {},
            'allowed_values': {},
            'openapi_types': {},
            'attribute_map': {},
            'location_map': {},
            'collection_format_map': {}
        }, headers_map={
            'accept': ['application/json'],
            'content_type': [],
        }, api_client=api_client, callable=__statusrequests_status_requests_get)
