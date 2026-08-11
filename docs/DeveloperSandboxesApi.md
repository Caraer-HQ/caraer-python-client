# caraer_client.DeveloperSandboxesApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](DeveloperSandboxesApi.md#create1) | **POST** /api/v2/developer-sandboxes | Create a developer sandbox
[**list**](DeveloperSandboxesApi.md#list) | **GET** /api/v2/developer-sandboxes | List developer sandboxes
[**show2**](DeveloperSandboxesApi.md#show2) | **GET** /api/v2/developer-sandboxes/{uuid} | Get a developer sandbox


# **create1**
> CreateResponse create1(create_developer_sandbox_request)

Create a developer sandbox

Clones the selected company's Neo4j database (no new Company node). Activate with X-Caraer-Sandbox-Uuid; company identity stays the owner.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_developer_sandbox_request import CreateDeveloperSandboxRequest
from caraer_client.models.create_response import CreateResponse
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
    api_instance = caraer_client.DeveloperSandboxesApi(api_client)
    create_developer_sandbox_request = caraer_client.CreateDeveloperSandboxRequest() # CreateDeveloperSandboxRequest | 

    try:
        # Create a developer sandbox
        api_response = api_instance.create1(create_developer_sandbox_request)
        print("The response of DeveloperSandboxesApi->create1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperSandboxesApi->create1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_developer_sandbox_request** | [**CreateDeveloperSandboxRequest**](CreateDeveloperSandboxRequest.md)|  | 

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
**200** | Sandbox created |  -  |
**400** | name is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> object list()

List developer sandboxes

Lists sandboxes owned by the caller's selected company.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
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
    api_instance = caraer_client.DeveloperSandboxesApi(api_client)

    try:
        # List developer sandboxes
        api_response = api_instance.list()
        print("The response of DeveloperSandboxesApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperSandboxesApi->list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show2**
> show2(uuid)

Get a developer sandbox

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
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
    api_instance = caraer_client.DeveloperSandboxesApi(api_client)
    uuid = 'uuid_example' # str | UUID of the sandbox

    try:
        # Get a developer sandbox
        api_instance.show2(uuid)
    except Exception as e:
        print("Exception when calling DeveloperSandboxesApi->show2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the sandbox | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Caller does not own this sandbox |  -  |
**404** | Sandbox not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

