# caraer_client.TraitsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trait**](TraitsApi.md#create_trait) | **POST** /api/v2/traits/{objectUuid}/{traitName} | Create or update a trait for an object
[**delete_trait**](TraitsApi.md#delete_trait) | **DELETE** /api/v2/traits/{objectUuid}/{traitName} | Delete a trait from an object
[**get_trait**](TraitsApi.md#get_trait) | **GET** /api/v2/traits/{objectUuid}/{traitName} | Fetch a specific trait for an object
[**get_traits**](TraitsApi.md#get_traits) | **GET** /api/v2/traits/{objectUuid} | Fetch all traits for an object


# **create_trait**
> CreateResponse create_trait(object_uuid, trait_name, body)

Create or update a trait for an object

Creates a new trait or updates an existing trait for the specified object. The trait name is provided in the URL, and trait details are supplied in the request body as a JSON map. If a trait with the specified name exists, it will be updated; otherwise, a new trait is created. Returns a CreateResponse containing the TraitDTO of the created or updated trait.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
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
    api_instance = caraer_client.TraitsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    trait_name = 'trait_name_example' # str | 
    body = 'body_example' # str | Trait details as a JSON map

    try:
        # Create or update a trait for an object
        api_response = api_instance.create_trait(object_uuid, trait_name, body)
        print("The response of TraitsApi->create_trait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TraitsApi->create_trait: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **trait_name** | **str**|  | 
 **body** | **str**| Trait details as a JSON map | 

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
**201** | Trait created successfully |  -  |
**400** | Invalid input data |  -  |
**404** | Trait type not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trait**
> DeleteResponse delete_trait(object_uuid, trait_name)

Delete a trait from an object

Removes a trait identified by its name from the specified object. Returns a DeleteResponse confirming that the trait has been removed.

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
    api_instance = caraer_client.TraitsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    trait_name = 'trait_name_example' # str | 

    try:
        # Delete a trait from an object
        api_response = api_instance.delete_trait(object_uuid, trait_name)
        print("The response of TraitsApi->delete_trait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TraitsApi->delete_trait: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **trait_name** | **str**|  | 

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
**200** | Trait removed successfully |  -  |
**404** | Trait not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trait**
> ShowResponse get_trait(object_uuid, trait_name)

Fetch a specific trait for an object

Retrieves details of a specific trait associated with the specified object, identified by the trait name. Returns a ShowResponse containing the TraitDTO. If the trait is not found, a NotFoundError is thrown.

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
    api_instance = caraer_client.TraitsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    trait_name = 'trait_name_example' # str | 

    try:
        # Fetch a specific trait for an object
        api_response = api_instance.get_trait(object_uuid, trait_name)
        print("The response of TraitsApi->get_trait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TraitsApi->get_trait: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **trait_name** | **str**|  | 

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
**200** | Trait retrieved successfully |  -  |
**404** | Trait not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traits**
> PaginationResponse get_traits(object_uuid)

Fetch all traits for an object

Retrieves a list of traits associated with the specified object. Returns a paginated response containing TraitDTO objects. The page is set to 0 by default, with a maximum limit of 100.

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
    api_instance = caraer_client.TraitsApi(api_client)
    object_uuid = 'object_uuid_example' # str | 

    try:
        # Fetch all traits for an object
        api_response = api_instance.get_traits(object_uuid)
        print("The response of TraitsApi->get_traits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TraitsApi->get_traits: %s\n" % e)
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
**200** | Traits retrieved successfully |  -  |
**404** | Object or traits not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

