# caraer_client.AppBarIframeSessionsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iframe_session**](AppBarIframeSessionsApi.md#create_iframe_session) | **POST** /api/v2/app-bars/{appBarUuid}/iframe-session | Create an iframe session token
[**validate_iframe_session**](AppBarIframeSessionsApi.md#validate_iframe_session) | **POST** /api/v2/app-bars/iframe-session/validate | Validate an iframe session token


# **create_iframe_session**
> create_iframe_session(app_bar_uuid, app_bar_iframe_session_request=app_bar_iframe_session_request)

Create an iframe session token

Issues a short-lived opaque token for an iframe-based app bar. The token can be validated by the embedded app to confirm user, company, view, and filter context.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_bar_iframe_session_request import AppBarIframeSessionRequest
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
    api_instance = caraer_client.AppBarIframeSessionsApi(api_client)
    app_bar_uuid = 'app_bar_uuid_example' # str | UUID of the iframe app bar
    app_bar_iframe_session_request = caraer_client.AppBarIframeSessionRequest() # AppBarIframeSessionRequest |  (optional)

    try:
        # Create an iframe session token
        api_instance.create_iframe_session(app_bar_uuid, app_bar_iframe_session_request=app_bar_iframe_session_request)
    except Exception as e:
        print("Exception when calling AppBarIframeSessionsApi->create_iframe_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_bar_uuid** | **str**| UUID of the iframe app bar | 
 **app_bar_iframe_session_request** | [**AppBarIframeSessionRequest**](AppBarIframeSessionRequest.md)|  | [optional] 

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
**200** | Token created |  -  |
**400** | Invalid request |  -  |
**404** | App bar not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_iframe_session**
> validate_iframe_session(app_bar_iframe_session_validate_request)

Validate an iframe session token

Public endpoint for embedded apps to validate a caraer_iframe_token and receive safe context.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_bar_iframe_session_validate_request import AppBarIframeSessionValidateRequest
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
    api_instance = caraer_client.AppBarIframeSessionsApi(api_client)
    app_bar_iframe_session_validate_request = caraer_client.AppBarIframeSessionValidateRequest() # AppBarIframeSessionValidateRequest | 

    try:
        # Validate an iframe session token
        api_instance.validate_iframe_session(app_bar_iframe_session_validate_request)
    except Exception as e:
        print("Exception when calling AppBarIframeSessionsApi->validate_iframe_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_bar_iframe_session_validate_request** | [**AppBarIframeSessionValidateRequest**](AppBarIframeSessionValidateRequest.md)|  | 

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
**200** | Token validated |  -  |
**401** | Invalid or expired token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

