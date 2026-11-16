# caraer_client.PortalAppearanceApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**effective**](PortalAppearanceApi.md#effective) | **GET** /api/v2/appearance | Read effective portal appearance
[**own**](PortalAppearanceApi.md#own) | **GET** /api/v2/partner/appearance | Read selected partner appearance
[**save1**](PortalAppearanceApi.md#save1) | **PUT** /api/v2/partner/appearance | Save selected partner appearance


# **effective**
> SuccessResponseEffectiveAppearanceDTO effective()

Read effective portal appearance

Authenticated selected-company branding inherited from its nearest whitelabel partner, with server-derived management capability. No partner identities are disclosed.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_effective_appearance_dto import SuccessResponseEffectiveAppearanceDTO
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
    api_instance = caraer_client.PortalAppearanceApi(api_client)

    try:
        # Read effective portal appearance
        api_response = api_instance.effective()
        print("The response of PortalAppearanceApi->effective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalAppearanceApi->effective: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponseEffectiveAppearanceDTO**](SuccessResponseEffectiveAppearanceDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **own**
> SuccessResponsePortalAppearanceDTO own()

Read selected partner appearance

Requires a whitelabel selected-company entitlement, selected membership and company-settings write permission.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_portal_appearance_dto import SuccessResponsePortalAppearanceDTO
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
    api_instance = caraer_client.PortalAppearanceApi(api_client)

    try:
        # Read selected partner appearance
        api_response = api_instance.own()
        print("The response of PortalAppearanceApi->own:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalAppearanceApi->own: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponsePortalAppearanceDTO**](SuccessResponsePortalAppearanceDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **save1**
> SuccessResponsePortalAppearanceDTO save1(portal_appearance_dto)

Save selected partner appearance

Writes only the selected whitelabel partner. Requires company-settings write permission. Null values restore Caraer defaults. No target company identifier is accepted.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.portal_appearance_dto import PortalAppearanceDTO
from caraer_client.models.success_response_portal_appearance_dto import SuccessResponsePortalAppearanceDTO
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
    api_instance = caraer_client.PortalAppearanceApi(api_client)
    portal_appearance_dto = caraer_client.PortalAppearanceDTO() # PortalAppearanceDTO | 

    try:
        # Save selected partner appearance
        api_response = api_instance.save1(portal_appearance_dto)
        print("The response of PortalAppearanceApi->save1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalAppearanceApi->save1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_appearance_dto** | [**PortalAppearanceDTO**](PortalAppearanceDTO.md)|  | 

### Return type

[**SuccessResponsePortalAppearanceDTO**](SuccessResponsePortalAppearanceDTO.md)

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

