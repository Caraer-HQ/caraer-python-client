# caraer_client.CMSV2EnvironmentsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](CMSV2EnvironmentsApi.md#create3) | **POST** /api/v2/cms/environments | Create an environment
[**delete1**](CMSV2EnvironmentsApi.md#delete1) | **DELETE** /api/v2/cms/environments/{key} | Delete an environment except main
[**group**](CMSV2EnvironmentsApi.md#group) | **GET** /api/v2/cms/environments/translations/{recordUuid} | Translation group for a record
[**link**](CMSV2EnvironmentsApi.md#link) | **POST** /api/v2/cms/environments/translations/{fromUuid}/link/{toUuid} | Link two records as translations
[**list2**](CMSV2EnvironmentsApi.md#list2) | **GET** /api/v2/cms/environments | List company environments
[**unlink**](CMSV2EnvironmentsApi.md#unlink) | **DELETE** /api/v2/cms/environments/translations/{fromUuid}/link/{toUuid} | Unlink a translation edge
[**update1**](CMSV2EnvironmentsApi.md#update1) | **PUT** /api/v2/cms/environments/{key} | Update routing, auth or htmlLang. Keys are immutable.


# **create3**
> ShowResponseCmsEnvironmentDTO create3(cms_environment_dto)

Create an environment

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.cms_environment_dto import CmsEnvironmentDTO
from caraer_client.models.show_response_cms_environment_dto import ShowResponseCmsEnvironmentDTO
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
    api_instance = caraer_client.CMSV2EnvironmentsApi(api_client)
    cms_environment_dto = caraer_client.CmsEnvironmentDTO() # CmsEnvironmentDTO | 

    try:
        # Create an environment
        api_response = api_instance.create3(cms_environment_dto)
        print("The response of CMSV2EnvironmentsApi->create3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2EnvironmentsApi->create3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cms_environment_dto** | [**CmsEnvironmentDTO**](CmsEnvironmentDTO.md)|  | 

### Return type

[**ShowResponseCmsEnvironmentDTO**](ShowResponseCmsEnvironmentDTO.md)

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

# **delete1**
> SuccessResponseString delete1(key)

Delete an environment except main

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
    api_instance = caraer_client.CMSV2EnvironmentsApi(api_client)
    key = 'key_example' # str | 

    try:
        # Delete an environment except main
        api_response = api_instance.delete1(key)
        print("The response of CMSV2EnvironmentsApi->delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2EnvironmentsApi->delete1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**SuccessResponseString**](SuccessResponseString.md)

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

# **group**
> ShowResponseMapStringObject group(record_uuid)

Translation group for a record

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
    api_instance = caraer_client.CMSV2EnvironmentsApi(api_client)
    record_uuid = 'record_uuid_example' # str | 

    try:
        # Translation group for a record
        api_response = api_instance.group(record_uuid)
        print("The response of CMSV2EnvironmentsApi->group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2EnvironmentsApi->group: %s\n" % e)
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

# **link**
> SuccessResponseString link(from_uuid, to_uuid)

Link two records as translations

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
    api_instance = caraer_client.CMSV2EnvironmentsApi(api_client)
    from_uuid = 'from_uuid_example' # str | 
    to_uuid = 'to_uuid_example' # str | 

    try:
        # Link two records as translations
        api_response = api_instance.link(from_uuid, to_uuid)
        print("The response of CMSV2EnvironmentsApi->link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2EnvironmentsApi->link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_uuid** | **str**|  | 
 **to_uuid** | **str**|  | 

### Return type

[**SuccessResponseString**](SuccessResponseString.md)

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

# **list2**
> ShowResponseListCmsEnvironmentDTO list2()

List company environments

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_cms_environment_dto import ShowResponseListCmsEnvironmentDTO
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
    api_instance = caraer_client.CMSV2EnvironmentsApi(api_client)

    try:
        # List company environments
        api_response = api_instance.list2()
        print("The response of CMSV2EnvironmentsApi->list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2EnvironmentsApi->list2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponseListCmsEnvironmentDTO**](ShowResponseListCmsEnvironmentDTO.md)

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

# **unlink**
> SuccessResponseString unlink(from_uuid, to_uuid)

Unlink a translation edge

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
    api_instance = caraer_client.CMSV2EnvironmentsApi(api_client)
    from_uuid = 'from_uuid_example' # str | 
    to_uuid = 'to_uuid_example' # str | 

    try:
        # Unlink a translation edge
        api_response = api_instance.unlink(from_uuid, to_uuid)
        print("The response of CMSV2EnvironmentsApi->unlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2EnvironmentsApi->unlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_uuid** | **str**|  | 
 **to_uuid** | **str**|  | 

### Return type

[**SuccessResponseString**](SuccessResponseString.md)

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

# **update1**
> ShowResponseCmsEnvironmentDTO update1(key, cms_environment_dto)

Update routing, auth or htmlLang. Keys are immutable.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.cms_environment_dto import CmsEnvironmentDTO
from caraer_client.models.show_response_cms_environment_dto import ShowResponseCmsEnvironmentDTO
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
    api_instance = caraer_client.CMSV2EnvironmentsApi(api_client)
    key = 'key_example' # str | 
    cms_environment_dto = caraer_client.CmsEnvironmentDTO() # CmsEnvironmentDTO | 

    try:
        # Update routing, auth or htmlLang. Keys are immutable.
        api_response = api_instance.update1(key, cms_environment_dto)
        print("The response of CMSV2EnvironmentsApi->update1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2EnvironmentsApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **cms_environment_dto** | [**CmsEnvironmentDTO**](CmsEnvironmentDTO.md)|  | 

### Return type

[**ShowResponseCmsEnvironmentDTO**](ShowResponseCmsEnvironmentDTO.md)

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

