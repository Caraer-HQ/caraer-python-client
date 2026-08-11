# caraer_client.ObjectsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object**](ObjectsApi.md#create_object) | **POST** /api/v2/objects/ | Create new object
[**delete_object**](ObjectsApi.md#delete_object) | **DELETE** /api/v2/objects/{uuid} | Delete object by UUID
[**get_access_grant_candidates**](ObjectsApi.md#get_access_grant_candidates) | **GET** /api/v2/objects/access-grant/candidates | List access grant candidates
[**get_object**](ObjectsApi.md#get_object) | **GET** /api/v2/objects/{uuid} | Get object by UUID
[**get_objects**](ObjectsApi.md#get_objects) | **POST** /api/v2/objects/index | Fetch paginated objects
[**get_preview**](ObjectsApi.md#get_preview) | **GET** /api/v2/objects/{uuid}/previews/{name} | Get specific preview by name
[**get_previews**](ObjectsApi.md#get_previews) | **POST** /api/v2/objects/previews | Get all previews over all objects
[**get_previews1**](ObjectsApi.md#get_previews1) | **GET** /api/v2/objects/{uuid}/previews | Get all previews of an object
[**grant_object_access**](ObjectsApi.md#grant_object_access) | **POST** /api/v2/objects/{objectUuid}/access-grant | Grant object record access
[**permanently_delete_archived_object**](ObjectsApi.md#permanently_delete_archived_object) | **DELETE** /api/v2/objects/{uuid}/permanent | Permanently delete archived object
[**save_preview**](ObjectsApi.md#save_preview) | **POST** /api/v2/objects/{uuid}/previews/{name} | Save object preview
[**sync_extended_objects**](ObjectsApi.md#sync_extended_objects) | **POST** /api/v2/objects/{uuid}/syncExtendedObjects | Sync extended objects for existing records
[**update_indices3**](ObjectsApi.md#update_indices3) | **PUT** /api/v2/objects/updateIndices | Update object indices
[**update_lifecycle_properties**](ObjectsApi.md#update_lifecycle_properties) | **PUT** /api/v2/objects/{objectUuid}/lifecycle-properties | Configure lifecycle property tracking
[**update_object**](ObjectsApi.md#update_object) | **PUT** /api/v2/objects/{uuid} | Update object by UUID


# **create_object**
> CreateResponse create_object(caraer_object_dto, views=views, properties=properties, relations=relations)

Create new object

Creates a new Caraer object using the provided details. Optional request parameters specify whether to include views, properties, and relations in the response. Validation rules: label (required, must be a string, maximum 32 characters), plural (required, must be a string, maximum 32 characters), name (required, must be a string, must be lowercase, must be unique, must match name pattern (lowercase letters, numbers, underscores)), description (optional, maximum 255 characters), groups (required, must be an array of string, no duplicate values allowed), showInMenu (required, must be a boolean).

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.caraer_object_dto import CaraerObjectDTO
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
    api_instance = caraer_client.ObjectsApi(api_client)
    caraer_object_dto = caraer_client.CaraerObjectDTO() # CaraerObjectDTO | Details of the object to create
    views = 'false' # str |  (optional) (default to 'false')
    properties = 'false' # str |  (optional) (default to 'false')
    relations = 'false' # str |  (optional) (default to 'false')

    try:
        # Create new object
        api_response = api_instance.create_object(caraer_object_dto, views=views, properties=properties, relations=relations)
        print("The response of ObjectsApi->create_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->create_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **caraer_object_dto** | [**CaraerObjectDTO**](CaraerObjectDTO.md)| Details of the object to create | 
 **views** | **str**|  | [optional] [default to &#39;false&#39;]
 **properties** | **str**|  | [optional] [default to &#39;false&#39;]
 **relations** | **str**|  | [optional] [default to &#39;false&#39;]

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
**201** | Object successfully created |  -  |
**400** | Invalid input |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object**
> DeleteResponse delete_object(uuid)

Delete object by UUID

Deletes a specific object identified by its UUID.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete object by UUID
        api_response = api_instance.delete_object(uuid)
        print("The response of ObjectsApi->delete_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->delete_object: %s\n" % e)
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
**200** | Object deleted successfully |  -  |
**404** | Object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_grant_candidates**
> ShowResponseObjectAccessGrantCandidatesDTO get_access_grant_candidates()

List access grant candidates

Returns all company users, teams, and installed apps that can receive record access on an object.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_object_access_grant_candidates_dto import ShowResponseObjectAccessGrantCandidatesDTO
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
    api_instance = caraer_client.ObjectsApi(api_client)

    try:
        # List access grant candidates
        api_response = api_instance.get_access_grant_candidates()
        print("The response of ObjectsApi->get_access_grant_candidates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_access_grant_candidates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponseObjectAccessGrantCandidatesDTO**](ShowResponseObjectAccessGrantCandidatesDTO.md)

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

# **get_object**
> ShowResponse get_object(uuid, views=views, properties=properties, relations=relations)

Get object by UUID

Fetches a single object by its UUID. Optional parameters determine whether to include views, properties, and relations in the response.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 
    views = 'false' # str |  (optional) (default to 'false')
    properties = 'false' # str |  (optional) (default to 'false')
    relations = 'false' # str |  (optional) (default to 'false')

    try:
        # Get object by UUID
        api_response = api_instance.get_object(uuid, views=views, properties=properties, relations=relations)
        print("The response of ObjectsApi->get_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **views** | **str**|  | [optional] [default to &#39;false&#39;]
 **properties** | **str**|  | [optional] [default to &#39;false&#39;]
 **relations** | **str**|  | [optional] [default to &#39;false&#39;]

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object fetched successfully |  -  |
**404** | Object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objects**
> PaginationResponse get_objects(body, views=views, properties=properties, relations=relations)

Fetch paginated objects

Fetches a paginated list of objects, optionally including views, properties, and/or relations. The request body should contain pagination details such as limit, page, filters, sort, and query.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    body = None # object | Pagination request details
    views = 'false' # str |  (optional) (default to 'false')
    properties = 'false' # str |  (optional) (default to 'false')
    relations = 'false' # str |  (optional) (default to 'false')

    try:
        # Fetch paginated objects
        api_response = api_instance.get_objects(body, views=views, properties=properties, relations=relations)
        print("The response of ObjectsApi->get_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Pagination request details | 
 **views** | **str**|  | [optional] [default to &#39;false&#39;]
 **properties** | **str**|  | [optional] [default to &#39;false&#39;]
 **relations** | **str**|  | [optional] [default to &#39;false&#39;]

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
**200** | Objects fetched successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview**
> ShowResponse get_preview(uuid, name)

Get specific preview by name

Fetches a preview for an object by the object's UUID and the preview name. Returns the preview data wrapped in a ShowResponse.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get specific preview by name
        api_response = api_instance.get_preview(uuid, name)
        print("The response of ObjectsApi->get_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **name** | **str**|  | 

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
**200** | Successfully fetched preview |  -  |
**404** | Object or preview not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_previews**
> PaginationResponse get_previews(body)

Get all previews over all objects

Fetches all previews over all objects. Returns a PaginationResponse containing a list of preview DTOs.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    body = None # object | 

    try:
        # Get all previews over all objects
        api_response = api_instance.get_previews(body)
        print("The response of ObjectsApi->get_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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
**200** | Successfully fetched previews |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_previews1**
> PaginationResponse get_previews1(uuid, search=search)

Get all previews of an object

Fetches all previews associated with a specific object. Returns a PaginationResponse containing a list of preview DTOs.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 
    search = '' # str |  (optional) (default to '')

    try:
        # Get all previews of an object
        api_response = api_instance.get_previews1(uuid, search=search)
        print("The response of ObjectsApi->get_previews1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->get_previews1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **search** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PaginationResponse**](PaginationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched previews |  -  |
**404** | Object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_object_access**
> SuccessResponseVoid grant_object_access(object_uuid, object_access_grant_request_dto)

Grant object record access

Accepts a request to grant record-level scopes on the object to selected users, teams, and installed apps. Validation runs synchronously; grants are applied asynchronously. Returns 202 Accepted on success.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.object_access_grant_request_dto import ObjectAccessGrantRequestDTO
from caraer_client.models.success_response_void import SuccessResponseVoid
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
    api_instance = caraer_client.ObjectsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    object_access_grant_request_dto = caraer_client.ObjectAccessGrantRequestDTO() # ObjectAccessGrantRequestDTO | 

    try:
        # Grant object record access
        api_response = api_instance.grant_object_access(object_uuid, object_access_grant_request_dto)
        print("The response of ObjectsApi->grant_object_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->grant_object_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **object_access_grant_request_dto** | [**ObjectAccessGrantRequestDTO**](ObjectAccessGrantRequestDTO.md)|  | 

### Return type

[**SuccessResponseVoid**](SuccessResponseVoid.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Grant accepted and processing in the background |  -  |
**400** | Invalid request |  -  |
**404** | Object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permanently_delete_archived_object**
> DeleteResponse permanently_delete_archived_object(uuid)

Permanently delete archived object

Hard-deletes a soft-deleted object. Only objects with deletedAt set can be removed.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Permanently delete archived object
        api_response = api_instance.permanently_delete_archived_object(uuid)
        print("The response of ObjectsApi->permanently_delete_archived_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->permanently_delete_archived_object: %s\n" % e)
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
**200** | Object permanently deleted |  -  |
**400** | Object is not archived |  -  |
**404** | Object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_preview**
> CreateResponse save_preview(uuid, name, preview_dto)

Save object preview

Creates or updates a preview for a specific object. The preview type is determined by the 'name' path variable. Depending on the preview type (e.g., 'detail', 'flow', 'pill', or 'page'), the request body will be mapped to the corresponding PreviewDTO and converted to the appropriate Preview model.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.preview_dto import PreviewDTO
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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 
    name = 'name_example' # str | 
    preview_dto = caraer_client.PreviewDTO() # PreviewDTO | Preview data

    try:
        # Save object preview
        api_response = api_instance.save_preview(uuid, name, preview_dto)
        print("The response of ObjectsApi->save_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->save_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **name** | **str**|  | 
 **preview_dto** | [**PreviewDTO**](PreviewDTO.md)| Preview data | 

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
**201** | Successfully created or updated preview |  -  |
**404** | Object or preview not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_extended_objects**
> SuccessResponse sync_extended_objects(uuid)

Sync extended objects for existing records

Synchronizes existing records for an object after extended configuration changes. The object path variable accepts UUID or object name. Records that reference the object as primary object, extended object, or label are re-extended.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Sync extended objects for existing records
        api_response = api_instance.sync_extended_objects(uuid)
        print("The response of ObjectsApi->sync_extended_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->sync_extended_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extended objects synchronized successfully |  -  |
**404** | Object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_indices3**
> update_indices3(body, views=views, properties=properties, relations=relations)

Update object indices

Updates indices of objects based on the provided mapping. The request body should contain a mapping of object UUIDs to index values. Optional request parameters determine if views, properties, and relations should be included in the response.

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
    api_instance = caraer_client.ObjectsApi(api_client)
    body = 'body_example' # str | Mapping of object indices
    views = 'false' # str |  (optional) (default to 'false')
    properties = 'false' # str |  (optional) (default to 'false')
    relations = 'false' # str |  (optional) (default to 'false')

    try:
        # Update object indices
        api_instance.update_indices3(body, views=views, properties=properties, relations=relations)
    except Exception as e:
        print("Exception when calling ObjectsApi->update_indices3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Mapping of object indices | 
 **views** | **str**|  | [optional] [default to &#39;false&#39;]
 **properties** | **str**|  | [optional] [default to &#39;false&#39;]
 **relations** | **str**|  | [optional] [default to &#39;false&#39;]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indices updated successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lifecycle_properties**
> UpdateResponse update_lifecycle_properties(object_uuid, update_lifecycle_properties_dto)

Configure lifecycle property tracking

Sets which properties on this object should generate lifecycle history records when their values change.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.update_lifecycle_properties_dto import UpdateLifecyclePropertiesDTO
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
    api_instance = caraer_client.ObjectsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    update_lifecycle_properties_dto = caraer_client.UpdateLifecyclePropertiesDTO() # UpdateLifecyclePropertiesDTO | 

    try:
        # Configure lifecycle property tracking
        api_response = api_instance.update_lifecycle_properties(object_uuid, update_lifecycle_properties_dto)
        print("The response of ObjectsApi->update_lifecycle_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->update_lifecycle_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **update_lifecycle_properties_dto** | [**UpdateLifecyclePropertiesDTO**](UpdateLifecyclePropertiesDTO.md)|  | 

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
**200** | Lifecycle properties updated |  -  |
**404** | Object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object**
> UpdateResponse update_object(uuid, caraer_object_dto, views=views, properties=properties, relations=relations)

Update object by UUID

Updates an existing object identified by its UUID with new details. Optional parameters determine if views, properties, and relations should be included in the response. Validation rules: label (required, must be a string, maximum 32 characters), plural (required, must be a string, maximum 32 characters), name (required, must be a string, must be lowercase, must be unique, must match name pattern (lowercase letters, numbers, underscores), cannot be changed after creation), description (optional, maximum 255 characters), groups (required, must be an array of string, no duplicate values allowed), showInMenu (required, must be a boolean).

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.caraer_object_dto import CaraerObjectDTO
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
    api_instance = caraer_client.ObjectsApi(api_client)
    uuid = 'uuid_example' # str | 
    caraer_object_dto = caraer_client.CaraerObjectDTO() # CaraerObjectDTO | Updated details of the object
    views = 'false' # str |  (optional) (default to 'false')
    properties = 'false' # str |  (optional) (default to 'false')
    relations = 'false' # str |  (optional) (default to 'false')

    try:
        # Update object by UUID
        api_response = api_instance.update_object(uuid, caraer_object_dto, views=views, properties=properties, relations=relations)
        print("The response of ObjectsApi->update_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->update_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **caraer_object_dto** | [**CaraerObjectDTO**](CaraerObjectDTO.md)| Updated details of the object | 
 **views** | **str**|  | [optional] [default to &#39;false&#39;]
 **properties** | **str**|  | [optional] [default to &#39;false&#39;]
 **relations** | **str**|  | [optional] [default to &#39;false&#39;]

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
**200** | Object updated successfully |  -  |
**400** | Invalid input |  -  |
**404** | Object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

