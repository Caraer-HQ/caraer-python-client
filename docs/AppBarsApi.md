# caraer_client.AppBarsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_app_bars**](AppBarsApi.md#list_app_bars) | **GET** /api/v2/app-bars | List installed app bars for a location
[**trigger_app_bar**](AppBarsApi.md#trigger_app_bar) | **POST** /api/v2/app-bars/{appBarUuid}/trigger | Trigger an action-based app bar


# **list_app_bars**
> list_app_bars(location, object=object, record_uuid=record_uuid, view_id=view_id, trait=trait)

List installed app bars for a location

Returns all app bars from installed apps for the authenticated user's company at the given location.

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
    api_instance = caraer_client.AppBarsApi(api_client)
    location = 'location_example' # str | App bar location
    object = 'object_example' # str | Object name in context (optional)
    record_uuid = 'record_uuid_example' # str | Record UUID in context (optional)
    view_id = 'view_id_example' # str | View ID in context (optional)
    trait = 'trait_example' # str | Trait name in context (optional)

    try:
        # List installed app bars for a location
        api_instance.list_app_bars(location, object=object, record_uuid=record_uuid, view_id=view_id, trait=trait)
    except Exception as e:
        print("Exception when calling AppBarsApi->list_app_bars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| App bar location | 
 **object** | **str**| Object name in context | [optional] 
 **record_uuid** | **str**| Record UUID in context | [optional] 
 **view_id** | **str**| View ID in context | [optional] 
 **trait** | **str**| Trait name in context | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App bars retrieved |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_app_bar**
> trigger_app_bar(app_bar_uuid, app_bar_trigger_request=app_bar_trigger_request)

Trigger an action-based app bar

Fires the app bar webhook with optional settings values and record/view context.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_bar_trigger_request import AppBarTriggerRequest
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
    api_instance = caraer_client.AppBarsApi(api_client)
    app_bar_uuid = 'app_bar_uuid_example' # str | UUID of the app bar to trigger
    app_bar_trigger_request = caraer_client.AppBarTriggerRequest() # AppBarTriggerRequest |  (optional)

    try:
        # Trigger an action-based app bar
        api_instance.trigger_app_bar(app_bar_uuid, app_bar_trigger_request=app_bar_trigger_request)
    except Exception as e:
        print("Exception when calling AppBarsApi->trigger_app_bar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_bar_uuid** | **str**| UUID of the app bar to trigger | 
 **app_bar_trigger_request** | [**AppBarTriggerRequest**](AppBarTriggerRequest.md)|  | [optional] 

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
**200** | Trigger accepted |  -  |
**400** | Invalid request |  -  |
**404** | App bar not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

