# caraer_client.WebpagesApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_template_webpage_editing_session**](WebpagesApi.md#claim_template_webpage_editing_session) | **POST** /api/v2/webpages/template/{objectName}/{environment}/editing-session | Claim a template webpage editing session
[**claim_webpage_editing_session**](WebpagesApi.md#claim_webpage_editing_session) | **POST** /api/v2/webpages/{uuid}/editing-session | Claim a webpage editing session
[**copy_property_to_environments**](WebpagesApi.md#copy_property_to_environments) | **POST** /api/v2/webpages/environments/properties | Copy properties to environments
[**copy_template_webpage**](WebpagesApi.md#copy_template_webpage) | **POST** /api/v2/webpages/template/{objectName}/copy/{fromEnvironment}/{toEnvironment} | Copy a template webpage from one environment to another
[**copy_webpage**](WebpagesApi.md#copy_webpage) | **POST** /api/v2/webpages/{uuid}/copy/{fromEnvironment}/{toEnvironment} | Copy a webpage from one environment to another
[**create_environments**](WebpagesApi.md#create_environments) | **POST** /api/v2/webpages/environments | Create an environment
[**create_or_update_template_webpage**](WebpagesApi.md#create_or_update_template_webpage) | **POST** /api/v2/webpages/template/{objectName}/{environment} | Create or update template webpage
[**create_signed_url**](WebpagesApi.md#create_signed_url) | **POST** /api/v2/webpages/{uuid}/protection/signed-url | Generate signed URL for protected webpage
[**create_webpage**](WebpagesApi.md#create_webpage) | **POST** /api/v2/webpages/ | Create a new webpage
[**delete_environment**](WebpagesApi.md#delete_environment) | **DELETE** /api/v2/webpages/environments/{environment} | Delete an environment
[**get_all_slugs**](WebpagesApi.md#get_all_slugs) | **GET** /api/v2/webpages/public/getSlugs | Get all public webpage slugs
[**get_company_settings**](WebpagesApi.md#get_company_settings) | **GET** /api/v2/webpages/public/companySettings | Fetch public company settings
[**get_environments**](WebpagesApi.md#get_environments) | **GET** /api/v2/webpages/environments | Get all environments
[**get_menus**](WebpagesApi.md#get_menus) | **GET** /api/v2/webpages/public/getMenus | Fetch public web menus
[**get_public_custom_footer_module**](WebpagesApi.md#get_public_custom_footer_module) | **GET** /api/v2/webpages/public/module/{moduleUuid} | Fetch public custom footer module
[**get_public_previews**](WebpagesApi.md#get_public_previews) | **POST** /api/v2/webpages/public/previews/{pageUuid}/{componentUuid}/{layout} | Get previews for a public webpage
[**get_public_webpage**](WebpagesApi.md#get_public_webpage) | **GET** /api/v2/webpages/public/{rootSlug}/{slug} | Get a public webpage by slug
[**get_public_webpage_by_uuid**](WebpagesApi.md#get_public_webpage_by_uuid) | **GET** /api/v2/webpages/public/uuid/{uuid} | Get a public webpage by UUID
[**get_public_webpage_protection**](WebpagesApi.md#get_public_webpage_protection) | **GET** /api/v2/webpages/public/uuid/{uuid}/protection | Get webpage protection metadata
[**get_template_webpage**](WebpagesApi.md#get_template_webpage) | **GET** /api/v2/webpages/template/{objectName}/{environment} | Get template webpage
[**get_template_webpage_editing_status**](WebpagesApi.md#get_template_webpage_editing_status) | **GET** /api/v2/webpages/template/{objectName}/{environment}/editing-status | Check if a template webpage is being edited
[**get_webpage**](WebpagesApi.md#get_webpage) | **GET** /api/v2/webpages/{uuid} | Get webpage details
[**get_webpage_editing_status**](WebpagesApi.md#get_webpage_editing_status) | **GET** /api/v2/webpages/{uuid}/editing-status | Check if a webpage is being edited
[**get_webpage_picker_pages**](WebpagesApi.md#get_webpage_picker_pages) | **GET** /api/v2/webpages/picker/pages | List webpages for picker dropdowns
[**list_protection_grants**](WebpagesApi.md#list_protection_grants) | **GET** /api/v2/webpages/{uuid}/protection/grants | List signed URL grants for a webpage
[**publish_webpage**](WebpagesApi.md#publish_webpage) | **PUT** /api/v2/webpages/{uuid}/publish | Publish a webpage
[**release_template_webpage_editing_session**](WebpagesApi.md#release_template_webpage_editing_session) | **DELETE** /api/v2/webpages/template/{objectName}/{environment}/editing-session | Release a template webpage editing session
[**release_webpage_editing_session**](WebpagesApi.md#release_webpage_editing_session) | **DELETE** /api/v2/webpages/{uuid}/editing-session | Release a webpage editing session
[**revoke_protection_grant**](WebpagesApi.md#revoke_protection_grant) | **DELETE** /api/v2/webpages/{uuid}/protection/grants/{grantUuid} | Revoke a signed URL grant
[**unlock_public_webpage**](WebpagesApi.md#unlock_public_webpage) | **POST** /api/v2/webpages/public/uuid/{uuid}/unlock | Unlock password-protected webpage
[**unpublish_webpage**](WebpagesApi.md#unpublish_webpage) | **PUT** /api/v2/webpages/{uuid}/unpublish | Unpublish a webpage
[**update_webpage**](WebpagesApi.md#update_webpage) | **PUT** /api/v2/webpages/{uuid} | Update a webpage
[**upload_file**](WebpagesApi.md#upload_file) | **POST** /api/v2/webpages/{uuid}/uploadFile | Upload a file for a webpage
[**upload_file1**](WebpagesApi.md#upload_file1) | **POST** /api/v2/webpages/uploadFile | Upload a file


# **claim_template_webpage_editing_session**
> WebpageEditingStatusDTO claim_template_webpage_editing_session(object_name, environment)

Claim a template webpage editing session

Registers the current user as editing the template webpage so other users are blocked from opening the builder.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.webpage_editing_status_dto import WebpageEditingStatusDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    object_name = 'object_name_example' # str | 
    environment = 'environment_example' # str | 

    try:
        # Claim a template webpage editing session
        api_response = api_instance.claim_template_webpage_editing_session(object_name, environment)
        print("The response of WebpagesApi->claim_template_webpage_editing_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->claim_template_webpage_editing_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **environment** | **str**|  | 

### Return type

[**WebpageEditingStatusDTO**](WebpageEditingStatusDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Editing session claimed or blocked |  -  |
**404** | Template webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_webpage_editing_session**
> WebpageEditingStatusDTO claim_webpage_editing_session(uuid, environment=environment)

Claim a webpage editing session

Registers the current user as editing this webpage so other users are blocked from opening the builder.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.webpage_editing_status_dto import WebpageEditingStatusDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    environment = 'staging' # str |  (optional) (default to 'staging')

    try:
        # Claim a webpage editing session
        api_response = api_instance.claim_webpage_editing_session(uuid, environment=environment)
        print("The response of WebpagesApi->claim_webpage_editing_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->claim_webpage_editing_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]

### Return type

[**WebpageEditingStatusDTO**](WebpageEditingStatusDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Editing session claimed |  -  |
**403** | Missing write access on webpage fields for this environment |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_property_to_environments**
> ShowResponse copy_property_to_environments(copy_property_to_environments_request)

Copy properties to environments

Copies selected properties for the chosen environments (e.g. production_title → german_production_title).

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.copy_property_to_environments_request import CopyPropertyToEnvironmentsRequest
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
    api_instance = caraer_client.WebpagesApi(api_client)
    copy_property_to_environments_request = caraer_client.CopyPropertyToEnvironmentsRequest() # CopyPropertyToEnvironmentsRequest | 

    try:
        # Copy properties to environments
        api_response = api_instance.copy_property_to_environments(copy_property_to_environments_request)
        print("The response of WebpagesApi->copy_property_to_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->copy_property_to_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_property_to_environments_request** | [**CopyPropertyToEnvironmentsRequest**](CopyPropertyToEnvironmentsRequest.md)|  | 

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment properties copied successfully |  -  |
**400** | Invalid input data |  -  |
**404** | Object or property not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_template_webpage**
> CreateResponse copy_template_webpage(object_name, from_environment, to_environment)

Copy a template webpage from one environment to another

Copies a template webpage by object name from one environment to another. Returns a CreateResponse containing the copied template webpage as a TemplateWebpageDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
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
    api_instance = caraer_client.WebpagesApi(api_client)
    object_name = 'object_name_example' # str | 
    from_environment = 'from_environment_example' # str | 
    to_environment = 'to_environment_example' # str | 

    try:
        # Copy a template webpage from one environment to another
        api_response = api_instance.copy_template_webpage(object_name, from_environment, to_environment)
        print("The response of WebpagesApi->copy_template_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->copy_template_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **from_environment** | **str**|  | 
 **to_environment** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template webpage copied successfully |  -  |
**404** | Template webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_webpage**
> CreateResponse copy_webpage(uuid, from_environment, to_environment)

Copy a webpage from one environment to another

Copies a webpage by its UUID from one environment to another. Returns a CreateResponse containing the copied webpage as a WebpageDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    from_environment = 'from_environment_example' # str | 
    to_environment = 'to_environment_example' # str | 

    try:
        # Copy a webpage from one environment to another
        api_response = api_instance.copy_webpage(uuid, from_environment, to_environment)
        print("The response of WebpagesApi->copy_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->copy_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **from_environment** | **str**|  | 
 **to_environment** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webpage copied successfully |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_environments**
> ShowResponse create_environments(create_or_update_environment_request)

Create an environment

Creates an environment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_or_update_environment_request import CreateOrUpdateEnvironmentRequest
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
    api_instance = caraer_client.WebpagesApi(api_client)
    create_or_update_environment_request = caraer_client.CreateOrUpdateEnvironmentRequest() # CreateOrUpdateEnvironmentRequest | 

    try:
        # Create an environment
        api_response = api_instance.create_environments(create_or_update_environment_request)
        print("The response of WebpagesApi->create_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->create_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_update_environment_request** | [**CreateOrUpdateEnvironmentRequest**](CreateOrUpdateEnvironmentRequest.md)|  | 

### Return type

[**ShowResponse**](ShowResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environments created or updated successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_template_webpage**
> UpdateResponse create_or_update_template_webpage(object_name, environment, template_webpage_dto)

Create or update template webpage

Creates a new or updates an existing template webpage for the specified object. An event is published after the template is changed. Returns an UpdateResponse or CreateResponse with the template webpage details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.template_webpage_dto import TemplateWebpageDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    object_name = 'object_name_example' # str | 
    environment = 'environment_example' # str | 
    template_webpage_dto = caraer_client.TemplateWebpageDTO() # TemplateWebpageDTO | Template webpage details

    try:
        # Create or update template webpage
        api_response = api_instance.create_or_update_template_webpage(object_name, environment, template_webpage_dto)
        print("The response of WebpagesApi->create_or_update_template_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->create_or_update_template_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **environment** | **str**|  | 
 **template_webpage_dto** | [**TemplateWebpageDTO**](TemplateWebpageDTO.md)| Template webpage details | 

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
**200** | Template webpage updated successfully |  -  |
**201** | Template webpage created successfully |  -  |
**404** | Template webpage not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_signed_url**
> CreateResponseSignedUrlResultDTO create_signed_url(uuid, environment=environment, create_signed_url_request=create_signed_url_request)

Generate signed URL for protected webpage

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response_signed_url_result_dto import CreateResponseSignedUrlResultDTO
from caraer_client.models.create_signed_url_request import CreateSignedUrlRequest
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    environment = 'staging' # str |  (optional) (default to 'staging')
    create_signed_url_request = caraer_client.CreateSignedUrlRequest() # CreateSignedUrlRequest |  (optional)

    try:
        # Generate signed URL for protected webpage
        api_response = api_instance.create_signed_url(uuid, environment=environment, create_signed_url_request=create_signed_url_request)
        print("The response of WebpagesApi->create_signed_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->create_signed_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]
 **create_signed_url_request** | [**CreateSignedUrlRequest**](CreateSignedUrlRequest.md)|  | [optional] 

### Return type

[**CreateResponseSignedUrlResultDTO**](CreateResponseSignedUrlResultDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webpage**
> CreateResponse create_webpage(webpage_dto, environment=environment)

Create a new webpage

Creates a new webpage using the provided webpage details. Returns a CreateResponse containing the newly created webpage as a WebpageDTO. Validation: Webpage fields are validated according to the Webpage validation rules. Required fields and format constraints are enforced.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.webpage_dto import WebpageDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    webpage_dto = caraer_client.WebpageDTO() # WebpageDTO | Webpage details
    environment = 'staging' # str |  (optional) (default to 'staging')

    try:
        # Create a new webpage
        api_response = api_instance.create_webpage(webpage_dto, environment=environment)
        print("The response of WebpagesApi->create_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->create_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webpage_dto** | [**WebpageDTO**](WebpageDTO.md)| Webpage details | 
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webpage created successfully |  -  |
**400** | Invalid input data |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment**
> ShowResponse delete_environment(environment)

Delete an environment

Soft deletes an environment.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    environment = 'environment_example' # str | 

    try:
        # Delete an environment
        api_response = api_instance.delete_environment(environment)
        print("The response of WebpagesApi->delete_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->delete_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  | 

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
**200** | Environment deleted successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_slugs**
> PaginationResponse get_all_slugs(x_caraer_subdomain, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)

Get all public webpage slugs

Retrieves a list of all webpage slugs for the public site. Returns a PaginationResponse containing WebpageMapItemDTO objects.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_response import PaginationResponse
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')

    try:
        # Get all public webpage slugs
        api_response = api_instance.get_all_slugs(x_caraer_subdomain, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)
        print("The response of WebpagesApi->get_all_slugs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_all_slugs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]

### Return type

[**PaginationResponse**](PaginationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Slugs retrieved successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_settings**
> SimplePublicCompanyDTO get_company_settings(x_caraer_subdomain, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)

Fetch public company settings

Retrieves the public company configuration for the given subdomain. Returns a ShowResponse containing PublicCompanyDTO details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.simple_public_company_dto import SimplePublicCompanyDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')

    try:
        # Fetch public company settings
        api_response = api_instance.get_company_settings(x_caraer_subdomain, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)
        print("The response of WebpagesApi->get_company_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_company_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]

### Return type

[**SimplePublicCompanyDTO**](SimplePublicCompanyDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company settings retrieved successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments**
> ShowResponse get_environments()

Get all environments

Retrieves a list of all environments.

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
    api_instance = caraer_client.WebpagesApi(api_client)

    try:
        # Get all environments
        api_response = api_instance.get_environments()
        print("The response of WebpagesApi->get_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_environments: %s\n" % e)
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
**200** | Environments retrieved successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_menus**
> PaginationResponse get_menus(x_caraer_subdomain, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)

Fetch public web menus

Retrieves a list of web menus for the public site. Returns a PaginationResponse containing WebMenuDTO objects.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_response import PaginationResponse
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')

    try:
        # Fetch public web menus
        api_response = api_instance.get_menus(x_caraer_subdomain, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)
        print("The response of WebpagesApi->get_menus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_menus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]

### Return type

[**PaginationResponse**](PaginationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Menus retrieved successfully |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_custom_footer_module**
> ShowResponse get_public_custom_footer_module(x_caraer_subdomain, module_uuid)

Fetch public custom footer module

Returns the PageContent tree for the module configured as custom footer when enabled. Requires X-Caraer-Subdomain; only the UUID configured in website settings is accessible.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    module_uuid = 'module_uuid_example' # str | 

    try:
        # Fetch public custom footer module
        api_response = api_instance.get_public_custom_footer_module(x_caraer_subdomain, module_uuid)
        print("The response of WebpagesApi->get_public_custom_footer_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_public_custom_footer_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **module_uuid** | **str**|  | 

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
**200** | Module retrieved successfully |  -  |
**404** | Module not found or not exposed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_previews**
> PaginationResponsePreviewDTO get_public_previews(x_caraer_subdomain, page_uuid, component_uuid, layout, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment, authorization=authorization, x_caraer_webpage_access=x_caraer_webpage_access, access=access, token=token)

Get previews for a public webpage

Retrieves a list of previews for a public webpage identified by its UUID. Returns a PaginationResponse containing PreviewDTO objects.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_response_preview_dto import PaginationResponsePreviewDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    page_uuid = 'page_uuid_example' # str | 
    component_uuid = 'component_uuid_example' # str | 
    layout = 'layout_example' # str | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')
    authorization = 'authorization_example' # str |  (optional)
    x_caraer_webpage_access = 'x_caraer_webpage_access_example' # str |  (optional)
    access = 'access_example' # str |  (optional)
    token = 'token_example' # str |  (optional)

    try:
        # Get previews for a public webpage
        api_response = api_instance.get_public_previews(x_caraer_subdomain, page_uuid, component_uuid, layout, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment, authorization=authorization, x_caraer_webpage_access=x_caraer_webpage_access, access=access, token=token)
        print("The response of WebpagesApi->get_public_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_public_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **page_uuid** | **str**|  | 
 **component_uuid** | **str**|  | 
 **layout** | **str**|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **authorization** | **str**|  | [optional] 
 **x_caraer_webpage_access** | **str**|  | [optional] 
 **access** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 

### Return type

[**PaginationResponsePreviewDTO**](PaginationResponsePreviewDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_webpage**
> WebpageDTO get_public_webpage(x_caraer_subdomain, root_slug, slug, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment, authorization=authorization, x_caraer_webpage_access=x_caraer_webpage_access, access=access, token=token)

Get a public webpage by slug

Retrieves a published webpage based on the provided root slug and slug. Returns a ShowResponse containing WebpageDTO data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.webpage_dto import WebpageDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    root_slug = 'root_slug_example' # str | 
    slug = 'slug_example' # str | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')
    authorization = 'authorization_example' # str |  (optional)
    x_caraer_webpage_access = 'x_caraer_webpage_access_example' # str |  (optional)
    access = 'access_example' # str |  (optional)
    token = 'token_example' # str |  (optional)

    try:
        # Get a public webpage by slug
        api_response = api_instance.get_public_webpage(x_caraer_subdomain, root_slug, slug, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment, authorization=authorization, x_caraer_webpage_access=x_caraer_webpage_access, access=access, token=token)
        print("The response of WebpagesApi->get_public_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_public_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **root_slug** | **str**|  | 
 **slug** | **str**|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **authorization** | **str**|  | [optional] 
 **x_caraer_webpage_access** | **str**|  | [optional] 
 **access** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 

### Return type

[**WebpageDTO**](WebpageDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webpage retrieved successfully |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_webpage_by_uuid**
> WebpageDTO get_public_webpage_by_uuid(x_caraer_subdomain, uuid, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment, authorization=authorization, x_caraer_webpage_access=x_caraer_webpage_access, access=access, token=token)

Get a public webpage by UUID

Retrieves a published webpage based on its UUID. Returns a ShowResponse containing WebpageDTO data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.webpage_dto import WebpageDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    uuid = 'uuid_example' # str | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')
    authorization = 'authorization_example' # str |  (optional)
    x_caraer_webpage_access = 'x_caraer_webpage_access_example' # str |  (optional)
    access = 'access_example' # str |  (optional)
    token = 'token_example' # str |  (optional)

    try:
        # Get a public webpage by UUID
        api_response = api_instance.get_public_webpage_by_uuid(x_caraer_subdomain, uuid, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment, authorization=authorization, x_caraer_webpage_access=x_caraer_webpage_access, access=access, token=token)
        print("The response of WebpagesApi->get_public_webpage_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_public_webpage_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **uuid** | **str**|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **authorization** | **str**|  | [optional] 
 **x_caraer_webpage_access** | **str**|  | [optional] 
 **access** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 

### Return type

[**WebpageDTO**](WebpageDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webpage retrieved successfully |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_webpage_protection**
> ShowResponseWebpageProtectionInfoDTO get_public_webpage_protection(x_caraer_subdomain, uuid, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)

Get webpage protection metadata

Returns protection requirements without page content.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_webpage_protection_info_dto import ShowResponseWebpageProtectionInfoDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    uuid = 'uuid_example' # str | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')

    try:
        # Get webpage protection metadata
        api_response = api_instance.get_public_webpage_protection(x_caraer_subdomain, uuid, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)
        print("The response of WebpagesApi->get_public_webpage_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_public_webpage_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **uuid** | **str**|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]

### Return type

[**ShowResponseWebpageProtectionInfoDTO**](ShowResponseWebpageProtectionInfoDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_webpage**
> ShowResponse get_template_webpage(object_name, environment)

Get template webpage

Retrieves the template webpage for the given object name by querying the TemplateWebpage associated with it. Returns a ShowResponse containing TemplateWebpageDTO data.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    object_name = 'object_name_example' # str | 
    environment = 'environment_example' # str | 

    try:
        # Get template webpage
        api_response = api_instance.get_template_webpage(object_name, environment)
        print("The response of WebpagesApi->get_template_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_template_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **environment** | **str**|  | 

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
**200** | Template webpage retrieved successfully |  -  |
**404** | Template webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_webpage_editing_status**
> WebpageEditingStatusDTO get_template_webpage_editing_status(object_name, environment)

Check if a template webpage is being edited

Returns whether another user is actively editing the template webpage for the given object and environment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.webpage_editing_status_dto import WebpageEditingStatusDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    object_name = 'object_name_example' # str | 
    environment = 'environment_example' # str | 

    try:
        # Check if a template webpage is being edited
        api_response = api_instance.get_template_webpage_editing_status(object_name, environment)
        print("The response of WebpagesApi->get_template_webpage_editing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_template_webpage_editing_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **environment** | **str**|  | 

### Return type

[**WebpageEditingStatusDTO**](WebpageEditingStatusDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Editing status retrieved successfully |  -  |
**404** | Template webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webpage**
> WebpageDTO get_webpage(uuid, smartened=smartened, environment=environment)

Get webpage details

Retrieves detailed information for a webpage identified by its UUID. Optionally, the webpage title is 'smartened' if the smartened parameter is true.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.webpage_dto import WebpageDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    smartened = False # bool |  (optional) (default to False)
    environment = 'staging' # str |  (optional) (default to 'staging')

    try:
        # Get webpage details
        api_response = api_instance.get_webpage(uuid, smartened=smartened, environment=environment)
        print("The response of WebpagesApi->get_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **smartened** | **bool**|  | [optional] [default to False]
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]

### Return type

[**WebpageDTO**](WebpageDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webpage retrieved successfully |  -  |
**403** | Missing read access on one or more webpage fields for this environment |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webpage_editing_status**
> WebpageEditingStatusDTO get_webpage_editing_status(uuid, environment=environment)

Check if a webpage is being edited

Returns whether another user is actively editing this webpage (via an open builder session or collaborative WebSocket connection).

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.webpage_editing_status_dto import WebpageEditingStatusDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    environment = 'staging' # str |  (optional) (default to 'staging')

    try:
        # Check if a webpage is being edited
        api_response = api_instance.get_webpage_editing_status(uuid, environment=environment)
        print("The response of WebpagesApi->get_webpage_editing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_webpage_editing_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]

### Return type

[**WebpageEditingStatusDTO**](WebpageEditingStatusDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Editing status retrieved successfully |  -  |
**403** | Missing read access on webpage fields for this environment |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webpage_picker_pages**
> ShowResponse get_webpage_picker_pages(environment=environment, published_only=published_only, exclude_template_related=exclude_template_related)

List webpages for picker dropdowns

Returns uuid and title for all webpage records across objects with a Page trait. Supports optional filters for published pages and excluding template-related pages.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    environment = 'production' # str | Environment to resolve webpage properties from (e.g. 'production' or 'staging'). (optional) (default to 'production')
    published_only = False # bool | When true, only returns pages that are published in the given environment. (optional) (default to False)
    exclude_template_related = False # bool | When true, excludes pages whose options mark them as related to a template. (optional) (default to False)

    try:
        # List webpages for picker dropdowns
        api_response = api_instance.get_webpage_picker_pages(environment=environment, published_only=published_only, exclude_template_related=exclude_template_related)
        print("The response of WebpagesApi->get_webpage_picker_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->get_webpage_picker_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Environment to resolve webpage properties from (e.g. &#39;production&#39; or &#39;staging&#39;). | [optional] [default to &#39;production&#39;]
 **published_only** | **bool**| When true, only returns pages that are published in the given environment. | [optional] [default to False]
 **exclude_template_related** | **bool**| When true, excludes pages whose options mark them as related to a template. | [optional] [default to False]

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
**200** | Webpages retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_protection_grants**
> PaginationResponseWebpageAccessGrantDTO list_protection_grants(uuid, environment=environment)

List signed URL grants for a webpage

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_response_webpage_access_grant_dto import PaginationResponseWebpageAccessGrantDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    environment = 'staging' # str |  (optional) (default to 'staging')

    try:
        # List signed URL grants for a webpage
        api_response = api_instance.list_protection_grants(uuid, environment=environment)
        print("The response of WebpagesApi->list_protection_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->list_protection_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]

### Return type

[**PaginationResponseWebpageAccessGrantDTO**](PaginationResponseWebpageAccessGrantDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_webpage**
> UpdateResponse publish_webpage(uuid, publish_at=publish_at, environment=environment)

Publish a webpage

Publishes a webpage by its UUID. Optionally, a publish_at timestamp (in seconds) may be provided. Returns an UpdateResponse containing the published webpage details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    publish_at = 'publish_at_example' # str |  (optional)
    environment = 'production' # str |  (optional) (default to 'production')

    try:
        # Publish a webpage
        api_response = api_instance.publish_webpage(uuid, publish_at=publish_at, environment=environment)
        print("The response of WebpagesApi->publish_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->publish_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **publish_at** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] [default to &#39;production&#39;]

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webpage published successfully |  -  |
**400** | Webpage failed publish validation |  -  |
**403** | Missing read or write access on webpage property fields for this environment |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_template_webpage_editing_session**
> ShowResponse release_template_webpage_editing_session(object_name, environment)

Release a template webpage editing session

Releases the editing session held by the current user for this template webpage.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    object_name = 'object_name_example' # str | 
    environment = 'environment_example' # str | 

    try:
        # Release a template webpage editing session
        api_response = api_instance.release_template_webpage_editing_session(object_name, environment)
        print("The response of WebpagesApi->release_template_webpage_editing_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->release_template_webpage_editing_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_name** | **str**|  | 
 **environment** | **str**|  | 

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
**200** | Editing session released |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_webpage_editing_session**
> ShowResponse release_webpage_editing_session(uuid)

Release a webpage editing session

Releases the editing session held by the current user for this webpage.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Release a webpage editing session
        api_response = api_instance.release_webpage_editing_session(uuid)
        print("The response of WebpagesApi->release_webpage_editing_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->release_webpage_editing_session: %s\n" % e)
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
**200** | Editing session released |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_protection_grant**
> SuccessResponseString revoke_protection_grant(uuid, grant_uuid, environment=environment)

Revoke a signed URL grant

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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    grant_uuid = 'grant_uuid_example' # str | 
    environment = 'staging' # str |  (optional) (default to 'staging')

    try:
        # Revoke a signed URL grant
        api_response = api_instance.revoke_protection_grant(uuid, grant_uuid, environment=environment)
        print("The response of WebpagesApi->revoke_protection_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->revoke_protection_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **grant_uuid** | **str**|  | 
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_public_webpage**
> SuccessResponseString unlock_public_webpage(x_caraer_subdomain, uuid, webpage_unlock_request, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)

Unlock password-protected webpage

Validates password and returns a short-lived access token.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_string import SuccessResponseString
from caraer_client.models.webpage_unlock_request import WebpageUnlockRequest
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
    api_instance = caraer_client.WebpagesApi(api_client)
    x_caraer_subdomain = 'x_caraer_subdomain_example' # str | 
    uuid = 'uuid_example' # str | 
    webpage_unlock_request = caraer_client.WebpageUnlockRequest() # WebpageUnlockRequest | 
    x_caraer_environment = 'production' # str |  (optional) (default to 'production')
    x_caraer_primary_environment = 'production' # str |  (optional) (default to 'production')

    try:
        # Unlock password-protected webpage
        api_response = api_instance.unlock_public_webpage(x_caraer_subdomain, uuid, webpage_unlock_request, x_caraer_environment=x_caraer_environment, x_caraer_primary_environment=x_caraer_primary_environment)
        print("The response of WebpagesApi->unlock_public_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->unlock_public_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_caraer_subdomain** | **str**|  | 
 **uuid** | **str**|  | 
 **webpage_unlock_request** | [**WebpageUnlockRequest**](WebpageUnlockRequest.md)|  | 
 **x_caraer_environment** | **str**|  | [optional] [default to &#39;production&#39;]
 **x_caraer_primary_environment** | **str**|  | [optional] [default to &#39;production&#39;]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_webpage**
> UpdateResponse unpublish_webpage(uuid, unpublish_at=unpublish_at, environment=environment)

Unpublish a webpage

Unpublishes a webpage by its UUID. Optionally, an unpublishAt timestamp (in seconds) may be provided. Returns an UpdateResponse containing the unpublished webpage details.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    unpublish_at = 'unpublish_at_example' # str |  (optional)
    environment = 'production' # str |  (optional) (default to 'production')

    try:
        # Unpublish a webpage
        api_response = api_instance.unpublish_webpage(uuid, unpublish_at=unpublish_at, environment=environment)
        print("The response of WebpagesApi->unpublish_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->unpublish_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **unpublish_at** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] [default to &#39;production&#39;]

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webpage unpublished successfully |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webpage**
> UpdateResponse update_webpage(uuid, webpage_dto, environment=environment)

Update a webpage

Updates an existing webpage identified by its UUID using the provided webpage details. Returns an UpdateResponse containing the updated webpage as a WebpageDTO. Validation: Webpage fields are validated according to the Webpage validation rules. Required fields and format constraints are enforced.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.update_response import UpdateResponse
from caraer_client.models.webpage_dto import WebpageDTO
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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 
    webpage_dto = caraer_client.WebpageDTO() # WebpageDTO | Webpage details
    environment = 'staging' # str |  (optional) (default to 'staging')

    try:
        # Update a webpage
        api_response = api_instance.update_webpage(uuid, webpage_dto, environment=environment)
        print("The response of WebpagesApi->update_webpage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->update_webpage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **webpage_dto** | [**WebpageDTO**](WebpageDTO.md)| Webpage details | 
 **environment** | **str**|  | [optional] [default to &#39;staging&#39;]

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
**200** | Webpage updated successfully |  -  |
**400** | Invalid input data |  -  |
**403** | Missing write access on one or more webpage fields for this environment |  -  |
**404** | Webpage not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> SuccessResponse upload_file(uuid)

Upload a file for a webpage

Uploads a file to S3 storage under the specified webpage's attachments folder, sets the file's ACL to public, and returns the public URL for the file in a SuccessResponse.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Upload a file for a webpage
        api_response = api_instance.upload_file(uuid)
        print("The response of WebpagesApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

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
**200** | File uploaded successfully |  -  |
**400** | Invalid file provided |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file1**
> SuccessResponse upload_file1(file)

Upload a file

Uploads a file to S3 storage and returns the public URL for the file in a SuccessResponse.

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
    api_instance = caraer_client.WebpagesApi(api_client)
    file = None # bytes | 

    try:
        # Upload a file
        api_response = api_instance.upload_file1(file)
        print("The response of WebpagesApi->upload_file1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebpagesApi->upload_file1: %s\n" % e)
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
**200** | File uploaded successfully |  -  |
**400** | Invalid file provided |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

