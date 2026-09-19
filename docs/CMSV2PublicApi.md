# caraer_client.CMSV2PublicApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_settings**](CMSV2PublicApi.md#app_settings) | **GET** /api/v2/webpages/v2/public/apps/{appName}/settings | Installed app settings with SECRET fields removed
[**asset**](CMSV2PublicApi.md#asset) | **GET** /api/v2/webpages/v2/public/asset | Redirect to a company file for the website runtime
[**build_manifest**](CMSV2PublicApi.md#build_manifest) | **GET** /api/v2/webpages/v2/build/manifest | Installed apps and modules for a company&#39;s website build
[**menus**](CMSV2PublicApi.md#menus) | **GET** /api/v2/webpages/v2/public/menus | Navigation menus for the header and footer
[**page_by_path**](CMSV2PublicApi.md#page_by_path) | **GET** /api/v2/webpages/v2/public/page | A published page by URL path
[**page_by_uuid**](CMSV2PublicApi.md#page_by_uuid) | **GET** /api/v2/webpages/v2/public/page/{uuid} | A page by record uuid
[**page_gate**](CMSV2PublicApi.md#page_gate) | **GET** /api/v2/webpages/v2/public/page/gate | Protection info for a path, without the page document
[**paths**](CMSV2PublicApi.md#paths) | **GET** /api/v2/webpages/v2/public/paths | Published paths per environment, for sitemaps and cache warming
[**records**](CMSV2PublicApi.md#records) | **POST** /api/v2/webpages/v2/public/records | Public records visible in an environment
[**settings**](CMSV2PublicApi.md#settings) | **GET** /api/v2/webpages/v2/public/settings | Company settings, branding and locales
[**unlock**](CMSV2PublicApi.md#unlock) | **POST** /api/v2/webpages/v2/public/page/{uuid}/unlock | Unlock a password-protected CMS v2 page


# **app_settings**
> ShowResponseMapStringObject app_settings(x_caraer_subdomain, app_name)

Installed app settings with SECRET fields removed

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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    app_name = 'app_name_example' # str | 

    try:
        # Installed app settings with SECRET fields removed
        api_response = api_instance.app_settings(x_caraer_subdomain, app_name)
        print("The response of CMSV2PublicApi->app_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->app_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **app_name** | **str**|  | 

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

# **asset**
> asset(x_caraer_subdomain, key, page_uuid=page_uuid, environment=environment, locale=locale, access=access, token=token, caraer_expires=caraer_expires, caraer_sig=caraer_sig, x_caraer_webpage_access=x_caraer_webpage_access, authorization=authorization)

Redirect to a company file for the website runtime

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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    key = 'key_example' # str | 
    page_uuid = 'page_uuid_example' # str |  (optional)
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    access = 'access_example' # str |  (optional)
    token = 'token_example' # str |  (optional)
    caraer_expires = 'caraer_expires_example' # str |  (optional)
    caraer_sig = 'caraer_sig_example' # str |  (optional)
    x_caraer_webpage_access = 'x_caraer_webpage_access_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Redirect to a company file for the website runtime
        api_instance.asset(x_caraer_subdomain, key, page_uuid=page_uuid, environment=environment, locale=locale, access=access, token=token, caraer_expires=caraer_expires, caraer_sig=caraer_sig, x_caraer_webpage_access=x_caraer_webpage_access, authorization=authorization)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **key** | **str**|  | 
 **page_uuid** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **access** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 
 **caraer_expires** | **str**|  | [optional] 
 **caraer_sig** | **str**|  | [optional] 
 **x_caraer_webpage_access** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **build_manifest**
> ShowResponseMapStringObject build_manifest(x_caraer_subdomain)

Installed apps and modules for a company's website build

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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 

    try:
        # Installed apps and modules for a company's website build
        api_response = api_instance.build_manifest(x_caraer_subdomain)
        print("The response of CMSV2PublicApi->build_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->build_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 

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

# **menus**
> ShowResponseListCmsPublicMenuDTO menus(x_caraer_subdomain, environment=environment, locale=locale)

Navigation menus for the header and footer

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_cms_public_menu_dto import ShowResponseListCmsPublicMenuDTO
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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)

    try:
        # Navigation menus for the header and footer
        api_response = api_instance.menus(x_caraer_subdomain, environment=environment, locale=locale)
        print("The response of CMSV2PublicApi->menus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->menus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 

### Return type

[**ShowResponseListCmsPublicMenuDTO**](ShowResponseListCmsPublicMenuDTO.md)

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

# **page_by_path**
> ShowResponseCmsPageDTO page_by_path(x_caraer_subdomain, path, x_caraer_webpage_access=x_caraer_webpage_access, authorization=authorization, environment=environment, locale=locale, access=access, token=token)

A published page by URL path

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_cms_page_dto import ShowResponseCmsPageDTO
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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    path = 'path_example' # str | 
    x_caraer_webpage_access = 'x_caraer_webpage_access_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    access = 'access_example' # str |  (optional)
    token = 'token_example' # str |  (optional)

    try:
        # A published page by URL path
        api_response = api_instance.page_by_path(x_caraer_subdomain, path, x_caraer_webpage_access=x_caraer_webpage_access, authorization=authorization, environment=environment, locale=locale, access=access, token=token)
        print("The response of CMSV2PublicApi->page_by_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->page_by_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **path** | **str**|  | 
 **x_caraer_webpage_access** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **access** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 

### Return type

[**ShowResponseCmsPageDTO**](ShowResponseCmsPageDTO.md)

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

# **page_by_uuid**
> ShowResponseCmsPageDTO page_by_uuid(x_caraer_subdomain, uuid, x_caraer_webpage_access=x_caraer_webpage_access, authorization=authorization, environment=environment, locale=locale, state=state, access=access, token=token, caraer_expires=caraer_expires, caraer_sig=caraer_sig)

A page by record uuid

Used by the builder preview, which addresses a page by uuid because a draft may not have a slug yet.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_cms_page_dto import ShowResponseCmsPageDTO
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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    uuid = 'uuid_example' # str | 
    x_caraer_webpage_access = 'x_caraer_webpage_access_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    state = 'published' # str |  (optional) (default to 'published')
    access = 'access_example' # str |  (optional)
    token = 'token_example' # str |  (optional)
    caraer_expires = 'caraer_expires_example' # str |  (optional)
    caraer_sig = 'caraer_sig_example' # str |  (optional)

    try:
        # A page by record uuid
        api_response = api_instance.page_by_uuid(x_caraer_subdomain, uuid, x_caraer_webpage_access=x_caraer_webpage_access, authorization=authorization, environment=environment, locale=locale, state=state, access=access, token=token, caraer_expires=caraer_expires, caraer_sig=caraer_sig)
        print("The response of CMSV2PublicApi->page_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->page_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **uuid** | **str**|  | 
 **x_caraer_webpage_access** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **state** | **str**|  | [optional] [default to &#39;published&#39;]
 **access** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 
 **caraer_expires** | **str**|  | [optional] 
 **caraer_sig** | **str**|  | [optional] 

### Return type

[**ShowResponseCmsPageDTO**](ShowResponseCmsPageDTO.md)

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

# **page_gate**
> ShowResponseMapStringObject page_gate(x_caraer_subdomain, path, environment=environment, locale=locale)

Protection info for a path, without the page document

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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    path = 'path_example' # str | 
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)

    try:
        # Protection info for a path, without the page document
        api_response = api_instance.page_gate(x_caraer_subdomain, path, environment=environment, locale=locale)
        print("The response of CMSV2PublicApi->page_gate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->page_gate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **path** | **str**|  | 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 

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

# **paths**
> ShowResponseListMapStringObject paths(x_caraer_subdomain, environment=environment, locale=locale)

Published paths per environment, for sitemaps and cache warming

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_map_string_object import ShowResponseListMapStringObject
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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)

    try:
        # Published paths per environment, for sitemaps and cache warming
        api_response = api_instance.paths(x_caraer_subdomain, environment=environment, locale=locale)
        print("The response of CMSV2PublicApi->paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->paths: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 

### Return type

[**ShowResponseListMapStringObject**](ShowResponseListMapStringObject.md)

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

# **records**
> ShowResponseMapStringObject records(x_caraer_subdomain, request_body, environment=environment, locale=locale)

Public records visible in an environment

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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)

    try:
        # Public records visible in an environment
        api_response = api_instance.records(x_caraer_subdomain, request_body, environment=environment, locale=locale)
        print("The response of CMSV2PublicApi->records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 

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

# **settings**
> ShowResponseMapStringObject settings(x_caraer_subdomain)

Company settings, branding and locales

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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 

    try:
        # Company settings, branding and locales
        api_response = api_instance.settings(x_caraer_subdomain)
        print("The response of CMSV2PublicApi->settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 

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

# **unlock**
> SuccessResponseString unlock(x_caraer_subdomain, uuid, request_body, environment=environment, locale=locale)

Unlock a password-protected CMS v2 page

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_string import SuccessResponseString
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
    api_instance = caraer_client.CMSV2PublicApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    uuid = 'uuid_example' # str | 
    request_body = {'key': 'request_body_example'} # Dict[str, str] | 
    environment = 'environment_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)

    try:
        # Unlock a password-protected CMS v2 page
        api_response = api_instance.unlock(x_caraer_subdomain, uuid, request_body, environment=environment, locale=locale)
        print("The response of CMSV2PublicApi->unlock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PublicApi->unlock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **uuid** | **str**|  | 
 **request_body** | [**Dict[str, str]**](str.md)|  | 
 **environment** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 

### Return type

[**SuccessResponseString**](SuccessResponseString.md)

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

