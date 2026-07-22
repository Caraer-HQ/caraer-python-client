# caraer_client.FilterApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter**](FilterApi.md#create_filter) | **POST** /api/v2/filters | Create a new saved filter
[**delete_filter**](FilterApi.md#delete_filter) | **DELETE** /api/v2/filters/{filterUuid} | Delete a saved filter
[**get_filter**](FilterApi.md#get_filter) | **GET** /api/v2/filters/{filterUuid} | Fetch a specific saved filter
[**get_filters**](FilterApi.md#get_filters) | **POST** /api/v2/filters/index/{objectUuid} | Fetch paginated saved filters
[**update_filter**](FilterApi.md#update_filter) | **PUT** /api/v2/filters/{filterUuid} | Update an existing saved filter


# **create_filter**
> CreateResponse create_filter(saved_filter_dto)

Create a new saved filter

Creates a new saved filter with the provided configuration.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.saved_filter_dto import SavedFilterDTO
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
    api_instance = caraer_client.FilterApi(api_client)
    saved_filter_dto = caraer_client.SavedFilterDTO() # SavedFilterDTO | Saved filter details for creation

    try:
        # Create a new saved filter
        api_response = api_instance.create_filter(saved_filter_dto)
        print("The response of FilterApi->create_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->create_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_filter_dto** | [**SavedFilterDTO**](SavedFilterDTO.md)| Saved filter details for creation | 

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
**201** | Filter created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> DeleteResponse delete_filter(filter_uuid)

Delete a saved filter

Soft deletes a saved filter identified by its UUID.

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
    api_instance = caraer_client.FilterApi(api_client)
    filter_uuid = 'filter_uuid_example' # str | 

    try:
        # Delete a saved filter
        api_response = api_instance.delete_filter(filter_uuid)
        print("The response of FilterApi->delete_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->delete_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_uuid** | **str**|  | 

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
**200** | Filter deleted successfully |  -  |
**404** | Filter not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter**
> ShowResponse get_filter(filter_uuid)

Fetch a specific saved filter

Retrieves details of a saved filter by its UUID.

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
    api_instance = caraer_client.FilterApi(api_client)
    filter_uuid = 'filter_uuid_example' # str | 

    try:
        # Fetch a specific saved filter
        api_response = api_instance.get_filter(filter_uuid)
        print("The response of FilterApi->get_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->get_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_uuid** | **str**|  | 

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
**200** | Filter retrieved successfully |  -  |
**404** | Filter not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters**
> PaginationResponse get_filters(object_uuid, body)

Fetch paginated saved filters

Fetches a paginated list of saved filters. The request body should contain pagination details such as limit, page, filters, and sort.

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
    api_instance = caraer_client.FilterApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    body = None # object | Pagination request details

    try:
        # Fetch paginated saved filters
        api_response = api_instance.get_filters(object_uuid, body)
        print("The response of FilterApi->get_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->get_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **body** | **object**| Pagination request details | 

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
**200** | Filters fetched successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filter**
> UpdateResponse update_filter(filter_uuid, saved_filter_dto)

Update an existing saved filter

Updates an existing saved filter identified by its UUID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.saved_filter_dto import SavedFilterDTO
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
    api_instance = caraer_client.FilterApi(api_client)
    filter_uuid = 'filter_uuid_example' # str | 
    saved_filter_dto = caraer_client.SavedFilterDTO() # SavedFilterDTO | Updated saved filter details

    try:
        # Update an existing saved filter
        api_response = api_instance.update_filter(filter_uuid, saved_filter_dto)
        print("The response of FilterApi->update_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->update_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_uuid** | **str**|  | 
 **saved_filter_dto** | [**SavedFilterDTO**](SavedFilterDTO.md)| Updated saved filter details | 

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
**200** | Filter updated successfully |  -  |
**400** | Invalid input data |  -  |
**404** | Filter not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

