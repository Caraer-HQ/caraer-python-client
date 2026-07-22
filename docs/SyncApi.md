# caraer_client.SyncApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync**](SyncApi.md#create_sync) | **POST** /api/v2/sync/ | Create a sync
[**delete_sync**](SyncApi.md#delete_sync) | **DELETE** /api/v2/sync/{uuid} | Delete a sync
[**get_sync**](SyncApi.md#get_sync) | **GET** /api/v2/sync/{uuid} | Get a sync
[**get_syncs**](SyncApi.md#get_syncs) | **POST** /api/v2/sync/index | Fetch paginated syncs
[**restore_sync**](SyncApi.md#restore_sync) | **POST** /api/v2/sync/{uuid}/restore | Restore a deleted sync
[**update_sync**](SyncApi.md#update_sync) | **PUT** /api/v2/sync/{uuid} | Update a sync


# **create_sync**
> CreateResponse create_sync(sync_dto)

Create a sync

Creates a new sync. Returns a CreateResponse containing the created sync details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.sync_dto import SyncDTO
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
    api_instance = caraer_client.SyncApi(api_client)
    sync_dto = caraer_client.SyncDTO() # SyncDTO | Sync data

    try:
        # Create a sync
        api_response = api_instance.create_sync(sync_dto)
        print("The response of SyncApi->create_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->create_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_dto** | [**SyncDTO**](SyncDTO.md)| Sync data | 

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
**200** | Sync created successfully |  -  |
**400** | Invalid sync data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sync**
> DeleteResponse delete_sync(uuid, sync_dto)

Delete a sync

Deletes an existing sync. Returns a DeleteResponse containing the deleted sync details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.delete_response import DeleteResponse
from caraer_client.models.sync_dto import SyncDTO
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
    api_instance = caraer_client.SyncApi(api_client)
    uuid = 'uuid_example' # str | 
    sync_dto = caraer_client.SyncDTO() # SyncDTO | Sync data

    try:
        # Delete a sync
        api_response = api_instance.delete_sync(uuid, sync_dto)
        print("The response of SyncApi->delete_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->delete_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **sync_dto** | [**SyncDTO**](SyncDTO.md)| Sync data | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync deleted successfully |  -  |
**400** | Invalid sync data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync**
> SyncDTO get_sync(uuid, sync_dto)

Get a sync

Retrieves a sync by its UUID. Returns a SyncDTO containing the sync details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.sync_dto import SyncDTO
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
    api_instance = caraer_client.SyncApi(api_client)
    uuid = 'uuid_example' # str | 
    sync_dto = caraer_client.SyncDTO() # SyncDTO | Sync data

    try:
        # Get a sync
        api_response = api_instance.get_sync(uuid, sync_dto)
        print("The response of SyncApi->get_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->get_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **sync_dto** | [**SyncDTO**](SyncDTO.md)| Sync data | 

### Return type

[**SyncDTO**](SyncDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync fetched successfully |  -  |
**400** | Invalid sync data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syncs**
> PaginationResponse get_syncs(body)

Fetch paginated syncs

Retrieves a paginated list of syncs. Returns a PaginationResponse containing SyncDTO objects based on the provided pagination criteria.

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
    api_instance = caraer_client.SyncApi(api_client)
    body = None # object | Pagination request for syncs

    try:
        # Fetch paginated syncs
        api_response = api_instance.get_syncs(body)
        print("The response of SyncApi->get_syncs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->get_syncs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Pagination request for syncs | 

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
**200** | Syncs fetched successfully |  -  |
**400** | Invalid pagination request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_sync**
> RestoreResponse restore_sync(uuid)

Restore a deleted sync

Restores a previously deleted sync by its UUID. Returns a RestoreResponse containing the restored sync details.

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
    api_instance = caraer_client.SyncApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Restore a deleted sync
        api_response = api_instance.restore_sync(uuid)
        print("The response of SyncApi->restore_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->restore_sync: %s\n" % e)
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
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync restored successfully |  -  |
**404** | Sync not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync**
> UpdateResponse update_sync(uuid, sync_dto)

Update a sync

Updates an existing sync. Returns a UpdateResponse containing the updated sync details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.sync_dto import SyncDTO
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
    api_instance = caraer_client.SyncApi(api_client)
    uuid = 'uuid_example' # str | 
    sync_dto = caraer_client.SyncDTO() # SyncDTO | Sync data

    try:
        # Update a sync
        api_response = api_instance.update_sync(uuid, sync_dto)
        print("The response of SyncApi->update_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->update_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **sync_dto** | [**SyncDTO**](SyncDTO.md)| Sync data | 

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
**200** | Sync updated successfully |  -  |
**400** | Invalid sync data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

