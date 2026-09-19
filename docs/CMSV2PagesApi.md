# caraer_client.CMSV2PagesApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_rewrite**](CMSV2PagesApi.md#ai_rewrite) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/ai/rewrite | Rewrite a page or a module from a prompt
[**create_translation**](CMSV2PagesApi.md#create_translation) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/environments/{key}/translate | Create a translated sibling page for an environment
[**discard_module_fork**](CMSV2PagesApi.md#discard_module_fork) | **DELETE** /api/v2/webpages/v2/pages/{recordUuid}/ai/module-fork/sessions/{sessionId} | Discard a Modify-this-module playground session
[**ensure_not_found**](CMSV2PagesApi.md#ensure_not_found) | **POST** /api/v2/webpages/v2/pages/not-found | Create or reuse the custom 404 page
[**environment_coverage**](CMSV2PagesApi.md#environment_coverage) | **GET** /api/v2/webpages/v2/pages/{recordUuid}/environments | Environment coverage for the builder dropdown
[**get**](CMSV2PagesApi.md#get) | **GET** /api/v2/webpages/v2/pages/{recordUuid} | Load a page for the builder
[**get_template**](CMSV2PagesApi.md#get_template) | **GET** /api/v2/webpages/v2/pages/templates/{objectUuid} | CMS v2 object template document
[**history**](CMSV2PagesApi.md#history) | **GET** /api/v2/webpages/v2/pages/{recordUuid}/history | Draft snapshots for one locale
[**host_on_environment**](CMSV2PagesApi.md#host_on_environment) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/environments/{key}/host | Host this page on another environment
[**library**](CMSV2PagesApi.md#library) | **GET** /api/v2/webpages/v2/pages/library/modules | Modules available to this company
[**patch**](CMSV2PagesApi.md#patch) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/patch | Apply patches to a page draft
[**preview_link**](CMSV2PagesApi.md#preview_link) | **GET** /api/v2/webpages/v2/pages/{recordUuid}/preview-link | Signed preview URL for the builder iframe
[**prompt_module_fork**](CMSV2PagesApi.md#prompt_module_fork) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/ai/module-fork/sessions/{sessionId}/prompt | Rewrite forked module source from a prompt
[**publish**](CMSV2PagesApi.md#publish) | **PUT** /api/v2/webpages/v2/pages/{recordUuid}/publish | Publish one locale, or all of them
[**restore_history**](CMSV2PagesApi.md#restore_history) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/history/{index}/restore | Restore a draft snapshot
[**save**](CMSV2PagesApi.md#save) | **PUT** /api/v2/webpages/v2/pages/{recordUuid} | Replace a page draft
[**save_meta**](CMSV2PagesApi.md#save_meta) | **PUT** /api/v2/webpages/v2/pages/{recordUuid}/meta | Update slug, title, excerpt, SEO and page scripts
[**save_module_fork**](CMSV2PagesApi.md#save_module_fork) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/ai/module-fork/sessions/{sessionId}/save | Publish the forked module into a private app
[**save_template**](CMSV2PagesApi.md#save_template) | **PUT** /api/v2/webpages/v2/pages/templates/{objectUuid} | Replace a CMS v2 object template
[**start_module_fork**](CMSV2PagesApi.md#start_module_fork) | **POST** /api/v2/webpages/v2/pages/{recordUuid}/ai/module-fork/sessions | Start a Modify-this-module playground session
[**unpublish**](CMSV2PagesApi.md#unpublish) | **PUT** /api/v2/webpages/v2/pages/{recordUuid}/unpublish | Take one locale offline
[**unselect_environment**](CMSV2PagesApi.md#unselect_environment) | **DELETE** /api/v2/webpages/v2/pages/{recordUuid}/environments/{key} | Remove an environment from this page only
[**update_module_fork_fields**](CMSV2PagesApi.md#update_module_fork_fields) | **PUT** /api/v2/webpages/v2/pages/{recordUuid}/ai/module-fork/sessions/{sessionId}/fields | Preview field values on the forked module


# **ai_rewrite**
> ShowResponseMapStringObject ai_rewrite(record_uuid, request_body)

Rewrite a page or a module from a prompt

Returns patches the editor applies through the same revision channel as a manual edit, so the change is undoable. Page scope may add, remove and reorder modules. A module's code lives in a shared npm package, so the AI rewrites field values and composition, never the component itself.

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Rewrite a page or a module from a prompt
        api_response = api_instance.ai_rewrite(record_uuid, request_body)
        print("The response of CMSV2PagesApi->ai_rewrite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->ai_rewrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

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

# **create_translation**
> ShowResponseCmsPageDTO create_translation(record_uuid, key)

Create a translated sibling page for an environment

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    key = 'key_example' # str | 

    try:
        # Create a translated sibling page for an environment
        api_response = api_instance.create_translation(record_uuid, key)
        print("The response of CMSV2PagesApi->create_translation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->create_translation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **key** | **str**|  | 

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

# **discard_module_fork**
> ShowResponseMapStringObject discard_module_fork(record_uuid, session_id)

Discard a Modify-this-module playground session

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # Discard a Modify-this-module playground session
        api_response = api_instance.discard_module_fork(record_uuid, session_id)
        print("The response of CMSV2PagesApi->discard_module_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->discard_module_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **session_id** | **str**|  | 

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

# **ensure_not_found**
> ShowResponseCmsPageDTO ensure_not_found()

Create or reuse the custom 404 page

Finds the page at /404 on the root Webpage object, or creates an empty draft there, and stores it as the company custom 404 page.

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)

    try:
        # Create or reuse the custom 404 page
        api_response = api_instance.ensure_not_found()
        print("The response of CMSV2PagesApi->ensure_not_found:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->ensure_not_found: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **environment_coverage**
> ShowResponseMapStringObject environment_coverage(record_uuid)

Environment coverage for the builder dropdown

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 

    try:
        # Environment coverage for the builder dropdown
        api_response = api_instance.environment_coverage(record_uuid)
        print("The response of CMSV2PagesApi->environment_coverage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->environment_coverage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 

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

# **get**
> ShowResponseCmsPageDTO get(record_uuid, locale=locale, state=state)

Load a page for the builder

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    locale = 'locale_example' # str |  (optional)
    state = 'draft' # str |  (optional) (default to 'draft')

    try:
        # Load a page for the builder
        api_response = api_instance.get(record_uuid, locale=locale, state=state)
        print("The response of CMSV2PagesApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **locale** | **str**|  | [optional] 
 **state** | **str**|  | [optional] [default to &#39;draft&#39;]

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

# **get_template**
> ShowResponseCmsPageDocument get_template(object_uuid, locale=locale)

CMS v2 object template document

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_cms_page_document import ShowResponseCmsPageDocument
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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    locale = 'locale_example' # str |  (optional)

    try:
        # CMS v2 object template document
        api_response = api_instance.get_template(object_uuid, locale=locale)
        print("The response of CMSV2PagesApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **locale** | **str**|  | [optional] 

### Return type

[**ShowResponseCmsPageDocument**](ShowResponseCmsPageDocument.md)

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

# **history**
> ShowResponseListMapStringObject history(record_uuid, locale=locale)

Draft snapshots for one locale

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    locale = 'locale_example' # str |  (optional)

    try:
        # Draft snapshots for one locale
        api_response = api_instance.history(record_uuid, locale=locale)
        print("The response of CMSV2PagesApi->history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
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

# **host_on_environment**
> ShowResponseCmsPageDTO host_on_environment(record_uuid, key)

Host this page on another environment

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    key = 'key_example' # str | 

    try:
        # Host this page on another environment
        api_response = api_instance.host_on_environment(record_uuid, key)
        print("The response of CMSV2PagesApi->host_on_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->host_on_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **key** | **str**|  | 

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

# **library**
> ShowResponseListCmsModuleDTO library()

Modules available to this company

Backs the builder's library picker. Only modules from installed apps, and never retired ones, because a new page must be able to render them.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_cms_module_dto import ShowResponseListCmsModuleDTO
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
    api_instance = caraer_client.CMSV2PagesApi(api_client)

    try:
        # Modules available to this company
        api_response = api_instance.library()
        print("The response of CMSV2PagesApi->library:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->library: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponseListCmsModuleDTO**](ShowResponseListCmsModuleDTO.md)

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

# **patch**
> ShowResponseCmsPageDTO patch(record_uuid, cms_page_patch_request)

Apply patches to a page draft

Rejected with 409 when expectedRevision does not match, so a stale client cannot overwrite another editor's work.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.cms_page_patch_request import CmsPagePatchRequest
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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    cms_page_patch_request = caraer_client.CmsPagePatchRequest() # CmsPagePatchRequest | 

    try:
        # Apply patches to a page draft
        api_response = api_instance.patch(record_uuid, cms_page_patch_request)
        print("The response of CMSV2PagesApi->patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **cms_page_patch_request** | [**CmsPagePatchRequest**](CmsPagePatchRequest.md)|  | 

### Return type

[**ShowResponseCmsPageDTO**](ShowResponseCmsPageDTO.md)

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

# **preview_link**
> ShowResponseMapStringObject preview_link(record_uuid, locale=locale, state=state)

Signed preview URL for the builder iframe

The iframe renders the draft document, which the public API will not serve. The signature covers the page and an expiry so a leaked link cannot be retargeted or replayed.

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    locale = 'locale_example' # str |  (optional)
    state = 'draft' # str |  (optional) (default to 'draft')

    try:
        # Signed preview URL for the builder iframe
        api_response = api_instance.preview_link(record_uuid, locale=locale, state=state)
        print("The response of CMSV2PagesApi->preview_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->preview_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **locale** | **str**|  | [optional] 
 **state** | **str**|  | [optional] [default to &#39;draft&#39;]

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

# **prompt_module_fork**
> ShowResponseMapStringObject prompt_module_fork(record_uuid, session_id, request_body)

Rewrite forked module source from a prompt

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    session_id = 'session_id_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Rewrite forked module source from a prompt
        api_response = api_instance.prompt_module_fork(record_uuid, session_id, request_body)
        print("The response of CMSV2PagesApi->prompt_module_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->prompt_module_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **session_id** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

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

# **publish**
> ShowResponseListCmsPageDTO publish(record_uuid, locale=locale, all_locales=all_locales)

Publish one locale, or all of them

Copies the draft over the published document. Publishing is per locale so a translated page can ship without republishing the others.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_cms_page_dto import ShowResponseListCmsPageDTO
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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    locale = 'locale_example' # str |  (optional)
    all_locales = False # bool |  (optional) (default to False)

    try:
        # Publish one locale, or all of them
        api_response = api_instance.publish(record_uuid, locale=locale, all_locales=all_locales)
        print("The response of CMSV2PagesApi->publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **locale** | **str**|  | [optional] 
 **all_locales** | **bool**|  | [optional] [default to False]

### Return type

[**ShowResponseListCmsPageDTO**](ShowResponseListCmsPageDTO.md)

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

# **restore_history**
> ShowResponseCmsPageDTO restore_history(record_uuid, index, locale=locale)

Restore a draft snapshot

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    index = 56 # int | 
    locale = 'locale_example' # str |  (optional)

    try:
        # Restore a draft snapshot
        api_response = api_instance.restore_history(record_uuid, index, locale=locale)
        print("The response of CMSV2PagesApi->restore_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->restore_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **index** | **int**|  | 
 **locale** | **str**|  | [optional] 

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

# **save**
> ShowResponseCmsPageDTO save(record_uuid, cms_page_document, locale=locale)

Replace a page draft

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.cms_page_document import CmsPageDocument
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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    cms_page_document = caraer_client.CmsPageDocument() # CmsPageDocument | 
    locale = 'locale_example' # str |  (optional)

    try:
        # Replace a page draft
        api_response = api_instance.save(record_uuid, cms_page_document, locale=locale)
        print("The response of CMSV2PagesApi->save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **cms_page_document** | [**CmsPageDocument**](CmsPageDocument.md)|  | 
 **locale** | **str**|  | [optional] 

### Return type

[**ShowResponseCmsPageDTO**](ShowResponseCmsPageDTO.md)

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

# **save_meta**
> ShowResponseCmsPageDTO save_meta(record_uuid, request_body, locale=locale)

Update slug, title, excerpt, SEO and page scripts

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 
    locale = 'locale_example' # str |  (optional)

    try:
        # Update slug, title, excerpt, SEO and page scripts
        api_response = api_instance.save_meta(record_uuid, request_body, locale=locale)
        print("The response of CMSV2PagesApi->save_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->save_meta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 
 **locale** | **str**|  | [optional] 

### Return type

[**ShowResponseCmsPageDTO**](ShowResponseCmsPageDTO.md)

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

# **save_module_fork**
> ShowResponseMapStringObject save_module_fork(record_uuid, session_id, request_body)

Publish the forked module into a private app

Merges the new module into the whole npm package so sibling modules are not retired, then swaps this placement with set_module.

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    session_id = 'session_id_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Publish the forked module into a private app
        api_response = api_instance.save_module_fork(record_uuid, session_id, request_body)
        print("The response of CMSV2PagesApi->save_module_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->save_module_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **session_id** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

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

# **save_template**
> ShowResponseCmsPageDocument save_template(object_uuid, cms_page_document, locale=locale)

Replace a CMS v2 object template

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.cms_page_document import CmsPageDocument
from caraer_client.models.show_response_cms_page_document import ShowResponseCmsPageDocument
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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    object_uuid = 'object_uuid_example' # str | 
    cms_page_document = caraer_client.CmsPageDocument() # CmsPageDocument | 
    locale = 'locale_example' # str |  (optional)

    try:
        # Replace a CMS v2 object template
        api_response = api_instance.save_template(object_uuid, cms_page_document, locale=locale)
        print("The response of CMSV2PagesApi->save_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->save_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**|  | 
 **cms_page_document** | [**CmsPageDocument**](CmsPageDocument.md)|  | 
 **locale** | **str**|  | [optional] 

### Return type

[**ShowResponseCmsPageDocument**](ShowResponseCmsPageDocument.md)

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

# **start_module_fork**
> ShowResponseMapStringObject start_module_fork(record_uuid, request_body)

Start a Modify-this-module playground session

CMS v2 companies and pages only. Copies the installed module's published source into a playground session. Live code edits stay off the company site until save publishes a platform v2 private-app package and a rebuild compiles it.

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Start a Modify-this-module playground session
        api_response = api_instance.start_module_fork(record_uuid, request_body)
        print("The response of CMSV2PagesApi->start_module_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->start_module_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

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

# **unpublish**
> ShowResponseMapStringObject unpublish(record_uuid, locale=locale)

Take one locale offline

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    locale = 'locale_example' # str |  (optional)

    try:
        # Take one locale offline
        api_response = api_instance.unpublish(record_uuid, locale=locale)
        print("The response of CMSV2PagesApi->unpublish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->unpublish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
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

# **unselect_environment**
> ShowResponseCmsPageDTO unselect_environment(record_uuid, key)

Remove an environment from this page only

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    key = 'key_example' # str | 

    try:
        # Remove an environment from this page only
        api_response = api_instance.unselect_environment(record_uuid, key)
        print("The response of CMSV2PagesApi->unselect_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->unselect_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **key** | **str**|  | 

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

# **update_module_fork_fields**
> ShowResponseMapStringObject update_module_fork_fields(record_uuid, session_id, request_body)

Preview field values on the forked module

Writes test values into the playground session without changing the live page.

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
    api_instance = caraer_client.CMSV2PagesApi(api_client)
    record_uuid = 'record_uuid_example' # str | 
    session_id = 'session_id_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Preview field values on the forked module
        api_response = api_instance.update_module_fork_fields(record_uuid, session_id, request_body)
        print("The response of CMSV2PagesApi->update_module_fork_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2PagesApi->update_module_fork_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**|  | 
 **session_id** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

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

