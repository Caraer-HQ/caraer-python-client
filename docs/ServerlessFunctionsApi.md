# caraer_client.ServerlessFunctionsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](ServerlessFunctionsApi.md#create3) | **POST** /api/v2/apps/{appUuid}/serverless-functions | Create a serverless function
[**delete1**](ServerlessFunctionsApi.md#delete1) | **DELETE** /api/v2/apps/{appUuid}/serverless-functions/{uuid} | Delete a serverless function
[**index2**](ServerlessFunctionsApi.md#index2) | **POST** /api/v2/apps/{appUuid}/serverless-functions/index | List serverless functions for an app
[**logs**](ServerlessFunctionsApi.md#logs) | **GET** /api/v2/apps/{appUuid}/serverless-functions/{uuid}/logs | Get serverless function logs
[**sample_payload**](ServerlessFunctionsApi.md#sample_payload) | **POST** /api/v2/apps/{appUuid}/serverless-functions/sample-payload | Generate a sample webhook payload
[**show1**](ServerlessFunctionsApi.md#show1) | **GET** /api/v2/apps/{appUuid}/serverless-functions/{uuid} | Get a serverless function
[**test_serverless_function**](ServerlessFunctionsApi.md#test_serverless_function) | **POST** /api/v2/apps/{appUuid}/serverless-functions/{uuid}/test | Test a serverless function
[**update1**](ServerlessFunctionsApi.md#update1) | **PUT** /api/v2/apps/{appUuid}/serverless-functions/{uuid} | Update a serverless function


# **create3**
> CreateResponse create3(app_uuid, serverless_function_dto)

Create a serverless function

Creates a new serverless function attached to the specified app.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.serverless_function_dto import ServerlessFunctionDTO
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app to attach the serverless function to
    serverless_function_dto = caraer_client.ServerlessFunctionDTO() # ServerlessFunctionDTO | Serverless function payload (runtime and code)

    try:
        # Create a serverless function
        api_response = api_instance.create3(app_uuid, serverless_function_dto)
        print("The response of ServerlessFunctionsApi->create3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->create3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app to attach the serverless function to | 
 **serverless_function_dto** | [**ServerlessFunctionDTO**](ServerlessFunctionDTO.md)| Serverless function payload (runtime and code) | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created serverless function |  -  |
**400** | Invalid request or app not installed for company |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> DeleteResponse delete1(app_uuid, uuid)

Delete a serverless function

Tears down the GCP Cloud Function (if provisioned) and deletes the serverless function entity.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.delete_response import DeleteResponse
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    uuid = 'uuid_example' # str | UUID of the serverless function to delete

    try:
        # Delete a serverless function
        api_response = api_instance.delete1(app_uuid, uuid)
        print("The response of ServerlessFunctionsApi->delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->delete1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **uuid** | **str**| UUID of the serverless function to delete | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted serverless function |  -  |
**404** | Serverless function not found for this app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index2**
> PaginationResponse index2(app_uuid, body)

List serverless functions for an app

Retrieves a paginated list of serverless functions that belong to the specified app.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_response import PaginationResponse
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app whose serverless functions to list
    body = None # object | Pagination and filtering options for the request

    try:
        # List serverless functions for an app
        api_response = api_instance.index2(app_uuid, body)
        print("The response of ServerlessFunctionsApi->index2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->index2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app whose serverless functions to list | 
 **body** | **object**| Pagination and filtering options for the request | 

### Return type

[**PaginationResponse**](PaginationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved serverless functions |  -  |
**400** | Invalid request or app not installed for company |  -  |
**401** | Unauthorized access |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logs**
> SuccessResponse logs(app_uuid, uuid, since=since, limit=limit)

Get serverless function logs

Queries Cloud Logging for recent log entries emitted by the Cloud Function backing this serverless function.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response import SuccessResponse
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    uuid = 'uuid_example' # str | UUID of the serverless function
    since = '1h' # str | Lookback window, e.g. 15m, 1h, 24h (optional) (default to '1h')
    limit = 100 # int | Maximum number of log entries to return (optional) (default to 100)

    try:
        # Get serverless function logs
        api_response = api_instance.logs(app_uuid, uuid, since=since, limit=limit)
        print("The response of ServerlessFunctionsApi->logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **uuid** | **str**| UUID of the serverless function | 
 **since** | **str**| Lookback window, e.g. 15m, 1h, 24h | [optional] [default to &#39;1h&#39;]
 **limit** | **int**| Maximum number of log entries to return | [optional] [default to 100]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved logs (may be empty if logging is unavailable) |  -  |
**404** | Serverless function not found for this app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_payload**
> SuccessResponse sample_payload(app_uuid, sample_payload_request)

Generate a sample webhook payload

Builds the same payload shape used for serverless invocations and webhook delivery from a record and event type, without invoking anything.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.sample_payload_request import SamplePayloadRequest
from caraer_client.models.success_response import SuccessResponse
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    sample_payload_request = caraer_client.SamplePayloadRequest() # SamplePayloadRequest | Sample payload request (recordUuid and eventType)

    try:
        # Generate a sample webhook payload
        api_response = api_instance.sample_payload(app_uuid, sample_payload_request)
        print("The response of ServerlessFunctionsApi->sample_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->sample_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **sample_payload_request** | [**SamplePayloadRequest**](SamplePayloadRequest.md)| Sample payload request (recordUuid and eventType) | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample payload generated |  -  |
**400** | Invalid input provided |  -  |
**404** | App or record not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show1**
> ShowResponse show1(app_uuid, uuid)

Get a serverless function

Retrieves a serverless function by its UUID, ensuring it belongs to the specified app.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response import ShowResponse
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    uuid = 'uuid_example' # str | UUID of the serverless function

    try:
        # Get a serverless function
        api_response = api_instance.show1(app_uuid, uuid)
        print("The response of ServerlessFunctionsApi->show1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->show1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **uuid** | **str**| UUID of the serverless function | 

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved serverless function |  -  |
**404** | Serverless function not found for this app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_serverless_function**
> SuccessResponse test_serverless_function(app_uuid, uuid, test_serverless_function_request)

Test a serverless function

Provisions (if needed) and invokes a serverless function for a given record and event type, using the same payload shape as webhooks.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response import SuccessResponse
from caraer_client.models.test_serverless_function_request import TestServerlessFunctionRequest
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    uuid = 'uuid_example' # str | UUID of the serverless function to test
    test_serverless_function_request = caraer_client.TestServerlessFunctionRequest() # TestServerlessFunctionRequest | Test serverless function payload (recordUuid and eventType)

    try:
        # Test a serverless function
        api_response = api_instance.test_serverless_function(app_uuid, uuid, test_serverless_function_request)
        print("The response of ServerlessFunctionsApi->test_serverless_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->test_serverless_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **uuid** | **str**| UUID of the serverless function to test | 
 **test_serverless_function_request** | [**TestServerlessFunctionRequest**](TestServerlessFunctionRequest.md)| Test serverless function payload (recordUuid and eventType) | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Serverless function test executed |  -  |
**400** | Invalid input provided |  -  |
**404** | App, serverless function, or record not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> ShowResponse update1(app_uuid, uuid, serverless_function_dto)

Update a serverless function

Updates an existing serverless function's runtime and code, keeping it attached to the same app.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.serverless_function_dto import ServerlessFunctionDTO
from caraer_client.models.show_response import ShowResponse
from caraer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://v2.api.caraer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = caraer_client.Configuration(
    host = "https://v2.api.caraer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = caraer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with caraer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = caraer_client.ServerlessFunctionsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    uuid = 'uuid_example' # str | UUID of the serverless function to update
    serverless_function_dto = caraer_client.ServerlessFunctionDTO() # ServerlessFunctionDTO | Updated serverless function payload (runtime and code)

    try:
        # Update a serverless function
        api_response = api_instance.update1(app_uuid, uuid, serverless_function_dto)
        print("The response of ServerlessFunctionsApi->update1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerlessFunctionsApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **uuid** | **str**| UUID of the serverless function to update | 
 **serverless_function_dto** | [**ServerlessFunctionDTO**](ServerlessFunctionDTO.md)| Updated serverless function payload (runtime and code) | 

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated serverless function |  -  |
**404** | Serverless function not found for this app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

