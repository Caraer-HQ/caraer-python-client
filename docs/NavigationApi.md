# caraer_client.NavigationApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**favorites**](NavigationApi.md#favorites) | **GET** /api/v2/navigation/favorites | Read authorized favorite views
[**navigation**](NavigationApi.md#navigation) | **GET** /api/v2/navigation | Read authorized navigation
[**preferences**](NavigationApi.md#preferences) | **PUT** /api/v2/navigation/objects/{objectUuid}/view-preferences | Set personal view navigation preferences
[**scopes**](NavigationApi.md#scopes) | **GET** /api/v2/access/scopes | Read available access scopes
[**views**](NavigationApi.md#views) | **GET** /api/v2/navigation/objects/{objectUuid}/views | Read authorized view navigation summaries


# **favorites**
> SuccessResponseListFavoriteViewDTO favorites(include_archived=include_archived)

Read authorized favorite views

Selected-company favorites across objects. Archived readable favorites require includeArchived=true. Each result carries only object identity/capability names and view navigation metadata.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_favorite_view_dto import SuccessResponseListFavoriteViewDTO
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
    api_instance = caraer_client.NavigationApi(api_client)
    include_archived = False # bool |  (optional) (default to False)

    try:
        # Read authorized favorite views
        api_response = api_instance.favorites(include_archived=include_archived)
        print("The response of NavigationApi->favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NavigationApi->favorites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_archived** | **bool**|  | [optional] [default to False]

### Return type

[**SuccessResponseListFavoriteViewDTO**](SuccessResponseListFavoriteViewDTO.md)

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

# **navigation**
> SuccessResponseNavigationDTO navigation()

Read authorized navigation

Selected-company object and view summaries with permission-gated menus. Does not load schemas, users, scopes, branding or dashboards.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_navigation_dto import SuccessResponseNavigationDTO
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
    api_instance = caraer_client.NavigationApi(api_client)

    try:
        # Read authorized navigation
        api_response = api_instance.navigation()
        print("The response of NavigationApi->navigation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NavigationApi->navigation: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponseNavigationDTO**](SuccessResponseNavigationDTO.md)

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

# **preferences**
> SuccessResponseListNavigationViewDTO preferences(object_uuid, view_navigation_preferences_request)

Set personal view navigation preferences

Atomic user/company-scoped index and favorite overrides for readable views of this object. Omission preserves; null clears to the legacy default. Does not create sharing edges or change authorization. Requires an actual selected-company user record.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_navigation_view_dto import SuccessResponseListNavigationViewDTO
from caraer_client.models.view_navigation_preferences_request import ViewNavigationPreferencesRequest
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
    api_instance = caraer_client.NavigationApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    view_navigation_preferences_request = caraer_client.ViewNavigationPreferencesRequest() # ViewNavigationPreferencesRequest | 

    try:
        # Set personal view navigation preferences
        api_response = api_instance.preferences(object_uuid, view_navigation_preferences_request)
        print("The response of NavigationApi->preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NavigationApi->preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **view_navigation_preferences_request** | [**ViewNavigationPreferencesRequest**](ViewNavigationPreferencesRequest.md)|  | 

### Return type

[**SuccessResponseListNavigationViewDTO**](SuccessResponseListNavigationViewDTO.md)

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

# **scopes**
> SuccessResponseListString scopes()

Read available access scopes

Scope catalog for managing selected-company user and team permissions. Requires user-management read or app-management write access. App-only callers discover record scopes only for readable objects. This is not a list of the caller's granted scopes.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_string import SuccessResponseListString
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
    api_instance = caraer_client.NavigationApi(api_client)

    try:
        # Read available access scopes
        api_response = api_instance.scopes()
        print("The response of NavigationApi->scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NavigationApi->scopes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponseListString**](SuccessResponseListString.md)

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

# **views**
> SuccessResponseListNavigationViewDTO views(object_uuid, include_archived=include_archived)

Read authorized view navigation summaries

Intent-loaded selected-company metadata. Archived readable views are included only with includeArchived=true; no filters, schemas or sharing grants are returned.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_navigation_view_dto import SuccessResponseListNavigationViewDTO
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
    api_instance = caraer_client.NavigationApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    include_archived = False # bool |  (optional) (default to False)

    try:
        # Read authorized view navigation summaries
        api_response = api_instance.views(object_uuid, include_archived=include_archived)
        print("The response of NavigationApi->views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NavigationApi->views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **include_archived** | **bool**|  | [optional] [default to False]

### Return type

[**SuccessResponseListNavigationViewDTO**](SuccessResponseListNavigationViewDTO.md)

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

