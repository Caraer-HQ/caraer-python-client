# caraer_client.CMSV2TransferApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach**](CMSV2TransferApi.md#attach) | **POST** /api/v2/company/{companyUuid}/cms-transfer/attach | Attach a manually created caraer-web project
[**cutover**](CMSV2TransferApi.md#cutover) | **POST** /api/v2/company/{companyUuid}/cms-transfer/cutover | Switch the live site to CMS v2: schema, caraer-web repo, and hostname
[**rollback**](CMSV2TransferApi.md#rollback) | **POST** /api/v2/company/{companyUuid}/cms-transfer/rollback | Restore the live hostname to the stored v1 project
[**status**](CMSV2TransferApi.md#status) | **GET** /api/v2/company/{companyUuid}/cms-transfer | Transfer status for one company


# **attach**
> ShowResponseCompanyDTO attach(company_uuid, request_body)

Attach a manually created caraer-web project

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_company_dto import ShowResponseCompanyDTO
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
    api_instance = caraer_client.CMSV2TransferApi(api_client)
    company_uuid = 'company_uuid_example' # str | 
    request_body = {'key': 'request_body_example'} # Dict[str, str] | 

    try:
        # Attach a manually created caraer-web project
        api_response = api_instance.attach(company_uuid, request_body)
        print("The response of CMSV2TransferApi->attach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2TransferApi->attach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 
 **request_body** | [**Dict[str, str]**](str.md)|  | 

### Return type

[**ShowResponseCompanyDTO**](ShowResponseCompanyDTO.md)

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

# **cutover**
> ShowResponseCompanyDTO cutover(company_uuid)

Switch the live site to CMS v2: schema, caraer-web repo, and hostname

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_company_dto import ShowResponseCompanyDTO
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
    api_instance = caraer_client.CMSV2TransferApi(api_client)
    company_uuid = 'company_uuid_example' # str | 

    try:
        # Switch the live site to CMS v2: schema, caraer-web repo, and hostname
        api_response = api_instance.cutover(company_uuid)
        print("The response of CMSV2TransferApi->cutover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2TransferApi->cutover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 

### Return type

[**ShowResponseCompanyDTO**](ShowResponseCompanyDTO.md)

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

# **rollback**
> ShowResponseCompanyDTO rollback(company_uuid)

Restore the live hostname to the stored v1 project

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_company_dto import ShowResponseCompanyDTO
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
    api_instance = caraer_client.CMSV2TransferApi(api_client)
    company_uuid = 'company_uuid_example' # str | 

    try:
        # Restore the live hostname to the stored v1 project
        api_response = api_instance.rollback(company_uuid)
        print("The response of CMSV2TransferApi->rollback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2TransferApi->rollback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 

### Return type

[**ShowResponseCompanyDTO**](ShowResponseCompanyDTO.md)

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

# **status**
> ShowResponseMapStringObject status(company_uuid)

Transfer status for one company

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
    api_instance = caraer_client.CMSV2TransferApi(api_client)
    company_uuid = 'company_uuid_example' # str | 

    try:
        # Transfer status for one company
        api_response = api_instance.status(company_uuid)
        print("The response of CMSV2TransferApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMSV2TransferApi->status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 

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

