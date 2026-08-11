# caraer_client.RecordsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate**](RecordsApi.md#aggregate) | **POST** /api/v2/records/aggregate | Aggregate records for analytics charts
[**aggregate_batch**](RecordsApi.md#aggregate_batch) | **POST** /api/v2/records/aggregate/batch | Batch aggregate records for analytics dashboards
[**bulk_delete**](RecordsApi.md#bulk_delete) | **POST** /api/v2/records/{objectName}/bulk-delete | Bulk delete records
[**bulk_edit**](RecordsApi.md#bulk_edit) | **PUT** /api/v2/records/{objectName}/bulk | Bulk create or update records
[**create**](RecordsApi.md#create) | **POST** /api/v2/records/{objectName} | Create a new record
[**create_or_update**](RecordsApi.md#create_or_update) | **POST** /api/v2/records/{objectName}/createOrUpdate | Create or update a record
[**create_relation**](RecordsApi.md#create_relation) | **POST** /api/v2/records/relations/{fromUuid}/{relationName}/{toUuid} | Create a relation between records
[**delete**](RecordsApi.md#delete) | **DELETE** /api/v2/records/{uuid} | Delete a record
[**delete_relation**](RecordsApi.md#delete_relation) | **DELETE** /api/v2/records/relations/{fromUuid}/{relationName}/{toUuid} | Delete a relation between records
[**extend**](RecordsApi.md#extend) | **POST** /api/v2/records/{uuid}/extend | Extend a record
[**index**](RecordsApi.md#index) | **POST** /api/v2/records/index | Fetch paginated records
[**index_flow**](RecordsApi.md#index_flow) | **POST** /api/v2/records/index/flow | Fetch records for flow view
[**index_page**](RecordsApi.md#index_page) | **POST** /api/v2/records/index/page | Fetch records for page view
[**index_table**](RecordsApi.md#index_table) | **POST** /api/v2/records/index/table | Fetch records for table view
[**preview**](RecordsApi.md#preview) | **GET** /api/v2/records/{uuid}/previews/{name} | Get record preview
[**query**](RecordsApi.md#query) | **POST** /api/v2/records/query | Advanced graph-aware record query
[**restore**](RecordsApi.md#restore) | **POST** /api/v2/records/{uuid}/restore | Restore a deleted record
[**search**](RecordsApi.md#search) | **POST** /api/v2/records/search | Search records
[**search_cross_object**](RecordsApi.md#search_cross_object) | **POST** /api/v2/records/search/cross-object | Search records across objects
[**show**](RecordsApi.md#show) | **GET** /api/v2/records/{uuid} | Get record details
[**show_by_object**](RecordsApi.md#show_by_object) | **GET** /api/v2/records/{objectName}/{uuid} | Get record details by object
[**suggest_analytics_widgets**](RecordsApi.md#suggest_analytics_widgets) | **POST** /api/v2/records/analytics/suggest-widgets | Suggest analytics widgets with AI
[**update**](RecordsApi.md#update) | **PUT** /api/v2/records/{objectName}/{uuid} | Update a record
[**update_by_uuid**](RecordsApi.md#update_by_uuid) | **PUT** /api/v2/records/{uuid} | Update a record by UUID
[**update_relation_edge**](RecordsApi.md#update_relation_edge) | **PATCH** /api/v2/records/relations/{fromUuid}/{relationName}/{toUuid} | Update relation edge properties


# **aggregate**
> SuccessResponse aggregate(aggregate_request)

Aggregate records for analytics charts

Groups Neo4j records by property or time bucket and returns series points with optional drilldown filters.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.aggregate_request import AggregateRequest
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
    aggregate_request = caraer_client.AggregateRequest() # AggregateRequest | 

    try:
        # Aggregate records for analytics charts
        api_response = api_instance.aggregate(aggregate_request)
        print("The response of RecordsApi->aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_request** | [**AggregateRequest**](AggregateRequest.md)|  | 

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
**200** | Aggregation completed |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_batch**
> SuccessResponse aggregate_batch(aggregate_batch_request)

Batch aggregate records for analytics dashboards

Runs multiple aggregation requests for dashboard widgets.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.aggregate_batch_request import AggregateBatchRequest
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
    aggregate_batch_request = caraer_client.AggregateBatchRequest() # AggregateBatchRequest | 

    try:
        # Batch aggregate records for analytics dashboards
        api_response = api_instance.aggregate_batch(aggregate_batch_request)
        print("The response of RecordsApi->aggregate_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->aggregate_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregate_batch_request** | [**AggregateBatchRequest**](AggregateBatchRequest.md)|  | 

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
**200** | Batch aggregation completed |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete**
> BulkDeleteRecordsResponse bulk_delete(object_name, bulk_delete_records_request)

Bulk delete records

Archives, anonymizes, or permanently deletes multiple records in one request. Returns HTTP 200 when every item succeeds. Returns HTTP 200 with per-record errors when one or more items fail; successful items are still applied and listed in data.uuids.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.bulk_delete_records_request import BulkDeleteRecordsRequest
from caraer_client.models.bulk_delete_records_response import BulkDeleteRecordsResponse
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
    bulk_delete_records_request = caraer_client.BulkDeleteRecordsRequest() # BulkDeleteRecordsRequest | 

    try:
        # Bulk delete records
        api_response = api_instance.bulk_delete(object_name, bulk_delete_records_request)
        print("The response of RecordsApi->bulk_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->bulk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **bulk_delete_records_request** | [**BulkDeleteRecordsRequest**](BulkDeleteRecordsRequest.md)|  | 

### Return type

[**BulkDeleteRecordsResponse**](BulkDeleteRecordsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bulk delete completed (possibly with per-record errors) |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_edit**
> BulkEditRecordsResponse bulk_edit(object_name, bulk_edit_records_request, ignore_errors=ignore_errors)

Bulk create or update records

Creates or updates multiple records in one request. Returns HTTP 201 when every item succeeds (no per-record errors). Returns HTTP 200 when one or more items fail validation; successful items are still persisted and listed in data.records, with failures in errors.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.bulk_edit_records_request import BulkEditRecordsRequest
from caraer_client.models.bulk_edit_records_response import BulkEditRecordsResponse
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
    bulk_edit_records_request = caraer_client.BulkEditRecordsRequest() # BulkEditRecordsRequest | 
    ignore_errors = False # bool | If 'true', allows each save to proceed while ignoring certain non-critical validation errors, when supported. (optional) (default to False)

    try:
        # Bulk create or update records
        api_response = api_instance.bulk_edit(object_name, bulk_edit_records_request, ignore_errors=ignore_errors)
        print("The response of RecordsApi->bulk_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->bulk_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **bulk_edit_records_request** | [**BulkEditRecordsRequest**](BulkEditRecordsRequest.md)|  | 
 **ignore_errors** | **bool**| If &#39;true&#39;, allows each save to proceed while ignoring certain non-critical validation errors, when supported. | [optional] [default to False]

### Return type

[**BulkEditRecordsResponse**](BulkEditRecordsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | All records saved successfully |  -  |
**200** | Partial success with per-record validation errors |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)
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
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 
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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)
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
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 
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
> SuccessResponse create_relation(from_uuid, relation_name, to_uuid, primary=primary, relation_edge_request_dto=relation_edge_request_dto)

Create a relation between records

Creates a relation between two records identified by their UUIDs using the provided relation name.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.relation_edge_request_dto import RelationEdgeRequestDTO
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
    relation_edge_request_dto = caraer_client.RelationEdgeRequestDTO() # RelationEdgeRequestDTO |  (optional)

    try:
        # Create a relation between records
        api_response = api_instance.create_relation(from_uuid, relation_name, to_uuid, primary=primary, relation_edge_request_dto=relation_edge_request_dto)
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
 **relation_edge_request_dto** | [**RelationEdgeRequestDTO**](RelationEdgeRequestDTO.md)|  | [optional] 

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

# **extend**
> SuccessResponse extend(uuid, extend_record_request, record_return_format=record_return_format, parse=parse)

Extend a record

Extends a record identified by its UUID to one or more objects. You can use this to move a record or add it to another object so it'll be visible in the new object.Returns a SuccessResponse confirming that the record has been extended.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.extend_record_request import ExtendRecordRequest
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
    extend_record_request = caraer_client.ExtendRecordRequest() # ExtendRecordRequest | 
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)

    try:
        # Extend a record
        api_response = api_instance.extend(uuid, extend_record_request, record_return_format=record_return_format, parse=parse)
        print("The response of RecordsApi->extend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->extend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **extend_record_request** | [**ExtendRecordRequest**](ExtendRecordRequest.md)|  | 
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 

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
**200** | Record extended successfully |  -  |
**404** | Record not found |  -  |
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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)
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
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 
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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)

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
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 

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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)

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
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 

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

# **query**
> AdvancedRecordQueryResponse query(advanced_record_query_request)

Advanced graph-aware record query

Executes a two-pass GraphRAG query using natural language or a declarative plan. Returns records with scores and graph evidence.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.advanced_record_query_request import AdvancedRecordQueryRequest
from caraer_client.models.advanced_record_query_response import AdvancedRecordQueryResponse
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
    advanced_record_query_request = caraer_client.AdvancedRecordQueryRequest() # AdvancedRecordQueryRequest | 

    try:
        # Advanced graph-aware record query
        api_response = api_instance.query(advanced_record_query_request)
        print("The response of RecordsApi->query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advanced_record_query_request** | [**AdvancedRecordQueryRequest**](AdvancedRecordQueryRequest.md)|  | 

### Return type

[**AdvancedRecordQueryResponse**](AdvancedRecordQueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query completed successfully |  -  |
**400** | Invalid query request |  -  |

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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)
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
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 
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

# **search_cross_object**
> PaginationResponse search_cross_object(cross_object_record_search_request, archived=archived, parse=parse)

Search records across objects

Searches records across multiple object types in one request. Use fromObjectUuid + relationName to limit to relation target objects (e.g. event attendees), or objectUuids for an explicit list, or omit both to search all company objects (capped). Returns preview-shaped results suitable for relation pickers.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.cross_object_record_search_request import CrossObjectRecordSearchRequest
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
    cross_object_record_search_request = caraer_client.CrossObjectRecordSearchRequest() # CrossObjectRecordSearchRequest | 
    archived = False # bool | When true, includes archived records. (optional) (default to False)
    parse = 'parse_example' # str | Parse property values for display. (optional)

    try:
        # Search records across objects
        api_response = api_instance.search_cross_object(cross_object_record_search_request, archived=archived, parse=parse)
        print("The response of RecordsApi->search_cross_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->search_cross_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_object_record_search_request** | [**CrossObjectRecordSearchRequest**](CrossObjectRecordSearchRequest.md)|  | 
 **archived** | **bool**| When true, includes archived records. | [optional] [default to False]
 **parse** | **str**| Parse property values for display. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ShowResponse show(uuid, object=object, record_return_format=record_return_format, parse=parse, fields=fields)

Get record details

Retrieves detailed information about a record by its UUID. Returns a ShowResponse containing the record details. Prefer GET /{objectName}/{uuid} when the object context is known.

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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)
    fields = 'fields_example' # str | Comma-separated property names to include (for example: name,status). When omitted, all properties are returned. (optional)

    try:
        # Get record details
        api_response = api_instance.show(uuid, object=object, record_return_format=record_return_format, parse=parse, fields=fields)
        print("The response of RecordsApi->show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **object** | **str**| Optional object name to resolve the record in a specific object context. | [optional] 
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 
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

# **show_by_object**
> ShowResponse show_by_object(object_name, uuid, record_return_format=record_return_format, parse=parse)

Get record details by object

Retrieves a record by object name and UUID. Same response as GET /{uuid}?object={objectName}.

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
    object_name = 'object_name_example' # str | 
    uuid = 'uuid_example' # str | 
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)

    try:
        # Get record details by object
        api_response = api_instance.show_by_object(object_name, uuid, record_return_format=record_return_format, parse=parse)
        print("The response of RecordsApi->show_by_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->show_by_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **uuid** | **str**|  | 
 **record_return_format** | **str**| Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. | [optional] [default to &#39;LEGACY&#39;]
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 

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

# **suggest_analytics_widgets**
> SuccessResponse suggest_analytics_widgets(suggest_analytics_widgets_request)

Suggest analytics widgets with AI

Uses structured OpenAI output plus schema validation to propose dashboard charts for an object. Returns an empty list when AI is unavailable.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response import SuccessResponse
from caraer_client.models.suggest_analytics_widgets_request import SuggestAnalyticsWidgetsRequest
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
    suggest_analytics_widgets_request = caraer_client.SuggestAnalyticsWidgetsRequest() # SuggestAnalyticsWidgetsRequest | 

    try:
        # Suggest analytics widgets with AI
        api_response = api_instance.suggest_analytics_widgets(suggest_analytics_widgets_request)
        print("The response of RecordsApi->suggest_analytics_widgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->suggest_analytics_widgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suggest_analytics_widgets_request** | [**SuggestAnalyticsWidgetsRequest**](SuggestAnalyticsWidgetsRequest.md)|  | 

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
**200** | Suggestions generated (may be empty) |  -  |
**400** | Invalid request |  -  |
**404** | Object not found |  -  |

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
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)
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
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 
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

# **update_by_uuid**
> UpdateResponse update_by_uuid(uuid, record_dto, object=object, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)

Update a record by UUID

Updates a record identified by UUID. Optional object query param resolves the object context (same as GET /{uuid}?object=...). When omitted, the record's current/primary object is used. Prefer PUT /{objectName}/{uuid} when the object context is known.

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
    record_dto = caraer_client.RecordDTO() # RecordDTO | 
    object = 'object_example' # str | Optional object name to resolve the record in a specific object context. (optional)
    parse = 'parse_example' # str | Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). (optional)
    ignore_errors = False # bool | If 'true', allows the update to proceed while ignoring certain non-critical validation errors, when supported. (optional) (default to False)
    record_return_format = 'LEGACY' # str | Format of the record to return. LEGACY, USER_FRIENDLY, EXPANDED. (optional) (default to 'LEGACY')

    try:
        # Update a record by UUID
        api_response = api_instance.update_by_uuid(uuid, record_dto, object=object, parse=parse, ignore_errors=ignore_errors, record_return_format=record_return_format)
        print("The response of RecordsApi->update_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->update_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **record_dto** | [**RecordDTO**](RecordDTO.md)|  | 
 **object** | **str**| Optional object name to resolve the record in a specific object context. | [optional] 
 **parse** | **str**| Value presentation mode: omit/false/db for raw stored values; true/human_readable for display strings; structured for rich JSON (e.g. PropertyOption arrays, related records). | [optional] 
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

# **update_relation_edge**
> SuccessResponse update_relation_edge(from_uuid, relation_name, to_uuid, relation_edge_request_dto)

Update relation edge properties

Patches values stored on an existing relation edge. Only keys present in edgeProperties are written; a null value clears a key.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.relation_edge_request_dto import RelationEdgeRequestDTO
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
    relation_edge_request_dto = caraer_client.RelationEdgeRequestDTO() # RelationEdgeRequestDTO | 

    try:
        # Update relation edge properties
        api_response = api_instance.update_relation_edge(from_uuid, relation_name, to_uuid, relation_edge_request_dto)
        print("The response of RecordsApi->update_relation_edge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->update_relation_edge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_uuid** | **str**|  | 
 **relation_name** | **str**|  | 
 **to_uuid** | **str**|  | 
 **relation_edge_request_dto** | [**RelationEdgeRequestDTO**](RelationEdgeRequestDTO.md)|  | 

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
**200** | Relation updated successfully |  -  |
**400** | Unknown or invalid edge property |  -  |
**404** | One or more entities not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

