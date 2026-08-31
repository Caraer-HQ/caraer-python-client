# caraer_client.WebMenusApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_menu**](WebMenusApi.md#create_web_menu) | **POST** /api/v2/webmenus | Create web menu
[**delete_web_menu**](WebMenusApi.md#delete_web_menu) | **DELETE** /api/v2/webmenus/{uuid} | Delete web menu
[**get_web_menu**](WebMenusApi.md#get_web_menu) | **GET** /api/v2/webmenus/{uuid} | Show web menu
[**index_web_menus**](WebMenusApi.md#index_web_menus) | **POST** /api/v2/webmenus/index | Index web menus
[**restore_web_menu**](WebMenusApi.md#restore_web_menu) | **POST** /api/v2/webmenus/{uuid}/restore | Restore deleted web menu
[**update_web_menu**](WebMenusApi.md#update_web_menu) | **PUT** /api/v2/webmenus/{uuid} | Update web menu


# **create_web_menu**
> CreateResponse create_web_menu(web_menu_dto)

Create web menu

Create web menu

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.web_menu_dto import WebMenuDTO
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
    api_instance = caraer_client.WebMenusApi(api_client)
    web_menu_dto = caraer_client.WebMenuDTO() # WebMenuDTO | 

    try:
        # Create web menu
        api_response = api_instance.create_web_menu(web_menu_dto)
        print("The response of WebMenusApi->create_web_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebMenusApi->create_web_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_menu_dto** | [**WebMenuDTO**](WebMenuDTO.md)|  | 

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
**200** | Web menu created successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_menu**
> DeleteResponse delete_web_menu(uuid)

Delete web menu

Delete web menu

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
    api_instance = caraer_client.WebMenusApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete web menu
        api_response = api_instance.delete_web_menu(uuid)
        print("The response of WebMenusApi->delete_web_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebMenusApi->delete_web_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web menu deleted successfully |  -  |
**400** | Bad request |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_menu**
> ShowResponseWebMenuDTO get_web_menu(uuid)

Show web menu

Show web menu

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_web_menu_dto import ShowResponseWebMenuDTO
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
    api_instance = caraer_client.WebMenusApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Show web menu
        api_response = api_instance.get_web_menu(uuid)
        print("The response of WebMenusApi->get_web_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebMenusApi->get_web_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ShowResponseWebMenuDTO**](ShowResponseWebMenuDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web menu shown successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_web_menus**
> PaginationResponseWebMenuDTO index_web_menus(pagination_request)

Index web menus

Index web menus

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_web_menu_dto import PaginationResponseWebMenuDTO
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
    api_instance = caraer_client.WebMenusApi(api_client)
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Index web menus
        api_response = api_instance.index_web_menus(pagination_request)
        print("The response of WebMenusApi->index_web_menus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebMenusApi->index_web_menus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponseWebMenuDTO**](PaginationResponseWebMenuDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web menus indexed successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_web_menu**
> RestoreResponse restore_web_menu(uuid)

Restore deleted web menu

Restore a deleted web menu by its UUID

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.restore_response import RestoreResponse
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
    api_instance = caraer_client.WebMenusApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Restore deleted web menu
        api_response = api_instance.restore_web_menu(uuid)
        print("The response of WebMenusApi->restore_web_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebMenusApi->restore_web_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**RestoreResponse**](RestoreResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web menu restored successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_menu**
> UpdateResponse update_web_menu(uuid, web_menu_dto)

Update web menu

Update web menu

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.update_response import UpdateResponse
from caraer_client.models.web_menu_dto import WebMenuDTO
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
    api_instance = caraer_client.WebMenusApi(api_client)
    uuid = 'uuid_example' # str | 
    web_menu_dto = caraer_client.WebMenuDTO() # WebMenuDTO | 

    try:
        # Update web menu
        api_response = api_instance.update_web_menu(uuid, web_menu_dto)
        print("The response of WebMenusApi->update_web_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebMenusApi->update_web_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **web_menu_dto** | [**WebMenuDTO**](WebMenuDTO.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web menu updated successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

