# caraer_client.RelationsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection**](RelationsApi.md#add_connection) | **PUT** /api/v2/relations/{relationUuid}/connection/{from}/{to} | Add a connection to a relation
[**create_relation_or_update**](RelationsApi.md#create_relation_or_update) | **POST** /api/v2/relations/{objectUuid} | Create or update a relation
[**delete_connection**](RelationsApi.md#delete_connection) | **DELETE** /api/v2/relations/{relationUuid}/connection/{from}/{to} | Delete a connection from a relation
[**delete_relation1**](RelationsApi.md#delete_relation1) | **DELETE** /api/v2/relations/{relationUuid} | Delete a relation
[**get_relation**](RelationsApi.md#get_relation) | **GET** /api/v2/relations/{relationUuid} | Get relation details
[**get_relation_for_object**](RelationsApi.md#get_relation_for_object) | **GET** /api/v2/relations/{relationUuid}/{objectUuid} | Get relation details for a specific object
[**get_relations**](RelationsApi.md#get_relations) | **POST** /api/v2/relations/index | Fetch paginated relations
[**get_relations_between_objects**](RelationsApi.md#get_relations_between_objects) | **POST** /api/v2/relations/index/{fromObjectUuid}/{toObjectUuid} | Get all relations between two objects
[**get_relations_by_object**](RelationsApi.md#get_relations_by_object) | **POST** /api/v2/relations/index/{objectUuid} | Fetch relations for a specific object
[**permanently_delete_archived_relation**](RelationsApi.md#permanently_delete_archived_relation) | **DELETE** /api/v2/relations/{relationUuid}/permanent | Permanently delete archived relation
[**restore_relation**](RelationsApi.md#restore_relation) | **POST** /api/v2/relations/{relationUuid}/restore | Restore a deleted relation
[**update_indices**](RelationsApi.md#update_indices) | **PUT** /api/v2/relations/updateIndices | Update relation indices


# **add_connection**
> SuccessResponse add_connection(relation_uuid, var_from, to)

Add a connection to a relation

Creates a connection between two objects for a given relation. The 'from' and 'to' UUIDs identify the objects to connect.

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
    api_instance = caraer_client.RelationsApi(api_client)
    relation_uuid = 'relation_uuid_example' # str | 
    var_from = 'var_from_example' # str | 
    to = 'to_example' # str | 

    try:
        # Add a connection to a relation
        api_response = api_instance.add_connection(relation_uuid, var_from, to)
        print("The response of RelationsApi->add_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->add_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_uuid** | **str**|  | 
 **var_from** | **str**|  | 
 **to** | **str**|  | 

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
**200** | Connection created successfully |  -  |
**404** | One or more entities not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_relation_or_update**
> UpdateResponse create_relation_or_update(object_uuid, relation_dto)

Create or update a relation

Creates a new relation or updates an existing one for the specified object. If a relation with the same name exists, it is updated; otherwise, a new relation is created. Returns an UpdateResponse if updated or a CreateResponse if created.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.relation_dto import RelationDTO
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
    api_instance = caraer_client.RelationsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    relation_dto = caraer_client.RelationDTO() # RelationDTO | Relation data

    try:
        # Create or update a relation
        api_response = api_instance.create_relation_or_update(object_uuid, relation_dto)
        print("The response of RelationsApi->create_relation_or_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->create_relation_or_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **relation_dto** | [**RelationDTO**](RelationDTO.md)| Relation data | 

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
**200** | Relation updated successfully |  -  |
**201** | Relation created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> SuccessResponse delete_connection(relation_uuid, var_from, to)

Delete a connection from a relation

Deletes a connection between two objects for a given relation using the specified UUIDs.

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
    api_instance = caraer_client.RelationsApi(api_client)
    relation_uuid = 'relation_uuid_example' # str | 
    var_from = 'var_from_example' # str | 
    to = 'to_example' # str | 

    try:
        # Delete a connection from a relation
        api_response = api_instance.delete_connection(relation_uuid, var_from, to)
        print("The response of RelationsApi->delete_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->delete_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_uuid** | **str**|  | 
 **var_from** | **str**|  | 
 **to** | **str**|  | 

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
**200** | Connection deleted successfully |  -  |
**404** | One or more entities not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relation1**
> DeleteResponse delete_relation1(relation_uuid)

Delete a relation

Deletes a relation specified by its UUID. Returns a DeleteResponse with the deleted relation details.

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
    api_instance = caraer_client.RelationsApi(api_client)
    relation_uuid = 'relation_uuid_example' # str | 

    try:
        # Delete a relation
        api_response = api_instance.delete_relation1(relation_uuid)
        print("The response of RelationsApi->delete_relation1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->delete_relation1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_uuid** | **str**|  | 

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
**200** | Relation deleted successfully |  -  |
**404** | Relation not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation**
> ShowResponse get_relation(relation_uuid)

Get relation details

Retrieves the details of a relation by its UUID. Returns a ShowResponse containing a RelationDTO.

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
    api_instance = caraer_client.RelationsApi(api_client)
    relation_uuid = 'relation_uuid_example' # str | 

    try:
        # Get relation details
        api_response = api_instance.get_relation(relation_uuid)
        print("The response of RelationsApi->get_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->get_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_uuid** | **str**|  | 

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
**200** | Relation retrieved successfully |  -  |
**404** | Relation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_for_object**
> ShowResponse get_relation_for_object(relation_uuid, object_uuid)

Get relation details for a specific object

Retrieves a relation by its UUID and associates it with the specified object, returning a RelationDTO that includes details from the related object.

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
    api_instance = caraer_client.RelationsApi(api_client)
    relation_uuid = 'relation_uuid_example' # str | 
    object_uuid = 'object_uuid_example' # str | 

    try:
        # Get relation details for a specific object
        api_response = api_instance.get_relation_for_object(relation_uuid, object_uuid)
        print("The response of RelationsApi->get_relation_for_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->get_relation_for_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_uuid** | **str**|  | 
 **object_uuid** | **str**|  | 

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
**200** | Relation for object retrieved successfully |  -  |
**404** | Relation or object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relations**
> PaginationResponse get_relations(body)

Fetch paginated relations

Retrieves a paginated list of relations. Returns a PaginationResponse containing RelationDTO objects based on the provided pagination criteria.

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
    api_instance = caraer_client.RelationsApi(api_client)
    body = None # object | Pagination request for relations

    try:
        # Fetch paginated relations
        api_response = api_instance.get_relations(body)
        print("The response of RelationsApi->get_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->get_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Pagination request for relations | 

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
**200** | Relations fetched successfully |  -  |
**400** | Invalid pagination request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relations_between_objects**
> PaginationResponse get_relations_between_objects(from_object_uuid, to_object_uuid, body)

Get all relations between two objects

Retrieves all relations between two objects based on the provided object UUIDs.

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
    api_instance = caraer_client.RelationsApi(api_client)
    from_object_uuid = 'from_object_uuid_example' # str | 
    to_object_uuid = 'to_object_uuid_example' # str | 
    body = None # object | 

    try:
        # Get all relations between two objects
        api_response = api_instance.get_relations_between_objects(from_object_uuid, to_object_uuid, body)
        print("The response of RelationsApi->get_relations_between_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->get_relations_between_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_object_uuid** | **str**|  | 
 **to_object_uuid** | **str**|  | 
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
**200** | Relations retrieved successfully |  -  |
**404** | One or more objects not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relations_by_object**
> PaginationResponse get_relations_by_object(object_uuid, body)

Fetch relations for a specific object

Returns relation definitions where this object participates in the **schema** graph for that relation name: either as origin `(thisObject)-[:relationName]->(:Object)` or as target `(:Object)-[:relationName]->(thisObject)`. Unrelated relations (same name elsewhere, or no typed edge touching this object) are excluded. Uses the object’s `name` to filter; request path uses object UUID.

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
    api_instance = caraer_client.RelationsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    body = None # object | Pagination request for relations

    try:
        # Fetch relations for a specific object
        api_response = api_instance.get_relations_by_object(object_uuid, body)
        print("The response of RelationsApi->get_relations_by_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->get_relations_by_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **body** | **object**| Pagination request for relations | 

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
**200** | Relations fetched successfully |  -  |
**404** | Object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permanently_delete_archived_relation**
> DeleteResponse permanently_delete_archived_relation(relation_uuid)

Permanently delete archived relation

Hard-deletes a soft-deleted relation. Only relations with deletedAt set can be removed.

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
    api_instance = caraer_client.RelationsApi(api_client)
    relation_uuid = 'relation_uuid_example' # str | 

    try:
        # Permanently delete archived relation
        api_response = api_instance.permanently_delete_archived_relation(relation_uuid)
        print("The response of RelationsApi->permanently_delete_archived_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->permanently_delete_archived_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_uuid** | **str**|  | 

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
**200** | Relation permanently deleted |  -  |
**400** | Relation is not archived |  -  |
**404** | Relation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_relation**
> RestoreResponse restore_relation(relation_uuid)

Restore a deleted relation

Restores a previously deleted relation by its UUID. Returns a RestoreResponse with the restored relation details.

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
    api_instance = caraer_client.RelationsApi(api_client)
    relation_uuid = 'relation_uuid_example' # str | 

    try:
        # Restore a deleted relation
        api_response = api_instance.restore_relation(relation_uuid)
        print("The response of RelationsApi->restore_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->restore_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_uuid** | **str**|  | 

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
**200** | Relation restored successfully |  -  |
**404** | Relation not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_indices**
> SuccessResponse update_indices(body)

Update relation indices

Updates the indices for relations. The request body should contain a mapping of relation UUIDs to their new index values. Returns a SuccessResponse containing the updated relation objects.

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
    api_instance = caraer_client.RelationsApi(api_client)
    body = 'body_example' # str | Mapping of relation UUIDs to new index values

    try:
        # Update relation indices
        api_response = api_instance.update_indices(body)
        print("The response of RelationsApi->update_indices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationsApi->update_indices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Mapping of relation UUIDs to new index values | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indices updated successfully |  -  |
**400** | Invalid input provided |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

