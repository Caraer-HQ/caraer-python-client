# caraer_client.CMSWebsiteUpdatesApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pending**](CMSWebsiteUpdatesApi.md#pending) | **GET** /api/v2/webpages/v2/updates | Pending module updates for this website
[**preview**](CMSWebsiteUpdatesApi.md#preview) | **POST** /api/v2/webpages/v2/updates/preview | Build a preview site with every pending module update
[**promote**](CMSWebsiteUpdatesApi.md#promote) | **POST** /api/v2/webpages/v2/updates/promote | Promote a previewed module set to production


# **pending**
> ShowResponseMapStringObject pending()

Pending module updates for this website

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_map_string_object import ShowResponseMapStringObject
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
    api_instance = caraer_client.CMSWebsiteUpdatesApi(api_client)

    try:
        # Pending module updates for this website
        api_response = api_instance.pending()
        print("The response of CMSWebsiteUpdatesApi->pending:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSWebsiteUpdatesApi->pending: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponseMapStringObject**](ShowResponseMapStringObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview**
> ShowResponseMapStringObject preview()

Build a preview site with every pending module update

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_map_string_object import ShowResponseMapStringObject
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
    api_instance = caraer_client.CMSWebsiteUpdatesApi(api_client)

    try:
        # Build a preview site with every pending module update
        api_response = api_instance.preview()
        print("The response of CMSWebsiteUpdatesApi->preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSWebsiteUpdatesApi->preview: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponseMapStringObject**](ShowResponseMapStringObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote**
> ShowResponseMapStringObject promote(request_body=request_body)

Promote a previewed module set to production

Rejected with 409 when the preview revision is no longer the current pending set.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_map_string_object import ShowResponseMapStringObject
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
    api_instance = caraer_client.CMSWebsiteUpdatesApi(api_client)
    request_body = None # Dict[str, Optional[object]] |  (optional)

    try:
        # Promote a previewed module set to production
        api_response = api_instance.promote(request_body=request_body)
        print("The response of CMSWebsiteUpdatesApi->promote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSWebsiteUpdatesApi->promote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | [optional] 

### Return type

[**ShowResponseMapStringObject**](ShowResponseMapStringObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

