# caraer_client.AppBillingApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_billing_status**](AppBillingApi.md#app_billing_status) | **GET** /api/v2/apps/{appUuid}/billing/status | Current-period billing for every installation of an app
[**cancel_pending_change**](AppBillingApi.md#cancel_pending_change) | **DELETE** /api/v2/apps/{appUuid}/installation/subscription/pending | Cancel a scheduled subscription change
[**get_subscription**](AppBillingApi.md#get_subscription) | **GET** /api/v2/apps/{appUuid}/installation/subscription | Current subscription state for the selected company&#39;s installation
[**installation_billing_status**](AppBillingApi.md#installation_billing_status) | **GET** /api/v2/apps/{appUuid}/installation/billing/status | Current-period billing for the selected company&#39;s installation
[**platform_billing_status**](AppBillingApi.md#platform_billing_status) | **GET** /api/v2/apps/billing/status | Platform-wide current-period app usage billing
[**record_meter_event**](AppBillingApi.md#record_meter_event) | **POST** /api/v2/apps/{appUuid}/installation/meter-events | Record a manual meter event for the selected company&#39;s installation
[**schedule_subscription_change**](AppBillingApi.md#schedule_subscription_change) | **POST** /api/v2/apps/{appUuid}/installation/subscription/change | Schedule a plan or commitment change
[**usage_periods**](AppBillingApi.md#usage_periods) | **GET** /api/v2/apps/{appUuid}/installation/usage/periods | Usage periods for the selected company&#39;s installation


# **app_billing_status**
> ShowResponseAppBillingStatusResponse app_billing_status(app_uuid)

Current-period billing for every installation of an app

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_billing_status_response import ShowResponseAppBillingStatusResponse
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # Current-period billing for every installation of an app
        api_response = api_instance.app_billing_status(app_uuid)
        print("The response of AppBillingApi->app_billing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->app_billing_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

### Return type

[**ShowResponseAppBillingStatusResponse**](ShowResponseAppBillingStatusResponse.md)

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

# **cancel_pending_change**
> ShowResponseAppSubscriptionDTO cancel_pending_change(app_uuid)

Cancel a scheduled subscription change

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_subscription_dto import ShowResponseAppSubscriptionDTO
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # Cancel a scheduled subscription change
        api_response = api_instance.cancel_pending_change(app_uuid)
        print("The response of AppBillingApi->cancel_pending_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->cancel_pending_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

### Return type

[**ShowResponseAppSubscriptionDTO**](ShowResponseAppSubscriptionDTO.md)

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

# **get_subscription**
> ShowResponseAppSubscriptionDTO get_subscription(app_uuid)

Current subscription state for the selected company's installation

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_subscription_dto import ShowResponseAppSubscriptionDTO
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # Current subscription state for the selected company's installation
        api_response = api_instance.get_subscription(app_uuid)
        print("The response of AppBillingApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

### Return type

[**ShowResponseAppSubscriptionDTO**](ShowResponseAppSubscriptionDTO.md)

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

# **installation_billing_status**
> ShowResponseAppInstallationBillingStatusDTO installation_billing_status(app_uuid)

Current-period billing for the selected company's installation

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_installation_billing_status_dto import ShowResponseAppInstallationBillingStatusDTO
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # Current-period billing for the selected company's installation
        api_response = api_instance.installation_billing_status(app_uuid)
        print("The response of AppBillingApi->installation_billing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->installation_billing_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

### Return type

[**ShowResponseAppInstallationBillingStatusDTO**](ShowResponseAppInstallationBillingStatusDTO.md)

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

# **platform_billing_status**
> ShowResponseAppBillingStatusResponse platform_billing_status(app_uuid=app_uuid, page=page, limit=limit)

Platform-wide current-period app usage billing

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_billing_status_response import ShowResponseAppBillingStatusResponse
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Platform-wide current-period app usage billing
        api_response = api_instance.platform_billing_status(app_uuid=app_uuid, page=page, limit=limit)
        print("The response of AppBillingApi->platform_billing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->platform_billing_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**ShowResponseAppBillingStatusResponse**](ShowResponseAppBillingStatusResponse.md)

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

# **record_meter_event**
> ShowResponseAppMeterEventResponse record_meter_event(app_uuid, app_meter_event_request)

Record a manual meter event for the selected company's installation

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_meter_event_request import AppMeterEventRequest
from caraer_client.models.show_response_app_meter_event_response import ShowResponseAppMeterEventResponse
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    app_meter_event_request = caraer_client.AppMeterEventRequest() # AppMeterEventRequest | 

    try:
        # Record a manual meter event for the selected company's installation
        api_response = api_instance.record_meter_event(app_uuid, app_meter_event_request)
        print("The response of AppBillingApi->record_meter_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->record_meter_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **app_meter_event_request** | [**AppMeterEventRequest**](AppMeterEventRequest.md)|  | 

### Return type

[**ShowResponseAppMeterEventResponse**](ShowResponseAppMeterEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_subscription_change**
> ShowResponseAppSubscriptionDTO schedule_subscription_change(app_uuid, app_subscription_change_request)

Schedule a plan or commitment change

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_subscription_change_request import AppSubscriptionChangeRequest
from caraer_client.models.show_response_app_subscription_dto import ShowResponseAppSubscriptionDTO
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    app_subscription_change_request = caraer_client.AppSubscriptionChangeRequest() # AppSubscriptionChangeRequest | 

    try:
        # Schedule a plan or commitment change
        api_response = api_instance.schedule_subscription_change(app_uuid, app_subscription_change_request)
        print("The response of AppBillingApi->schedule_subscription_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->schedule_subscription_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **app_subscription_change_request** | [**AppSubscriptionChangeRequest**](AppSubscriptionChangeRequest.md)|  | 

### Return type

[**ShowResponseAppSubscriptionDTO**](ShowResponseAppSubscriptionDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_periods**
> ShowResponseListAppInstallationBillingStatusDTO usage_periods(app_uuid)

Usage periods for the selected company's installation

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_app_installation_billing_status_dto import ShowResponseListAppInstallationBillingStatusDTO
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
    api_instance = caraer_client.AppBillingApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # Usage periods for the selected company's installation
        api_response = api_instance.usage_periods(app_uuid)
        print("The response of AppBillingApi->usage_periods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBillingApi->usage_periods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

### Return type

[**ShowResponseListAppInstallationBillingStatusDTO**](ShowResponseListAppInstallationBillingStatusDTO.md)

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

