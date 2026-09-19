# caraer_client.CMSModulesApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](CMSModulesApi.md#list) | **GET** /api/v2/apps/{appUuid}/cms-modules | List an app&#39;s CMS modules
[**publish_package**](CMSModulesApi.md#publish_package) | **POST** /api/v2/apps/{appUuid}/cms-modules/package | Publish an app&#39;s CMS module package
[**upsert**](CMSModulesApi.md#upsert) | **PUT** /api/v2/apps/{appUuid}/cms-modules | Replace an app&#39;s CMS module catalog


# **list**
> ShowResponseListCmsModuleDTO list(app_uuid)

List an app's CMS modules

Includes retired modules, so a developer can see what a push removed.

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
    api_instance = caraer_client.CMSModulesApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # List an app's CMS modules
        api_response = api_instance.list(app_uuid)
        print("The response of CMSModulesApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSModulesApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

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

# **publish_package**
> ShowResponseListCmsModuleDTO publish_package(app_uuid, request_body)

Publish an app's CMS module package

Accepts a staged npm tarball (base64) and module manifests. Publishes to the platform registry with the host token, then replaces the catalog.

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
    api_instance = caraer_client.CMSModulesApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Publish an app's CMS module package
        api_response = api_instance.publish_package(app_uuid, request_body)
        print("The response of CMSModulesApi->publish_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSModulesApi->publish_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

### Return type

[**ShowResponseListCmsModuleDTO**](ShowResponseListCmsModuleDTO.md)

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

# **upsert**
> ShowResponseListCmsModuleDTO upsert(app_uuid, request_body)

Replace an app's CMS module catalog

Registers the modules shipped by a published package version. Modules missing from the payload are retired rather than deleted, because pages may still reference them.

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
    api_instance = caraer_client.CMSModulesApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Replace an app's CMS module catalog
        api_response = api_instance.upsert(app_uuid, request_body)
        print("The response of CMSModulesApi->upsert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSModulesApi->upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

### Return type

[**ShowResponseListCmsModuleDTO**](ShowResponseListCmsModuleDTO.md)

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

