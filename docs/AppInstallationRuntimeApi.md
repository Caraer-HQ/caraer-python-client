# caraer_client.AppInstallationRuntimeApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_secret**](AppInstallationRuntimeApi.md#delete_secret) | **DELETE** /api/v2/apps/{appUuid}/installation/secrets/{name} | Delete an encrypted secret
[**delete_state_key**](AppInstallationRuntimeApi.md#delete_state_key) | **DELETE** /api/v2/apps/{appUuid}/installation/state/{key} | Delete a state key
[**enqueue_job**](AppInstallationRuntimeApi.md#enqueue_job) | **POST** /api/v2/apps/{appUuid}/installation/jobs | Enqueue an async serverless function job
[**get_job**](AppInstallationRuntimeApi.md#get_job) | **GET** /api/v2/apps/{appUuid}/installation/jobs/{jobId} | Get async job status
[**get_state**](AppInstallationRuntimeApi.md#get_state) | **GET** /api/v2/apps/{appUuid}/installation/state | Get installation state map
[**get_state_key**](AppInstallationRuntimeApi.md#get_state_key) | **GET** /api/v2/apps/{appUuid}/installation/state/{key} | Get a single state key
[**list_connections**](AppInstallationRuntimeApi.md#list_connections) | **GET** /api/v2/apps/{appUuid}/installation/connections | List external OAuth connection status
[**list_secrets**](AppInstallationRuntimeApi.md#list_secrets) | **GET** /api/v2/apps/{appUuid}/installation/secrets | List secret names (no values)
[**merge_company_settings**](AppInstallationRuntimeApi.md#merge_company_settings) | **PUT** /api/v2/apps/{appUuid}/installation/settings | Merge COMPANY-scoped installation settings from the app runtime
[**put_secret**](AppInstallationRuntimeApi.md#put_secret) | **PUT** /api/v2/apps/{appUuid}/installation/secrets/{name} | Set an encrypted secret
[**put_state**](AppInstallationRuntimeApi.md#put_state) | **PUT** /api/v2/apps/{appUuid}/installation/state | Replace/merge installation state (shallow merge)
[**put_state_key**](AppInstallationRuntimeApi.md#put_state_key) | **PUT** /api/v2/apps/{appUuid}/installation/state/{key} | Put a single state key
[**revoke_connection**](AppInstallationRuntimeApi.md#revoke_connection) | **DELETE** /api/v2/apps/{appUuid}/installation/connections/{providerOrConnectionId} | Revoke external OAuth connection tokens by connection id or provider name
[**save_user_settings**](AppInstallationRuntimeApi.md#save_user_settings) | **PUT** /api/v2/apps/{appUuid}/installation/settings/user | Save USER-scoped installation settings for the current user
[**start_o_auth**](AppInstallationRuntimeApi.md#start_o_auth) | **POST** /api/v2/apps/{appUuid}/installation/oauth/{provider}/start | Start external OAuth authorize (returns provider authorize URL)


# **delete_secret**
> DeleteResponseVoid delete_secret(app_uuid, name)

Delete an encrypted secret

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.delete_response_void import DeleteResponseVoid
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    name = 'name_example' # str | 

    try:
        # Delete an encrypted secret
        api_response = api_instance.delete_secret(app_uuid, name)
        print("The response of AppInstallationRuntimeApi->delete_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->delete_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**DeleteResponseVoid**](DeleteResponseVoid.md)

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

# **delete_state_key**
> DeleteResponse delete_state_key(app_uuid, key)

Delete a state key

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.delete_response import DeleteResponse
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    key = 'key_example' # str | 

    try:
        # Delete a state key
        api_response = api_instance.delete_state_key(app_uuid, key)
        print("The response of AppInstallationRuntimeApi->delete_state_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->delete_state_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

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

# **enqueue_job**
> ShowResponseMapStringObject enqueue_job(app_uuid, request_body)

Enqueue an async serverless function job

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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Enqueue an async serverless function job
        api_response = api_instance.enqueue_job(app_uuid, request_body)
        print("The response of AppInstallationRuntimeApi->enqueue_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->enqueue_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
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

# **get_job**
> ShowResponseMapStringObject get_job(app_uuid, job_id)

Get async job status

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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        # Get async job status
        api_response = api_instance.get_job(app_uuid, job_id)
        print("The response of AppInstallationRuntimeApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **job_id** | **str**|  | 

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

# **get_state**
> ShowResponseMapStringObject get_state(app_uuid)

Get installation state map

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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # Get installation state map
        api_response = api_instance.get_state(app_uuid)
        print("The response of AppInstallationRuntimeApi->get_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->get_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

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
**200** | State map |  -  |
**403** | Forbidden |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_key**
> ShowResponseObject get_state_key(app_uuid, key)

Get a single state key

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_object import ShowResponseObject
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    key = 'key_example' # str | 

    try:
        # Get a single state key
        api_response = api_instance.get_state_key(app_uuid, key)
        print("The response of AppInstallationRuntimeApi->get_state_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->get_state_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**ShowResponseObject**](ShowResponseObject.md)

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

# **list_connections**
> ShowResponseListAppConnectionStatusDTO list_connections(app_uuid)

List external OAuth connection status

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_app_connection_status_dto import ShowResponseListAppConnectionStatusDTO
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # List external OAuth connection status
        api_response = api_instance.list_connections(app_uuid)
        print("The response of AppInstallationRuntimeApi->list_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->list_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

### Return type

[**ShowResponseListAppConnectionStatusDTO**](ShowResponseListAppConnectionStatusDTO.md)

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

# **list_secrets**
> ShowResponseListString list_secrets(app_uuid)

List secret names (no values)

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_string import ShowResponseListString
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 

    try:
        # List secret names (no values)
        api_response = api_instance.list_secrets(app_uuid)
        print("The response of AppInstallationRuntimeApi->list_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->list_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 

### Return type

[**ShowResponseListString**](ShowResponseListString.md)

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

# **merge_company_settings**
> ShowResponseMapStringObject merge_company_settings(app_uuid, app_setting_field_schema)

Merge COMPANY-scoped installation settings from the app runtime

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_setting_field_schema import AppSettingFieldSchema
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    app_setting_field_schema = [caraer_client.AppSettingFieldSchema()] # List[AppSettingFieldSchema] | 

    try:
        # Merge COMPANY-scoped installation settings from the app runtime
        api_response = api_instance.merge_company_settings(app_uuid, app_setting_field_schema)
        print("The response of AppInstallationRuntimeApi->merge_company_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->merge_company_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **app_setting_field_schema** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md)|  | 

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
**200** | Merged settings map |  -  |
**403** | Forbidden |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_secret**
> SuccessResponseVoid put_secret(app_uuid, name, request_body)

Set an encrypted secret

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_void import SuccessResponseVoid
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    name = 'name_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Set an encrypted secret
        api_response = api_instance.put_secret(app_uuid, name, request_body)
        print("The response of AppInstallationRuntimeApi->put_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->put_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **name** | **str**|  | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

### Return type

[**SuccessResponseVoid**](SuccessResponseVoid.md)

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

# **put_state**
> ShowResponseMapStringObject put_state(app_uuid, request_body)

Replace/merge installation state (shallow merge)

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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Replace/merge installation state (shallow merge)
        api_response = api_instance.put_state(app_uuid, request_body)
        print("The response of AppInstallationRuntimeApi->put_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->put_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
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

# **put_state_key**
> ShowResponseObject put_state_key(app_uuid, key, body)

Put a single state key

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_object import ShowResponseObject
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    key = 'key_example' # str | 
    body = None # object | 

    try:
        # Put a single state key
        api_response = api_instance.put_state_key(app_uuid, key, body)
        print("The response of AppInstallationRuntimeApi->put_state_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->put_state_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **key** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**ShowResponseObject**](ShowResponseObject.md)

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

# **revoke_connection**
> DeleteResponseVoid revoke_connection(app_uuid, provider_or_connection_id)

Revoke external OAuth connection tokens by connection id or provider name

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.delete_response_void import DeleteResponseVoid
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    provider_or_connection_id = 'provider_or_connection_id_example' # str | 

    try:
        # Revoke external OAuth connection tokens by connection id or provider name
        api_response = api_instance.revoke_connection(app_uuid, provider_or_connection_id)
        print("The response of AppInstallationRuntimeApi->revoke_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->revoke_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **provider_or_connection_id** | **str**|  | 

### Return type

[**DeleteResponseVoid**](DeleteResponseVoid.md)

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

# **save_user_settings**
> SuccessResponseVoid save_user_settings(app_uuid, app_setting_field_schema)

Save USER-scoped installation settings for the current user

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_setting_field_schema import AppSettingFieldSchema
from caraer_client.models.success_response_void import SuccessResponseVoid
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    app_setting_field_schema = [caraer_client.AppSettingFieldSchema()] # List[AppSettingFieldSchema] | 

    try:
        # Save USER-scoped installation settings for the current user
        api_response = api_instance.save_user_settings(app_uuid, app_setting_field_schema)
        print("The response of AppInstallationRuntimeApi->save_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->save_user_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **app_setting_field_schema** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md)|  | 

### Return type

[**SuccessResponseVoid**](SuccessResponseVoid.md)

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

# **start_o_auth**
> ShowResponseAppOAuthStartResponseDTO start_o_auth(app_uuid, provider, redirect_uri=redirect_uri)

Start external OAuth authorize (returns provider authorize URL)

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_o_auth_start_response_dto import ShowResponseAppOAuthStartResponseDTO
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
    api_instance = caraer_client.AppInstallationRuntimeApi(api_client)
    app_uuid = 'app_uuid_example' # str | 
    provider = 'provider_example' # str | 
    redirect_uri = 'redirect_uri_example' # str |  (optional)

    try:
        # Start external OAuth authorize (returns provider authorize URL)
        api_response = api_instance.start_o_auth(app_uuid, provider, redirect_uri=redirect_uri)
        print("The response of AppInstallationRuntimeApi->start_o_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstallationRuntimeApi->start_o_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**|  | 
 **provider** | **str**|  | 
 **redirect_uri** | **str**|  | [optional] 

### Return type

[**ShowResponseAppOAuthStartResponseDTO**](ShowResponseAppOAuthStartResponseDTO.md)

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

