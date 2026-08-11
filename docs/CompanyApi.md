# caraer_client.CompanyApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company**](CompanyApi.md#create_company) | **POST** /api/v2/company/ | Create a new company
[**get_company**](CompanyApi.md#get_company) | **GET** /api/v2/company/ | Get current company
[**get_company_by_uuid**](CompanyApi.md#get_company_by_uuid) | **GET** /api/v2/company/{uuid} | Get company by UUID
[**get_digital_identity**](CompanyApi.md#get_digital_identity) | **GET** /api/v2/company/digital-identity | Get digital identity
[**get_suite_dashboard**](CompanyApi.md#get_suite_dashboard) | **GET** /api/v2/company/suite-dashboards/{suiteName} | Get suite dashboard
[**get_suite_dashboards**](CompanyApi.md#get_suite_dashboards) | **GET** /api/v2/company/suite-dashboards | List suite dashboards
[**get_website_settings**](CompanyApi.md#get_website_settings) | **GET** /api/v2/company/website-settings | Get website settings
[**resume_webhook_dispatch**](CompanyApi.md#resume_webhook_dispatch) | **POST** /api/v2/company/{companyUuid}/webhooks/resume | Resume webhook dispatch
[**update_company**](CompanyApi.md#update_company) | **PUT** /api/v2/company/{uuid} | Update company
[**update_digital_identity**](CompanyApi.md#update_digital_identity) | **PUT** /api/v2/company/digital-identity | Update digital identity
[**update_suite_dashboard**](CompanyApi.md#update_suite_dashboard) | **PUT** /api/v2/company/suite-dashboards/{suiteName} | Update suite dashboard
[**update_website_settings**](CompanyApi.md#update_website_settings) | **PUT** /api/v2/company/website-settings | Update website settings
[**upload_font**](CompanyApi.md#upload_font) | **POST** /api/v2/company/uploadFont | Upload a font file


# **create_company**
> SuccessResponse create_company(create_company_request)

Create a new company

Creates a new company based on the provided request data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_company_request import CreateCompanyRequest
from caraer_client.models.success_response import SuccessResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    create_company_request = caraer_client.CreateCompanyRequest() # CreateCompanyRequest | 

    try:
        # Create a new company
        api_response = api_instance.create_company(create_company_request)
        print("The response of CompanyApi->create_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->create_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_company_request** | [**CreateCompanyRequest**](CreateCompanyRequest.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company created successfully |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> ShowResponse get_company()

Get current company

Returns the company currently selected by the logged-in user. Requires TOOLS_COMPANY_SETTINGS_READ scope.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response import ShowResponse
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
    api_instance = caraer_client.CompanyApi(api_client)

    try:
        # Get current company
        api_response = api_instance.get_company()
        print("The response of CompanyApi->get_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_company: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_by_uuid**
> ShowResponse get_company_by_uuid(uuid)

Get company by UUID

Returns a company by its UUID. Requires TOOLS_COMPANY_SETTINGS_READ scope.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response import ShowResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get company by UUID
        api_response = api_instance.get_company_by_uuid(uuid)
        print("The response of CompanyApi->get_company_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_company_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |
**404** | Company not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_digital_identity**
> ShowResponse get_digital_identity()

Get digital identity

Returns the digital identity (branding) for the company currently selected by the logged-in user.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response import ShowResponse
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
    api_instance = caraer_client.CompanyApi(api_client)

    try:
        # Get digital identity
        api_response = api_instance.get_digital_identity()
        print("The response of CompanyApi->get_digital_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_digital_identity: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Digital identity returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suite_dashboard**
> ShowResponse get_suite_dashboard(suite_name)

Get suite dashboard

Returns the home analytics dashboard for a suite. Empty dashboard when none is saved.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response import ShowResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    suite_name = 'suite_name_example' # str | 

    try:
        # Get suite dashboard
        api_response = api_instance.get_suite_dashboard(suite_name)
        print("The response of CompanyApi->get_suite_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_suite_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suite_name** | **str**|  | 

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suite dashboard returned |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suite_dashboards**
> ShowResponse get_suite_dashboards()

List suite dashboards

Returns all home analytics dashboards keyed by suite name for the selected company.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response import ShowResponse
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
    api_instance = caraer_client.CompanyApi(api_client)

    try:
        # List suite dashboards
        api_response = api_instance.get_suite_dashboards()
        print("The response of CompanyApi->get_suite_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_suite_dashboards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suite dashboards returned |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_settings**
> ShowResponse get_website_settings()

Get website settings

Returns the website settings for the company currently selected by the logged-in user.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response import ShowResponse
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
    api_instance = caraer_client.CompanyApi(api_client)

    try:
        # Get website settings
        api_response = api_instance.get_website_settings()
        print("The response of CompanyApi->get_website_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_website_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website settings returned successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_webhook_dispatch**
> SuccessResponse resume_webhook_dispatch(company_uuid)

Resume webhook dispatch

Clears the per-company webhook circuit breaker so outbound deliveries resume immediately.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response import SuccessResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    company_uuid = 'company_uuid_example' # str | 

    try:
        # Resume webhook dispatch
        api_response = api_instance.resume_webhook_dispatch(company_uuid)
        print("The response of CompanyApi->resume_webhook_dispatch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->resume_webhook_dispatch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Circuit breaker cleared |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company**
> UpdateResponse update_company(uuid, company_dto)

Update company

Updates a company by UUID. Request body should contain the company fields to update.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.company_dto import CompanyDTO
from caraer_client.models.update_response import UpdateResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    uuid = 'uuid_example' # str | 
    company_dto = caraer_client.CompanyDTO() # CompanyDTO | 

    try:
        # Update company
        api_response = api_instance.update_company(uuid, company_dto)
        print("The response of CompanyApi->update_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->update_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **company_dto** | [**CompanyDTO**](CompanyDTO.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company updated successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |
**404** | Company not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_digital_identity**
> UpdateResponse update_digital_identity(digital_identity_dto)

Update digital identity

Updates the digital identity (branding) for the company currently selected by the logged-in user.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.digital_identity_dto import DigitalIdentityDTO
from caraer_client.models.update_response import UpdateResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    digital_identity_dto = caraer_client.DigitalIdentityDTO() # DigitalIdentityDTO | 

    try:
        # Update digital identity
        api_response = api_instance.update_digital_identity(digital_identity_dto)
        print("The response of CompanyApi->update_digital_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->update_digital_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_identity_dto** | [**DigitalIdentityDTO**](DigitalIdentityDTO.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Digital identity updated successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |
**404** | Digital identity not found for company |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_suite_dashboard**
> UpdateResponse update_suite_dashboard(suite_name, analytics_dashboard_config)

Update suite dashboard

Creates or replaces the home analytics dashboard for a suite.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.analytics_dashboard_config import AnalyticsDashboardConfig
from caraer_client.models.update_response import UpdateResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    suite_name = 'suite_name_example' # str | 
    analytics_dashboard_config = caraer_client.AnalyticsDashboardConfig() # AnalyticsDashboardConfig | 

    try:
        # Update suite dashboard
        api_response = api_instance.update_suite_dashboard(suite_name, analytics_dashboard_config)
        print("The response of CompanyApi->update_suite_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->update_suite_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suite_name** | **str**|  | 
 **analytics_dashboard_config** | [**AnalyticsDashboardConfig**](AnalyticsDashboardConfig.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suite dashboard saved |  -  |
**400** | Invalid dashboard config |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_settings**
> UpdateResponse update_website_settings(website_settings_dto)

Update website settings

Updates the website settings for the company currently selected by the logged-in user.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.update_response import UpdateResponse
from caraer_client.models.website_settings_dto import WebsiteSettingsDTO
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
    api_instance = caraer_client.CompanyApi(api_client)
    website_settings_dto = caraer_client.WebsiteSettingsDTO() # WebsiteSettingsDTO | 

    try:
        # Update website settings
        api_response = api_instance.update_website_settings(website_settings_dto)
        print("The response of CompanyApi->update_website_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->update_website_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_settings_dto** | [**WebsiteSettingsDTO**](WebsiteSettingsDTO.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website settings updated successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |
**404** | Website settings not found for company |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_font**
> SuccessResponse upload_font(file)

Upload a font file

Uploads a font file to S3 storage and returns the public URL.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response import SuccessResponse
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
    api_instance = caraer_client.CompanyApi(api_client)
    file = None # bytes | 

    try:
        # Upload a font file
        api_response = api_instance.upload_font(file)
        print("The response of CompanyApi->upload_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->upload_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Font uploaded successfully |  -  |
**400** | Invalid file provided |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

