# caraer_client.ViewsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](ViewsApi.md#create_view) | **POST** /api/v2/objects/{objectUuid}/views/ | Create a new view
[**delete_view**](ViewsApi.md#delete_view) | **DELETE** /api/v2/objects/{objectUuid}/views/{viewUuid} | Delete a view
[**favorite_view**](ViewsApi.md#favorite_view) | **PUT** /api/v2/objects/{objectUuid}/views/{viewUuid}/favorite | Toggle view favorite status
[**get_view**](ViewsApi.md#get_view) | **GET** /api/v2/objects/{objectUuid}/views/{viewUuid} | Get view details
[**get_views**](ViewsApi.md#get_views) | **POST** /api/v2/objects/{objectUuid}/views/index | Fetch paginated views for an object
[**update_indices1**](ViewsApi.md#update_indices1) | **PUT** /api/v2/objects/{objectUuid}/views/updateIndices | Update view indices
[**update_view**](ViewsApi.md#update_view) | **PUT** /api/v2/objects/{objectUuid}/views/{viewUuid} | Update an existing view


# **create_view**
> CreateResponse create_view(object_uuid, view_dto)

Create a new view

Creates a new view for the specified object. The request body must contain the view details as a ViewDTO. Returns a CreateResponse containing the newly created view as a ViewDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.view_dto import ViewDTO
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
    api_instance = caraer_client.ViewsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    view_dto = caraer_client.ViewDTO() # ViewDTO | View details to create

    try:
        # Create a new view
        api_response = api_instance.create_view(object_uuid, view_dto)
        print("The response of ViewsApi->create_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->create_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **view_dto** | [**ViewDTO**](ViewDTO.md)| View details to create | 

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
**201** | View created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view**
> DeleteResponse delete_view(object_uuid, view_uuid)

Delete a view

Deletes the view identified by its UUID from the specified object. Returns a DeleteResponse confirming the deletion.

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
    api_instance = caraer_client.ViewsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    view_uuid = 'view_uuid_example' # str | 

    try:
        # Delete a view
        api_response = api_instance.delete_view(object_uuid, view_uuid)
        print("The response of ViewsApi->delete_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->delete_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **view_uuid** | **str**|  | 

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
**200** | View deleted successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_view**
> UpdateResponse favorite_view(object_uuid, view_uuid)

Toggle view favorite status

Toggles the favorite status of the specified view. Returns an UpdateResponse containing the updated view details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
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
    api_instance = caraer_client.ViewsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    view_uuid = 'view_uuid_example' # str | 

    try:
        # Toggle view favorite status
        api_response = api_instance.favorite_view(object_uuid, view_uuid)
        print("The response of ViewsApi->favorite_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->favorite_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **view_uuid** | **str**|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | View favorite status updated successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view**
> ShowResponseViewDTO get_view(object_uuid, view_uuid)

Get view details

Retrieves detailed information for a view identified by its UUID for the specified object. Returns a ShowResponse containing the ViewDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_view_dto import ShowResponseViewDTO
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
    api_instance = caraer_client.ViewsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    view_uuid = 'view_uuid_example' # str | 

    try:
        # Get view details
        api_response = api_instance.get_view(object_uuid, view_uuid)
        print("The response of ViewsApi->get_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->get_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **view_uuid** | **str**|  | 

### Return type

[**ShowResponseViewDTO**](ShowResponseViewDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | View retrieved successfully |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_views**
> PaginationResponseViewDTO get_views(object_uuid, pagination_request)

Fetch paginated views for an object

Retrieves a paginated list of views for the specified object. A custom Cypher query is used to filter views based on the object's UUID. Returns a PaginationResponse containing ViewDTO objects.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_view_dto import PaginationResponseViewDTO
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
    api_instance = caraer_client.ViewsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | Pagination request details (limit, page, filters, sort, query)

    try:
        # Fetch paginated views for an object
        api_response = api_instance.get_views(object_uuid, pagination_request)
        print("The response of ViewsApi->get_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->get_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)| Pagination request details (limit, page, filters, sort, query) | 

### Return type

[**PaginationResponseViewDTO**](PaginationResponseViewDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Views fetched successfully |  -  |
**400** | Invalid pagination request |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_indices1**
> SuccessResponseString update_indices1(object_uuid, request_body)

Update view indices

Updates the indices for views associated with the specified object. The request body must include a mapping of view UUIDs to their new index values. Returns a SuccessResponse with the updated view DTOs.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_string import SuccessResponseString
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
    api_instance = caraer_client.ViewsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    request_body = {'key': 56} # Dict[str, int] | Mapping of view UUIDs to new index values

    try:
        # Update view indices
        api_response = api_instance.update_indices1(object_uuid, request_body)
        print("The response of ViewsApi->update_indices1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->update_indices1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **request_body** | [**Dict[str, int]**](int.md)| Mapping of view UUIDs to new index values | 

### Return type

[**SuccessResponseString**](SuccessResponseString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | View indices updated successfully |  -  |
**400** | Invalid input provided |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view**
> UpdateResponse update_view(object_uuid, view_uuid, view_dto)

Update an existing view

Updates the details of an existing view identified by its UUID for the specified object. The request body must contain the updated view details as a ViewDTO. Returns an UpdateResponse with the updated view data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.update_response import UpdateResponse
from caraer_client.models.view_dto import ViewDTO
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
    api_instance = caraer_client.ViewsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    view_uuid = 'view_uuid_example' # str | 
    view_dto = caraer_client.ViewDTO() # ViewDTO | Updated view details

    try:
        # Update an existing view
        api_response = api_instance.update_view(object_uuid, view_uuid, view_dto)
        print("The response of ViewsApi->update_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->update_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **view_uuid** | **str**|  | 
 **view_dto** | [**ViewDTO**](ViewDTO.md)| Updated view details | 

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
**200** | View updated successfully |  -  |
**400** | Invalid input data |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

