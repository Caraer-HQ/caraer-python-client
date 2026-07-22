# caraer_client.PropertyApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_properties_to_object**](PropertyApi.md#copy_properties_to_object) | **POST** /api/v2/objects/{objectUuid}/properties/copy | Copy properties to object
[**create_property**](PropertyApi.md#create_property) | **POST** /api/v2/objects/{objectUuid}/properties/ | Create a new property
[**delete_property**](PropertyApi.md#delete_property) | **DELETE** /api/v2/objects/{objectUuid}/properties/{propertyUuid} | Delete a property
[**get_calculation_types**](PropertyApi.md#get_calculation_types) | **GET** /api/v2/objects/{objectUuid}/properties/calculation-types | Retrieve allowed calculation types per property type
[**get_formats**](PropertyApi.md#get_formats) | **GET** /api/v2/objects/{objectUuid}/properties/formats | Retrieve property formats
[**get_properties**](PropertyApi.md#get_properties) | **POST** /api/v2/objects/{objectUuid}/properties/index | Fetch paginated properties
[**get_property**](PropertyApi.md#get_property) | **GET** /api/v2/objects/{objectUuid}/properties/{propertyUuid} | Fetch a specific property
[**get_property_calculation_types**](PropertyApi.md#get_property_calculation_types) | **GET** /api/v2/objects/{objectUuid}/properties/{propertyUuid}/calculation-types | Retrieve allowed calculation types for a property
[**permanently_delete_archived_property**](PropertyApi.md#permanently_delete_archived_property) | **DELETE** /api/v2/objects/{objectUuid}/properties/{propertyUuid}/permanent | Permanently remove archived property
[**pin_property**](PropertyApi.md#pin_property) | **PUT** /api/v2/objects/{objectUuid}/properties/{propertyUuid}/pin | Pin a property
[**restore_property**](PropertyApi.md#restore_property) | **POST** /api/v2/objects/{objectUuid}/properties/{propertyUuid}/restore | Restore a soft-deleted property
[**unpin_property**](PropertyApi.md#unpin_property) | **DELETE** /api/v2/objects/{objectUuid}/properties/{propertyUuid}/pin | Unpin a property
[**update_indices2**](PropertyApi.md#update_indices2) | **PUT** /api/v2/objects/{objectUuid}/properties/updateIndices | Update property indices
[**update_property**](PropertyApi.md#update_property) | **PUT** /api/v2/objects/{objectUuid}/properties/{propertyUuid} | Update an existing property


# **copy_properties_to_object**
> SuccessResponse copy_properties_to_object(object_uuid, copy_properties_to_object_request)

Copy properties to object

Attaches existing properties from other objects to the target object in a single request. Archived links on the target object are restored. Properties already active on the target are rejected.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.copy_properties_to_object_request import CopyPropertiesToObjectRequest
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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    copy_properties_to_object_request = caraer_client.CopyPropertiesToObjectRequest() # CopyPropertiesToObjectRequest | 

    try:
        # Copy properties to object
        api_response = api_instance.copy_properties_to_object(object_uuid, copy_properties_to_object_request)
        print("The response of PropertyApi->copy_properties_to_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->copy_properties_to_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **copy_properties_to_object_request** | [**CopyPropertiesToObjectRequest**](CopyPropertiesToObjectRequest.md)|  | 

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
**200** | Properties copied successfully |  -  |
**400** | Invalid input data |  -  |
**404** | Object or property not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property**
> CreateResponse create_property(object_uuid, save_property_dto)

Create a new property

Creates a new property for a specific object using the provided property details. The SavePropertyDTO must include necessary details, and the object association is determined by the objectUuid path variable. Returns a CreateResponse containing the newly created property as a PropertyDTO. Validation rules: name (required, must be unique, must be lowercase, must match name pattern (lowercase letters, numbers, underscores)), label (required), description (maximum 255 characters), type (required, must be one of valid PropertyTypes, cannot be changed after creation), format (required, must be one of valid PropertyFormats, cannot be changed after creation), rules (required, must be an array of string).

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.save_property_dto import SavePropertyDTO
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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    save_property_dto = caraer_client.SavePropertyDTO() # SavePropertyDTO | Property details for creation

    try:
        # Create a new property
        api_response = api_instance.create_property(object_uuid, save_property_dto)
        print("The response of PropertyApi->create_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->create_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **save_property_dto** | [**SavePropertyDTO**](SavePropertyDTO.md)| Property details for creation | 

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
**201** | Property created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property**
> DeleteResponse delete_property(object_uuid, property_uuid)

Delete a property

Deletes a property from the specified object, identified by the property UUID. Returns a DeleteResponse containing the deleted property's details.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 

    try:
        # Delete a property
        api_response = api_instance.delete_property(object_uuid, property_uuid)
        print("The response of PropertyApi->delete_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->delete_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 

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
**200** | Property deleted successfully |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_types**
> PaginationResponse get_calculation_types(object_uuid)

Retrieve allowed calculation types per property type

Returns the calculation functions available for each property type (for example min/max on numbers).

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 

    try:
        # Retrieve allowed calculation types per property type
        api_response = api_instance.get_calculation_types(object_uuid)
        print("The response of PropertyApi->get_calculation_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->get_calculation_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 

### Return type

[**PaginationResponse**](PaginationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calculation types retrieved successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_formats**
> PaginationResponse get_formats(object_uuid)

Retrieve property formats

Fetches a sorted list of available property formats. The formats are retrieved from the PropertyFormats enum and converted to PropertyFormat instances.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 

    try:
        # Retrieve property formats
        api_response = api_instance.get_formats(object_uuid)
        print("The response of PropertyApi->get_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->get_formats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 

### Return type

[**PaginationResponse**](PaginationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Property formats retrieved successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> PaginationResponse get_properties(object_uuid, body)

Fetch paginated properties

Retrieves a paginated list of properties for a given object. Depending on the object UUID format, a Cypher query is constructed to filter properties belonging to that object. Returns a PaginationResponse containing PropertyDTO objects.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    body = None # object | Pagination details (limit, page, filters, sort, query)

    try:
        # Fetch paginated properties
        api_response = api_instance.get_properties(object_uuid, body)
        print("The response of PropertyApi->get_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->get_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **body** | **object**| Pagination details (limit, page, filters, sort, query) | 

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
**200** | Properties fetched successfully |  -  |
**400** | Invalid pagination request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property**
> ShowResponse get_property(object_uuid, property_uuid)

Fetch a specific property

Retrieves details of a property by its UUID and associates it with its parent object. Returns a ShowResponse containing a PropertyDTO object with complete property details.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 

    try:
        # Fetch a specific property
        api_response = api_instance.get_property(object_uuid, property_uuid)
        print("The response of PropertyApi->get_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->get_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 

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
**200** | Property retrieved successfully |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_calculation_types**
> SuccessResponse get_property_calculation_types(object_uuid, property_uuid)

Retrieve allowed calculation types for a property

Returns calculation functions supported for the property's type.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 

    try:
        # Retrieve allowed calculation types for a property
        api_response = api_instance.get_property_calculation_types(object_uuid, property_uuid)
        print("The response of PropertyApi->get_property_calculation_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->get_property_calculation_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 

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
**200** | Calculation types retrieved successfully |  -  |
**404** | Property or object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permanently_delete_archived_property**
> DeleteResponse permanently_delete_archived_property(object_uuid, property_uuid)

Permanently remove archived property

Deletes the soft-deleted HAS_PROPERTY link to this object. If the property is not linked to any other object, the property node is hard-deleted.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 

    try:
        # Permanently remove archived property
        api_response = api_instance.permanently_delete_archived_property(object_uuid, property_uuid)
        print("The response of PropertyApi->permanently_delete_archived_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->permanently_delete_archived_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 

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
**200** | Archived property permanently removed |  -  |
**400** | Property is not archived for this object |  -  |
**404** | Object or property not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_property**
> UpdateResponse pin_property(object_uuid, property_uuid)

Pin a property

Pins the specified property for the logged-in user. Pinned properties appear at the top of record create and update forms.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 

    try:
        # Pin a property
        api_response = api_instance.pin_property(object_uuid, property_uuid)
        print("The response of PropertyApi->pin_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->pin_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Property pinned successfully |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_property**
> RestoreResponse restore_property(object_uuid, property_uuid)

Restore a soft-deleted property

Restores a previously deleted property by propertyUuid for the specified objectUuid. Returns a RestoreResponse containing the restored property details.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 

    try:
        # Restore a soft-deleted property
        api_response = api_instance.restore_property(object_uuid, property_uuid)
        print("The response of PropertyApi->restore_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->restore_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 

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
**200** | Property restored successfully |  -  |
**404** | Property or Object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpin_property**
> UpdateResponse unpin_property(object_uuid, property_uuid)

Unpin a property

Removes the pin for the specified property for the logged-in user.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 

    try:
        # Unpin a property
        api_response = api_instance.unpin_property(object_uuid, property_uuid)
        print("The response of PropertyApi->unpin_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->unpin_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Property unpinned successfully |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_indices2**
> SuccessResponse update_indices2(object_uuid, body)

Update property indices

Updates the indices for properties of a specific object. The request body should contain a mapping between property UUIDs and their new index values. Returns a SuccessResponse containing a list of updated PropertyDTO objects.

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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    body = 'body_example' # str | Mapping of property UUIDs to new index values

    try:
        # Update property indices
        api_response = api_instance.update_indices2(object_uuid, body)
        print("The response of PropertyApi->update_indices2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_indices2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **body** | **str**| Mapping of property UUIDs to new index values | 

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

# **update_property**
> UpdateResponse update_property(object_uuid, property_uuid, save_property_dto)

Update an existing property

Updates the details of an existing property for a specific object. The property details are provided via SavePropertyDTO, and the property is identified by its UUID. Returns an UpdateResponse containing the updated property as a PropertyDTO. Validation rules: name (required, must be unique, must be lowercase, must match name pattern (lowercase letters, numbers, underscores), cannot be changed after creation), label (required), description (maximum 255 characters), type (required, must be one of valid PropertyTypes, cannot be changed after creation), format (required, must be one of valid PropertyFormats, cannot be changed after creation), rules (required, must be an array of string).

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.save_property_dto import SavePropertyDTO
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
    api_instance = caraer_client.PropertyApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    property_uuid = 'property_uuid_example' # str | 
    save_property_dto = caraer_client.SavePropertyDTO() # SavePropertyDTO | Updated property details

    try:
        # Update an existing property
        api_response = api_instance.update_property(object_uuid, property_uuid, save_property_dto)
        print("The response of PropertyApi->update_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyApi->update_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **property_uuid** | **str**|  | 
 **save_property_dto** | [**SavePropertyDTO**](SavePropertyDTO.md)| Updated property details | 

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
**200** | Property updated successfully |  -  |
**400** | Invalid input data |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

