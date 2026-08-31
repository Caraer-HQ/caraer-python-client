# caraer_client.ModuleApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_module**](ModuleApi.md#create_module) | **POST** /api/v2/modules/ | Create a new module
[**create_personal_module**](ModuleApi.md#create_personal_module) | **POST** /api/v2/modules/personal/ | Create a personal module
[**delete_module**](ModuleApi.md#delete_module) | **DELETE** /api/v2/modules/{moduleId} | Delete a module
[**delete_personal_module**](ModuleApi.md#delete_personal_module) | **DELETE** /api/v2/modules/personal/{moduleId} | Delete a personal module
[**get_module**](ModuleApi.md#get_module) | **GET** /api/v2/modules/{moduleId} | Fetch a specific module
[**get_modules**](ModuleApi.md#get_modules) | **POST** /api/v2/modules/index | Fetch paginated modules
[**get_personal_module**](ModuleApi.md#get_personal_module) | **GET** /api/v2/modules/personal/{moduleId} | Fetch a personal module
[**get_personal_modules**](ModuleApi.md#get_personal_modules) | **POST** /api/v2/modules/personal/index | Fetch paginated personal modules
[**update_module**](ModuleApi.md#update_module) | **PUT** /api/v2/modules/{moduleId} | Update an existing module
[**update_personal_module**](ModuleApi.md#update_personal_module) | **PUT** /api/v2/modules/personal/{moduleId} | Update a personal module


# **create_module**
> CreateResponse create_module(page_content_dto)

Create a new module

Creates a new module.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.page_content_dto import PageContentDTO
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
    api_instance = caraer_client.ModuleApi(api_client)
    page_content_dto = caraer_client.PageContentDTO() # PageContentDTO | Module details

    try:
        # Create a new module
        api_response = api_instance.create_module(page_content_dto)
        print("The response of ModuleApi->create_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->create_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_content_dto** | [**PageContentDTO**](PageContentDTO.md)| Module details | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Module created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_personal_module**
> CreateResponse create_personal_module(page_content_dto)

Create a personal module

Creates a module in the user's personal library.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.page_content_dto import PageContentDTO
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
    api_instance = caraer_client.ModuleApi(api_client)
    page_content_dto = caraer_client.PageContentDTO() # PageContentDTO | 

    try:
        # Create a personal module
        api_response = api_instance.create_personal_module(page_content_dto)
        print("The response of ModuleApi->create_personal_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->create_personal_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_content_dto** | [**PageContentDTO**](PageContentDTO.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Module created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_module**
> DeleteResponse delete_module(module_id)

Delete a module

Deletes a module by its UUID.

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
    api_instance = caraer_client.ModuleApi(api_client)
    module_id = 'module_id_example' # str | 

    try:
        # Delete a module
        api_response = api_instance.delete_module(module_id)
        print("The response of ModuleApi->delete_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->delete_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 

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
**200** | Module deleted successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_personal_module**
> DeleteResponse delete_personal_module(module_id)

Delete a personal module

Deletes a personal module for the logged-in user.

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
    api_instance = caraer_client.ModuleApi(api_client)
    module_id = 'module_id_example' # str | 

    try:
        # Delete a personal module
        api_response = api_instance.delete_personal_module(module_id)
        print("The response of ModuleApi->delete_personal_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->delete_personal_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 

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
**200** | Module deleted successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module**
> ShowResponsePageContentDTO get_module(module_id)

Fetch a specific module

Retrieves details of a module by its UUID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_page_content_dto import ShowResponsePageContentDTO
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
    api_instance = caraer_client.ModuleApi(api_client)
    module_id = 'module_id_example' # str | 

    try:
        # Fetch a specific module
        api_response = api_instance.get_module(module_id)
        print("The response of ModuleApi->get_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->get_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 

### Return type

[**ShowResponsePageContentDTO**](ShowResponsePageContentDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Module retrieved successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_modules**
> PaginationResponsePageContentDTO get_modules(pagination_request)

Fetch paginated modules

Retrieves a paginated list of modules.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_page_content_dto import PaginationResponsePageContentDTO
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
    api_instance = caraer_client.ModuleApi(api_client)
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | Pagination details

    try:
        # Fetch paginated modules
        api_response = api_instance.get_modules(pagination_request)
        print("The response of ModuleApi->get_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->get_modules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)| Pagination details | 

### Return type

[**PaginationResponsePageContentDTO**](PaginationResponsePageContentDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modules fetched successfully |  -  |
**400** | Invalid pagination request |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_module**
> ShowResponsePageContentDTO get_personal_module(module_id)

Fetch a personal module

Retrieves a personal module by UUID for the logged-in user.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_page_content_dto import ShowResponsePageContentDTO
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
    api_instance = caraer_client.ModuleApi(api_client)
    module_id = 'module_id_example' # str | 

    try:
        # Fetch a personal module
        api_response = api_instance.get_personal_module(module_id)
        print("The response of ModuleApi->get_personal_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->get_personal_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 

### Return type

[**ShowResponsePageContentDTO**](ShowResponsePageContentDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Module retrieved successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_modules**
> PaginationResponsePageContentDTO get_personal_modules(pagination_request)

Fetch paginated personal modules

Retrieves personal modules for the logged-in user.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_page_content_dto import PaginationResponsePageContentDTO
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
    api_instance = caraer_client.ModuleApi(api_client)
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Fetch paginated personal modules
        api_response = api_instance.get_personal_modules(pagination_request)
        print("The response of ModuleApi->get_personal_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->get_personal_modules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponsePageContentDTO**](PaginationResponsePageContentDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modules fetched successfully |  -  |
**400** | Invalid pagination request |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_module**
> UpdateResponse update_module(module_id, page_content_dto)

Update an existing module

Updates the details of an existing module.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.page_content_dto import PageContentDTO
from caraer_client.models.update_response import UpdateResponse
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
    api_instance = caraer_client.ModuleApi(api_client)
    module_id = 'module_id_example' # str | 
    page_content_dto = caraer_client.PageContentDTO() # PageContentDTO | Updated module details

    try:
        # Update an existing module
        api_response = api_instance.update_module(module_id, page_content_dto)
        print("The response of ModuleApi->update_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->update_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **page_content_dto** | [**PageContentDTO**](PageContentDTO.md)| Updated module details | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Module updated successfully |  -  |
**400** | Invalid input data |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_personal_module**
> UpdateResponse update_personal_module(module_id, page_content_dto)

Update a personal module

Updates a personal module for the logged-in user.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.page_content_dto import PageContentDTO
from caraer_client.models.update_response import UpdateResponse
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
    api_instance = caraer_client.ModuleApi(api_client)
    module_id = 'module_id_example' # str | 
    page_content_dto = caraer_client.PageContentDTO() # PageContentDTO | 

    try:
        # Update a personal module
        api_response = api_instance.update_personal_module(module_id, page_content_dto)
        print("The response of ModuleApi->update_personal_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->update_personal_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **page_content_dto** | [**PageContentDTO**](PageContentDTO.md)|  | 

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
**200** | Module updated successfully |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

