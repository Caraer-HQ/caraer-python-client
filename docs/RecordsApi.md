# caraer_client.RecordsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](RecordsApi.md#create) | **POST** /api/v2/records/{objectName} | Create a new record
[**create_or_update**](RecordsApi.md#create_or_update) | **POST** /api/v2/records/{objectName}/createOrUpdate | Create or update a record
[**create_relation**](RecordsApi.md#create_relation) | **POST** /api/v2/records/relations/{fromUuid}/{relationName}/{toUuid} | Create a relation between records
[**delete**](RecordsApi.md#delete) | **DELETE** /api/v2/records/{uuid} | Delete a record
[**delete_relation**](RecordsApi.md#delete_relation) | **DELETE** /api/v2/records/relations/{fromUuid}/{relationName}/{toUuid} | Delete a relation between records
[**index**](RecordsApi.md#index) | **POST** /api/v2/records/index | Fetch paginated records
[**index_flow**](RecordsApi.md#index_flow) | **POST** /api/v2/records/index/flow | Fetch records for flow view
[**index_page**](RecordsApi.md#index_page) | **POST** /api/v2/records/index/page | Fetch records for page view
[**index_table**](RecordsApi.md#index_table) | **POST** /api/v2/records/index/table | Fetch records for table view
[**morph**](RecordsApi.md#morph) | **POST** /api/v2/records/{uuid}/morph | Morph a record
[**preview**](RecordsApi.md#preview) | **GET** /api/v2/records/{uuid}/previews/{name} | Get record preview
[**restore**](RecordsApi.md#restore) | **POST** /api/v2/records/{uuid}/restore | Restore a deleted record
[**search**](RecordsApi.md#search) | **POST** /api/v2/records/search | Search records
[**show1**](RecordsApi.md#show1) | **GET** /api/v2/records/{uuid} | Get record details
[**update**](RecordsApi.md#update) | **PUT** /api/v2/records/{objectName}/{uuid} | Update a record


# **create**
> CreateResponse create(object_name, record_dto, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)

Create a new record

Creates a new record for the specified object using the provided RecordDTO data. Returns a CreateResponse with the newly created record. Validation: Record properties are validated according to the property rules defined for the object. Each property may have validation rules such as required, type constraints, character limits, uniqueness, etc.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.record_dto import RecordDTO
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
    api_instance = caraer_client.RecordsApi(api_client)
    object_name = 'object_name_example' # str | 
    record_dto = caraer_client.RecordDTO() # RecordDTO | Record data to create
    parse = False # bool | If 'true', parses the created record to human-readable values before returning. (optional) (default to False)
    ignore_errors = False # bool | If 'true', allows the creation to proceed while ignoring certain non-critical validation errors, when supported. (optional) (default to False)
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')

    try:
        # Create a new record
        api_response = api_instance.create(object_name, record_dto, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)
        print("The response of RecordsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **record_dto** | [**RecordDTO**](RecordDTO.md)| Record data to create | 
 **parse** | **bool**| If &#39;true&#39;, parses the created record to human-readable values before returning. | [optional] [default to False]
 **ignore_errors** | **bool**| If &#39;true&#39;, allows the creation to proceed while ignoring certain non-critical validation errors, when supported. | [optional] [default to False]
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]

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
**201** | Record created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update**
> create_or_update(object_name, record_dto, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)

Create or update a record

Creates a new record or updates an existing one based on uniqueness criteria for the given object. If a matching record exists, it is updated; otherwise, a new record is created. Returns a CreateResponse or UpdateResponse with the record details. Validation: Record properties are validated according to the property rules defined for the object. Each property may have validation rules such as required, type constraints, character limits, uniqueness, etc.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.record_dto import RecordDTO
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
    api_instance = caraer_client.RecordsApi(api_client)
    object_name = 'object_name_example' # str | 
    record_dto = caraer_client.RecordDTO() # RecordDTO | Record data to create or update
    parse = False # bool |  (optional) (default to False)
    ignore_errors = False # bool |  (optional) (default to False)
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')

    try:
        # Create or update a record
        api_instance.create_or_update(object_name, record_dto, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)
    except Exception as e:
        print("Exception when calling RecordsApi->create_or_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **record_dto** | [**RecordDTO**](RecordDTO.md)| Record data to create or update | 
 **parse** | **bool**|  | [optional] [default to False]
 **ignore_errors** | **bool**|  | [optional] [default to False]
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Record updated successfully |  -  |
**201** | Record created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_relation**
> SuccessResponse create_relation(from_uuid, relation_name, to_uuid, primary=primary)

Create a relation between records

Creates a relation between two records identified by their UUIDs using the provided relation name.

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
    api_instance = caraer_client.RecordsApi(api_client)
    from_uuid = 'from_uuid_example' # str | 
    relation_name = 'relation_name_example' # str | 
    to_uuid = 'to_uuid_example' # str | 
    primary = None # object | When 'true', marks the created relation as primary. Defaults to 'false'. (optional)

    try:
        # Create a relation between records
        api_response = api_instance.create_relation(from_uuid, relation_name, to_uuid, primary=primary)
        print("The response of RecordsApi->create_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->create_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_uuid** | **str**|  | 
 **relation_name** | **str**|  | 
 **to_uuid** | **str**|  | 
 **primary** | [**object**](.md)| When &#39;true&#39;, marks the created relation as primary. Defaults to &#39;false&#39;. | [optional] 

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
**200** | Relation created successfully |  -  |
**404** | One or more entities not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SuccessResponse delete(uuid, mode=mode)

Delete a record

Deletes a record specified by its UUID.

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
    api_instance = caraer_client.RecordsApi(api_client)
    uuid = 'uuid_example' # str | 
    mode = 'archive' # str | Controls how the record is removed. Allowed values: 'archive' (soft delete, keep all data), 'anonymize' (remove data but keep relationships), 'delete' (hard delete). Defaults to 'archive'. (optional) (default to 'archive')

    try:
        # Delete a record
        api_response = api_instance.delete(uuid, mode=mode)
        print("The response of RecordsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **mode** | **str**| Controls how the record is removed. Allowed values: &#39;archive&#39; (soft delete, keep all data), &#39;anonymize&#39; (remove data but keep relationships), &#39;delete&#39; (hard delete). Defaults to &#39;archive&#39;. | [optional] [default to &#39;archive&#39;]

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
**200** | Record deleted successfully |  -  |
**404** | Record not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relation**
> SuccessResponse delete_relation(from_uuid, relation_name, to_uuid)

Delete a relation between records

Deletes a relation between two records identified by their UUIDs and the relation name.

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
    api_instance = caraer_client.RecordsApi(api_client)
    from_uuid = 'from_uuid_example' # str | 
    relation_name = 'relation_name_example' # str | 
    to_uuid = 'to_uuid_example' # str | 

    try:
        # Delete a relation between records
        api_response = api_instance.delete_relation(from_uuid, relation_name, to_uuid)
        print("The response of RecordsApi->delete_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->delete_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_uuid** | **str**|  | 
 **relation_name** | **str**|  | 
 **to_uuid** | **str**|  | 

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
**200** | Relation deleted successfully |  -  |
**404** | One or more entities not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index**
> PaginationResponse index(body, parse=parse, archived=archived, related_record_uuid=related_record_uuid, record_return_format=record_return_format)

Fetch paginated records

Retrieves a paginated list of records. If a preview type is specified in the request, returns records formatted for preview; otherwise, returns full record details.

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
    api_instance = caraer_client.RecordsApi(api_client)
    body = 'body_example' # str | Pagination request for records
    parse = True # bool | If set to 'true', records are parsed to human-readable values (for example, unix timestamps are formatted as dates). (optional)
    archived = False # bool | When 'true', archived records are returned instead of active records. Defaults to 'false'. (optional) (default to False)
    related_record_uuid = 'related_record_uuid_example' # str | UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. (optional)
    record_return_format = 'LEGACY' # str | Format of the records to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')

    try:
        # Fetch paginated records
        api_response = api_instance.index(body, parse=parse, archived=archived, related_record_uuid=related_record_uuid, record_return_format=record_return_format)
        print("The response of RecordsApi->index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Pagination request for records | 
 **parse** | **bool**| If set to &#39;true&#39;, records are parsed to human-readable values (for example, unix timestamps are formatted as dates). | [optional] 
 **archived** | **bool**| When &#39;true&#39;, archived records are returned instead of active records. Defaults to &#39;false&#39;. | [optional] [default to False]
 **related_record_uuid** | **str**| UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. | [optional] 
 **record_return_format** | **str**| Format of the records to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]

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
**200** | Records fetched successfully |  -  |
**400** | Invalid pagination request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_flow**
> SuccessResponse index_flow(body, related_record_uuid=related_record_uuid, parse=parse)

Fetch records for flow view

Retrieves a list of records formatted for flow view based on a specific property. If the property is not provided in the request, defaults to the 'status' property of the main object. Returns a SuccessResponse containing the flow records.

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
    api_instance = caraer_client.RecordsApi(api_client)
    body = 'body_example' # str | Pagination request for flow view
    related_record_uuid = 'related_record_uuid_example' # str | UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. (optional)
    parse = True # bool | Whether to parse the record before returning it. (optional)

    try:
        # Fetch records for flow view
        api_response = api_instance.index_flow(body, related_record_uuid=related_record_uuid, parse=parse)
        print("The response of RecordsApi->index_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->index_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Pagination request for flow view | 
 **related_record_uuid** | **str**| UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. | [optional] 
 **parse** | **bool**| Whether to parse the record before returning it. | [optional] 

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
**200** | Records for flow view fetched successfully |  -  |
**400** | Required property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_page**
> PaginationResponse index_page(body, environment=environment, related_record_uuid=related_record_uuid, fields=fields, published_only=published_only, exclude_template_related=exclude_template_related)

Fetch records for page view

Retrieves a paginated list of webpages for page view. The search query is temporarily removed from the pagination request and passed separately. Returns a PaginationResponse containing WebpageDTO objects.

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
    api_instance = caraer_client.RecordsApi(api_client)
    body = 'body_example' # str | Pagination request for page view
    environment = 'staging' # str | Target environment for resolving webpages (for example 'staging' or 'production'). Defaults to 'staging'. (optional) (default to 'staging')
    related_record_uuid = 'related_record_uuid_example' # str | UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. (optional)
    fields = 'fields_example' # str | Comma-separated WebpageDTO fields to return (for example: uuid,title). When omitted, the full WebpageDTO is returned. (optional)
    published_only = False # bool | When true, only returns pages published in the selected environment. (optional) (default to False)
    exclude_template_related = False # bool | When true, excludes pages whose options mark them as related to a template. (optional) (default to False)

    try:
        # Fetch records for page view
        api_response = api_instance.index_page(body, environment=environment, related_record_uuid=related_record_uuid, fields=fields, published_only=published_only, exclude_template_related=exclude_template_related)
        print("The response of RecordsApi->index_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->index_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Pagination request for page view | 
 **environment** | **str**| Target environment for resolving webpages (for example &#39;staging&#39; or &#39;production&#39;). Defaults to &#39;staging&#39;. | [optional] [default to &#39;staging&#39;]
 **related_record_uuid** | **str**| UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. | [optional] 
 **fields** | **str**| Comma-separated WebpageDTO fields to return (for example: uuid,title). When omitted, the full WebpageDTO is returned. | [optional] 
 **published_only** | **bool**| When true, only returns pages published in the selected environment. | [optional] [default to False]
 **exclude_template_related** | **bool**| When true, excludes pages whose options mark them as related to a template. | [optional] [default to False]

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
**200** | Webpages fetched successfully |  -  |
**400** | Invalid pagination request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_table**
> PaginationResponse index_table(body, related_record_uuid=related_record_uuid)

Fetch records for table view

Retrieves records formatted for table display. Returns a PaginationResponse containing records formatted for table view.

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
    api_instance = caraer_client.RecordsApi(api_client)
    body = 'body_example' # str | Pagination request for table view
    related_record_uuid = 'related_record_uuid_example' # str | UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. (optional)

    try:
        # Fetch records for table view
        api_response = api_instance.index_table(body, related_record_uuid=related_record_uuid)
        print("The response of RecordsApi->index_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->index_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Pagination request for table view | 
 **related_record_uuid** | **str**| UUID of a record used for relation-aware filtering. If supplied and the request body contains a filter, that filter will be smartened based on this related record. If no filter is supplied, a default filter will be applied that returns all records related in any way (any relation) to this record. | [optional] 

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
**200** | Records for table view fetched successfully |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **morph**
> SuccessResponse morph(uuid, morph_record_request, record_return_format=record_return_format, parse=parse)

Morph a record

Morphs a record identified by its UUID to one or more objects. You can use this to move a record or add it to another object so it'll be visible in the new object.Returns a SuccessResponse confirming that the record has been morphed.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.morph_record_request import MorphRecordRequest
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
    api_instance = caraer_client.RecordsApi(api_client)
    uuid = 'uuid_example' # str | 
    morph_record_request = caraer_client.MorphRecordRequest() # MorphRecordRequest | 
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')
    parse = True # bool | Whether to parse the record before returning it. (optional)

    try:
        # Morph a record
        api_response = api_instance.morph(uuid, morph_record_request, record_return_format=record_return_format, parse=parse)
        print("The response of RecordsApi->morph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->morph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **morph_record_request** | [**MorphRecordRequest**](MorphRecordRequest.md)|  | 
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]
 **parse** | **bool**| Whether to parse the record before returning it. | [optional] 

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
**200** | Record morphed successfully |  -  |
**404** | Record not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview**
> ShowResponse preview(uuid, name, object=object, parse=parse)

Get record preview

Retrieves a preview for a record specified by its UUID and preview name. Returns a ShowResponse containing the preview data.

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
    api_instance = caraer_client.RecordsApi(api_client)
    uuid = 'uuid_example' # str | 
    name = 'name_example' # str | 
    object = 'object_example' # str | Optional object name used to resolve the record before building the preview. (optional)
    parse = True # bool | Whether to parse the record before returning it. (optional)

    try:
        # Get record preview
        api_response = api_instance.preview(uuid, name, object=object, parse=parse)
        print("The response of RecordsApi->preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **name** | **str**|  | 
 **object** | **str**| Optional object name used to resolve the record before building the preview. | [optional] 
 **parse** | **bool**| Whether to parse the record before returning it. | [optional] 

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
**200** | Preview retrieved successfully |  -  |
**404** | Record or preview not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore**
> SuccessResponse restore(uuid)

Restore a deleted record

Restores a soft-deleted record identified by its UUID. Returns a SuccessResponse confirming that the record has been restored.

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
    api_instance = caraer_client.RecordsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Restore a deleted record
        api_response = api_instance.restore(uuid)
        print("The response of RecordsApi->restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->restore: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Record restored successfully |  -  |
**404** | Record not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> PaginationResponse search(body, archived=archived, parse=parse, record_return_format=record_return_format)

Search records

Performs a search for records based on the specified criteria in the request body. Returns a PaginationResponse containing matching records.

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
    api_instance = caraer_client.RecordsApi(api_client)
    body = 'body_example' # str | Search criteria
    archived = False # bool | When set to 'true', includes soft-deleted records in the search results. (optional) (default to False)
    parse = False # bool | If 'true', parses returned records to human-readable values. (optional) (default to False)
    record_return_format = 'LEGACY' # str | Format of the records to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')

    try:
        # Search records
        api_response = api_instance.search(body, archived=archived, parse=parse, record_return_format=record_return_format)
        print("The response of RecordsApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Search criteria | 
 **archived** | **bool**| When set to &#39;true&#39;, includes soft-deleted records in the search results. | [optional] [default to False]
 **parse** | **bool**| If &#39;true&#39;, parses returned records to human-readable values. | [optional] [default to False]
 **record_return_format** | **str**| Format of the records to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]

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
**200** | Search completed successfully |  -  |
**400** | Invalid search parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show1**
> ShowResponse show1(uuid, object=object, record_return_format=record_return_format, parse=parse, fields=fields)

Get record details

Retrieves detailed information about a record by its UUID. Returns a ShowResponse containing the record details.

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
    api_instance = caraer_client.RecordsApi(api_client)
    uuid = 'uuid_example' # str | 
    object = 'object_example' # str | Optional object name to resolve the record in a specific object context. (optional)
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')
    parse = True # bool | Whether to parse the record before returning it. (optional)
    fields = 'fields_example' # str | Comma-separated property names to include (for example: name,status). When omitted, all properties are returned. (optional)

    try:
        # Get record details
        api_response = api_instance.show1(uuid, object=object, record_return_format=record_return_format, parse=parse, fields=fields)
        print("The response of RecordsApi->show1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->show1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **object** | **str**| Optional object name to resolve the record in a specific object context. | [optional] 
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]
 **parse** | **bool**| Whether to parse the record before returning it. | [optional] 
 **fields** | **str**| Comma-separated property names to include (for example: name,status). When omitted, all properties are returned. | [optional] 

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
**200** | Record retrieved successfully |  -  |
**404** | Record not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> UpdateResponse update(uuid, object_name, record_dto, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)

Update a record

Updates a record's details identified by its UUID. The record data is provided as a RecordDTO. Returns an UpdateResponse with the updated record. Validation: Record properties are validated according to the property rules defined for the object. Each property may have validation rules such as required, type constraints, character limits, uniqueness, etc.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.record_dto import RecordDTO
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
    api_instance = caraer_client.RecordsApi(api_client)
    uuid = 'uuid_example' # str | 
    object_name = 'object_name_example' # str | 
    record_dto = caraer_client.RecordDTO() # RecordDTO | Record data to update
    parse = False # bool | If 'true', parses the updated record to human-readable values before returning. (optional) (default to False)
    ignore_errors = False # bool | If 'true', allows the update to proceed while ignoring certain non-critical validation errors, when supported. (optional) (default to False)
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')

    try:
        # Update a record
        api_response = api_instance.update(uuid, object_name, record_dto, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)
        print("The response of RecordsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **object_name** | **str**|  | 
 **record_dto** | [**RecordDTO**](RecordDTO.md)| Record data to update | 
 **parse** | **bool**| If &#39;true&#39;, parses the updated record to human-readable values before returning. | [optional] [default to False]
 **ignore_errors** | **bool**| If &#39;true&#39;, allows the update to proceed while ignoring certain non-critical validation errors, when supported. | [optional] [default to False]
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]

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
**200** | Record updated successfully |  -  |
**400** | Invalid input data |  -  |
**404** | Record not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

