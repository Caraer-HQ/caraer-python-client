# caraer_client.BrowserAuthenticationApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](BrowserAuthenticationApi.md#authorize) | **GET** /api/v2/auth/browser/authorize | Open the browser-owned provider session
[**exchange**](BrowserAuthenticationApi.md#exchange) | **POST** /api/v2/auth/browser/exchange | Exchange a native callback code
[**start**](BrowserAuthenticationApi.md#start) | **POST** /api/v2/auth/browser/start | Start browser sign-in


# **authorize**
> authorize(flow)

Open the browser-owned provider session

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
    api_instance = caraer_client.BrowserAuthenticationApi(api_client)
    flow = 'flow_example' # str | 

    try:
        # Open the browser-owned provider session
        api_instance.authorize(flow)
    except Exception as e:
        print("Exception when calling BrowserAuthenticationApi->authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | **str**|  | 

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
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange**
> ShowResponseBrowserAuthSessionResponse exchange(browser_auth_exchange_request)

Exchange a native callback code

Exchanges an unexpired single-use code only after exact redirect and PKCE verifier checks. Access/refresh tokens are returned in JSON and never in callback URLs.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.browser_auth_exchange_request import BrowserAuthExchangeRequest
from caraer_client.models.show_response_browser_auth_session_response import ShowResponseBrowserAuthSessionResponse
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
    api_instance = caraer_client.BrowserAuthenticationApi(api_client)
    browser_auth_exchange_request = caraer_client.BrowserAuthExchangeRequest() # BrowserAuthExchangeRequest | 

    try:
        # Exchange a native callback code
        api_response = api_instance.exchange(browser_auth_exchange_request)
        print("The response of BrowserAuthenticationApi->exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserAuthenticationApi->exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browser_auth_exchange_request** | [**BrowserAuthExchangeRequest**](BrowserAuthExchangeRequest.md)|  | 

### Return type

[**ShowResponseBrowserAuthSessionResponse**](ShowResponseBrowserAuthSessionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> ShowResponseBrowserAuthStartResponse start(browser_auth_start_request)

Start browser sign-in

Requires an exact configured redirect URI, random client state and S256 PKCE challenge. Open the returned URL in the system browser.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.browser_auth_start_request import BrowserAuthStartRequest
from caraer_client.models.show_response_browser_auth_start_response import ShowResponseBrowserAuthStartResponse
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
    api_instance = caraer_client.BrowserAuthenticationApi(api_client)
    browser_auth_start_request = caraer_client.BrowserAuthStartRequest() # BrowserAuthStartRequest | 

    try:
        # Start browser sign-in
        api_response = api_instance.start(browser_auth_start_request)
        print("The response of BrowserAuthenticationApi->start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrowserAuthenticationApi->start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **browser_auth_start_request** | [**BrowserAuthStartRequest**](BrowserAuthStartRequest.md)|  | 

### Return type

[**ShowResponseBrowserAuthStartResponse**](ShowResponseBrowserAuthStartResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

