# caraer_client.ApplicationsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_webhook_for_app**](ApplicationsApi.md#create_app_webhook_for_app) | **POST** /api/v2/apps/{appUuid}/webhooks | Create a webhook for an app (app-scoped path)
[**create_private_app**](ApplicationsApi.md#create_private_app) | **POST** /api/v2/apps/private | Create a private app
[**create_public_app**](ApplicationsApi.md#create_public_app) | **POST** /api/v2/apps/public | Create a public app
[**delete_app_webhook**](ApplicationsApi.md#delete_app_webhook) | **DELETE** /api/v2/apps/{appUuid}/webhooks/{webhookUuid} | Delete a webhook for an app
[**get_app**](ApplicationsApi.md#get_app) | **GET** /api/v2/apps/{uuid} | Retrieve application details by UUID
[**get_app_webhook**](ApplicationsApi.md#get_app_webhook) | **GET** /api/v2/apps/{appUuid}/webhooks/{webhookUuid} | Get a webhook for an app
[**get_app_webhooks**](ApplicationsApi.md#get_app_webhooks) | **POST** /api/v2/apps/{appUuid}/webhooks/index | Retrieve a paginated list of webhooks for an app
[**get_apps**](ApplicationsApi.md#get_apps) | **POST** /api/v2/apps/index | Retrieve a paginated list of applications
[**get_company_information**](ApplicationsApi.md#get_company_information) | **GET** /api/v2/apps/{appUuid}/me | Get current user&#39;s company information
[**get_my_created_apps**](ApplicationsApi.md#get_my_created_apps) | **POST** /api/v2/apps/my/index | Retrieve apps created by the logged-in user&#39;s selected company
[**get_public_app**](ApplicationsApi.md#get_public_app) | **GET** /api/v2/apps/public/{uuid} | Get a public app (creator view)
[**get_runtime_logs**](ApplicationsApi.md#get_runtime_logs) | **GET** /api/v2/apps/{appUuid}/runtime/logs | Get app runtime logs
[**get_webhook_events**](ApplicationsApi.md#get_webhook_events) | **GET** /api/v2/apps/{appUuid}/webhooks/events | Get available webhook record events
[**get_webhook_formats**](ApplicationsApi.md#get_webhook_formats) | **GET** /api/v2/apps/{appUuid}/webhooks/formats | Get available webhook formats
[**get_webhook_property_topics**](ApplicationsApi.md#get_webhook_property_topics) | **GET** /api/v2/apps/{appUuid}/webhooks/property-topics | Get webhook property topic options
[**install_app**](ApplicationsApi.md#install_app) | **POST** /api/v2/apps/{uuid}/install | Install an application
[**list_app_categories**](ApplicationsApi.md#list_app_categories) | **GET** /api/v2/apps/categories | List predefined marketplace app categories
[**load_setting_options**](ApplicationsApi.md#load_setting_options) | **POST** /api/v2/apps/{uuid}/settings-schema/options | Load dynamic options for a setting select field
[**migrate_to_v2**](ApplicationsApi.md#migrate_to_v2) | **POST** /api/v2/apps/{uuid}/migrate-v2 | Migrate an app from platform V1 to V2
[**review_public_app**](ApplicationsApi.md#review_public_app) | **POST** /api/v2/apps/public/{uuid}/review | Review a public app
[**rotate_app**](ApplicationsApi.md#rotate_app) | **POST** /api/v2/apps/{uuid}/rotate | Rotate application configurations
[**stream_runtime_logs**](ApplicationsApi.md#stream_runtime_logs) | **GET** /api/v2/apps/{appUuid}/runtime/logs/stream | Stream app runtime logs (SSE)
[**submit_public_app**](ApplicationsApi.md#submit_public_app) | **POST** /api/v2/apps/public/{uuid}/submit | Submit a public app for review
[**test_app_webhook**](ApplicationsApi.md#test_app_webhook) | **POST** /api/v2/apps/{appUuid}/webhooks/test/{webhookUuid}/{recordUuid}/{eventType} | Test a webhook for an app
[**test_app_webhook_auto**](ApplicationsApi.md#test_app_webhook_auto) | **POST** /api/v2/apps/{appUuid}/webhooks/test/{webhookUuid} | Test a webhook for an app (auto-resolve)
[**test_app_webhook_unsaved**](ApplicationsApi.md#test_app_webhook_unsaved) | **POST** /api/v2/apps/{appUuid}/webhooks/test | Test an unsaved webhook for an app
[**uninstall_app**](ApplicationsApi.md#uninstall_app) | **POST** /api/v2/apps/{uuid}/uninstall | Uninstall an application
[**update_app_webhook_for_app**](ApplicationsApi.md#update_app_webhook_for_app) | **PUT** /api/v2/apps/{appUuid}/webhooks/{webhookUuid} | Update a webhook for an app
[**update_public_app**](ApplicationsApi.md#update_public_app) | **PUT** /api/v2/apps/public/{uuid} | Update a public app (creator edit)


# **create_app_webhook_for_app**
> CreateResponse create_app_webhook_for_app(app_uuid, subscribe_webhook_dto)

Create a webhook for an app (app-scoped path)

Creates a new webhook for the specified app using normal bearer authentication. The app must be installed for the authenticated user's selected company. This endpoint is an app-scoped equivalent of the generic webhook creation endpoint.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.subscribe_webhook_dto import SubscribeWebhookDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app to create the webhook for
    subscribe_webhook_dto = caraer_client.SubscribeWebhookDTO() # SubscribeWebhookDTO | Webhook details

    try:
        # Create a webhook for an app (app-scoped path)
        api_response = api_instance.create_app_webhook_for_app(app_uuid, subscribe_webhook_dto)
        print("The response of ApplicationsApi->create_app_webhook_for_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_app_webhook_for_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app to create the webhook for | 
 **subscribe_webhook_dto** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md)| Webhook details | 

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
**200** | Webhook created successfully |  -  |
**400** | Invalid input provided or app not installed |  -  |
**404** | App not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_private_app**
> CreateResponse create_private_app(create_private_app_request)

Create a private app

Creates a new private app with the provided label and optional description. Private apps are automatically installed for the creating user's company. Returns the created app details as a CreateResponse wrapping an AppDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_private_app_request import CreatePrivateAppRequest
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    create_private_app_request = caraer_client.CreatePrivateAppRequest() # CreatePrivateAppRequest | 

    try:
        # Create a private app
        api_response = api_instance.create_private_app(create_private_app_request)
        print("The response of ApplicationsApi->create_private_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_private_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_private_app_request** | [**CreatePrivateAppRequest**](CreatePrivateAppRequest.md)|  | 

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
**200** | Successfully created the private app |  -  |
**400** | Invalid request data |  -  |
**401** | Unauthorized access |  -  |
**500** | Internal server error |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_public_app**
> CreateResponse create_public_app(app_dto)

Create a public app

Creates a new public app with the provided label and optional description. Public apps are automatically published for the creating user's company. Returns the created app details as a CreateResponse wrapping an AppDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_dto import AppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_dto = caraer_client.AppDTO() # AppDTO | 

    try:
        # Create a public app
        api_response = api_instance.create_public_app(app_dto)
        print("The response of ApplicationsApi->create_public_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_public_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_dto** | [**AppDTO**](AppDTO.md)|  | 

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
**200** | Successfully created the public app |  -  |
**400** | Invalid request data |  -  |
**401** | Unauthorized access |  -  |
**500** | Internal server error |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_webhook**
> DeleteResponse delete_app_webhook(app_uuid, webhook_uuid)

Delete a webhook for an app

Deletes a webhook that belongs to the specified app and the authenticated user's selected company.

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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app that owns the webhook
    webhook_uuid = 'webhook_uuid_example' # str | UUID of the webhook to delete

    try:
        # Delete a webhook for an app
        api_response = api_instance.delete_app_webhook(app_uuid, webhook_uuid)
        print("The response of ApplicationsApi->delete_app_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_app_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app that owns the webhook | 
 **webhook_uuid** | **str**| UUID of the webhook to delete | 

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
**200** | Webhook deleted successfully |  -  |
**404** | Webhook not found for the specified app or company |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> ShowResponseAppDTO get_app(uuid)

Retrieve application details by UUID

Fetches details about an application specified by its UUID. Returns the application details as a ShowResponse wrapping an AppDetailDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the application to retrieve

    try:
        # Retrieve application details by UUID
        api_response = api_instance.get_app(uuid)
        print("The response of ApplicationsApi->get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the application to retrieve | 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved application details |  -  |
**404** | Application not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_webhook**
> ShowResponseSubscribeWebhookDTO get_app_webhook(app_uuid, webhook_uuid)

Get a webhook for an app

Fetches a single webhook that belongs to the specified app.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_subscribe_webhook_dto import ShowResponseSubscribeWebhookDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app that owns the webhook
    webhook_uuid = 'webhook_uuid_example' # str | UUID of the webhook to fetch

    try:
        # Get a webhook for an app
        api_response = api_instance.get_app_webhook(app_uuid, webhook_uuid)
        print("The response of ApplicationsApi->get_app_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_app_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app that owns the webhook | 
 **webhook_uuid** | **str**| UUID of the webhook to fetch | 

### Return type

[**ShowResponseSubscribeWebhookDTO**](ShowResponseSubscribeWebhookDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook retrieved successfully |  -  |
**404** | Webhook not found for the specified app or company |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_webhooks**
> PaginationResponseSubscribeWebhookDTO get_app_webhooks(app_uuid, pagination_request)

Retrieve a paginated list of webhooks for an app

Fetches a paginated and optionally filtered list of webhooks associated with the specified app and the authenticated user's selected company.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_subscribe_webhook_dto import PaginationResponseSubscribeWebhookDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the application for which to retrieve webhooks
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Retrieve a paginated list of webhooks for an app
        api_response = api_instance.get_app_webhooks(app_uuid, pagination_request)
        print("The response of ApplicationsApi->get_app_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_app_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the application for which to retrieve webhooks | 
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponseSubscribeWebhookDTO**](PaginationResponseSubscribeWebhookDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of webhooks for the app |  -  |
**400** | Invalid request data or app not installed for company |  -  |
**401** | Unauthorized access |  -  |
**404** | Application not found |  -  |
**500** | Internal server error |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> PaginationResponseAppDTO get_apps(pagination_request, type=type, installed_only=installed_only)

Retrieve a paginated list of applications

Fetches a paginated and optionally filtered list of applications. The list is sorted alphabetically by category and name. On success, returns a PaginationResponse containing AppSummaryDTO objects.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_app_dto import PaginationResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 
    type = '' # str |  (optional) (default to '')
    installed_only = False # bool |  (optional) (default to False)

    try:
        # Retrieve a paginated list of applications
        api_response = api_instance.get_apps(pagination_request, type=type, installed_only=installed_only)
        print("The response of ApplicationsApi->get_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 
 **type** | **str**|  | [optional] [default to &#39;&#39;]
 **installed_only** | **bool**|  | [optional] [default to False]

### Return type

[**PaginationResponseAppDTO**](PaginationResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of applications |  -  |
**400** | Invalid request data |  -  |
**401** | Unauthorized access |  -  |
**500** | Internal server error |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_information**
> SimplePublicCompanyDTO get_company_information(app_uuid)

Get current user's company information

Retrieves the company information of the authenticated user. The response includes public details of the user's selected company.

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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app to get the company information for

    try:
        # Get current user's company information
        api_response = api_instance.get_company_information(app_uuid)
        print("The response of ApplicationsApi->get_company_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_company_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app to get the company information for | 

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
**200** | Successfully retrieved company information |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_created_apps**
> PaginationResponseAppDTO get_my_created_apps(pagination_request)

Retrieve apps created by the logged-in user's selected company

Fetches a paginated and optionally filtered list of apps where the selected company is the creator. Returns a PaginationResponse containing AppDTO objects.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_app_dto import PaginationResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Retrieve apps created by the logged-in user's selected company
        api_response = api_instance.get_my_created_apps(pagination_request)
        print("The response of ApplicationsApi->get_my_created_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_my_created_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponseAppDTO**](PaginationResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved creator apps |  -  |
**400** | Invalid request data |  -  |
**401** | Unauthorized access |  -  |
**500** | Internal server error |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_app**
> ShowResponseAppDTO get_public_app(uuid)

Get a public app (creator view)

Gets the full app for the creator, including appPublish, appBars, details, and pricing. Returns AppCreatorDTO with everything under App.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the public app to retrieve

    try:
        # Get a public app (creator view)
        api_response = api_instance.get_public_app(uuid)
        print("The response of ApplicationsApi->get_public_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_public_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the public app to retrieve | 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the public app |  -  |
**404** | Public app not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_logs**
> SuccessResponseMapStringObject get_runtime_logs(app_uuid, since=since, limit=limit)

Get app runtime logs

Queries Cloud Logging for the shared V2 app container (app-{uuid}) without filtering to a single function.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_map_string_object import SuccessResponseMapStringObject
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    since = '1h' # str | Lookback window, e.g. 15m, 1h, 24h (optional) (default to '1h')
    limit = 100 # int | Maximum number of log entries to return (optional) (default to 100)

    try:
        # Get app runtime logs
        api_response = api_instance.get_runtime_logs(app_uuid, since=since, limit=limit)
        print("The response of ApplicationsApi->get_runtime_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_runtime_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **since** | **str**| Lookback window, e.g. 15m, 1h, 24h | [optional] [default to &#39;1h&#39;]
 **limit** | **int**| Maximum number of log entries to return | [optional] [default to 100]

### Return type

[**SuccessResponseMapStringObject**](SuccessResponseMapStringObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved logs (may be empty if logging is unavailable) |  -  |
**404** | App not found |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_events**
> List[Dict[str, Optional[object]]] get_webhook_events(app_uuid)

Get available webhook record events

Returns all supported record webhook events with their details.

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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app to get the webhook events for

    try:
        # Get available webhook record events
        api_response = api_instance.get_webhook_events(app_uuid)
        print("The response of ApplicationsApi->get_webhook_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_webhook_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app to get the webhook events for | 

### Return type

**List[Dict[str, Optional[object]]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available webhook record events |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_formats**
> List[Dict[str, Optional[object]]] get_webhook_formats(app_uuid)

Get available webhook formats

Returns all supported webhook payload formats with their details.

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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app to get the webhook formats for

    try:
        # Get available webhook formats
        api_response = api_instance.get_webhook_formats(app_uuid)
        print("The response of ApplicationsApi->get_webhook_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_webhook_formats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app to get the webhook formats for | 

### Return type

**List[Dict[str, Optional[object]]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available webhook formats |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_property_topics**
> List[Dict[str, str]] get_webhook_property_topics(app_uuid, object)

Get webhook property topic options

Returns property names on an object that can be used in 4-part property_changed webhook topics.

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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app
    object = 'object_example' # str | Object name (e.g. contact)

    try:
        # Get webhook property topic options
        api_response = api_instance.get_webhook_property_topics(app_uuid, object)
        print("The response of ApplicationsApi->get_webhook_property_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_webhook_property_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 
 **object** | **str**| Object name (e.g. contact) | 

### Return type

**List[Dict[str, str]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of property names |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_app**
> ShowResponseAppDTO install_app(uuid, install_app_request=install_app_request)

Install an application

Installs the application specified by its UUID with optional initial configuration settings. Returns the updated application details as a ShowResponse wrapping an AppDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.install_app_request import InstallAppRequest
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the application to install
    install_app_request = caraer_client.InstallAppRequest() # InstallAppRequest |  (optional)

    try:
        # Install an application
        api_response = api_instance.install_app(uuid, install_app_request=install_app_request)
        print("The response of ApplicationsApi->install_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->install_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the application to install | 
 **install_app_request** | [**InstallAppRequest**](InstallAppRequest.md)|  | [optional] 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully installed the application |  -  |
**404** | Application not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_categories**
> List[Dict[str, object]] list_app_categories()

List predefined marketplace app categories

Returns the allowed category keys and labels for public app marketplace listings.

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
    api_instance = caraer_client.ApplicationsApi(api_client)

    try:
        # List predefined marketplace app categories
        api_response = api_instance.list_app_categories()
        print("The response of ApplicationsApi->list_app_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_app_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Dict[str, object]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved app categories |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_setting_options**
> ShowResponseLoadAppSettingOptionsResponse load_setting_options(uuid, load_app_setting_options_request)

Load dynamic options for a setting select field

Invokes the app serverless function configured on the field's optionsSource and returns options for SINGLE_SELECT / MULTI_SELECT fields. Uses the draft settingsSchema from the installer UI so credentials entered in other fields are available to the loader.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.load_app_setting_options_request import LoadAppSettingOptionsRequest
from caraer_client.models.show_response_load_app_setting_options_response import ShowResponseLoadAppSettingOptionsResponse
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the application
    load_app_setting_options_request = caraer_client.LoadAppSettingOptionsRequest() # LoadAppSettingOptionsRequest | Field name, optional query, and draft settings schema

    try:
        # Load dynamic options for a setting select field
        api_response = api_instance.load_setting_options(uuid, load_app_setting_options_request)
        print("The response of ApplicationsApi->load_setting_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->load_setting_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the application | 
 **load_app_setting_options_request** | [**LoadAppSettingOptionsRequest**](LoadAppSettingOptionsRequest.md)| Field name, optional query, and draft settings schema | 

### Return type

[**ShowResponseLoadAppSettingOptionsResponse**](ShowResponseLoadAppSettingOptionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Options loaded successfully |  -  |
**400** | Invalid request or dependsOn not satisfied |  -  |
**403** | App not accessible |  -  |
**404** | App, field, or serverless function not found |  -  |
**502** | Serverless function failed or returned invalid response |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_to_v2**
> SuccessResponseMapStringObject migrate_to_v2(uuid, migrate_app_to_v2_request=migrate_app_to_v2_request)

Migrate an app from platform V1 to V2

Opt-in in-place migration to the shared container runtime. Validates a single runtime, sets platformVersion=2, schedules an async rebuild, and keeps invoking via legacy gcpReference until runtimeStatus is READY.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.migrate_app_to_v2_request import MigrateAppToV2Request
from caraer_client.models.success_response_map_string_object import SuccessResponseMapStringObject
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the app to migrate
    migrate_app_to_v2_request = caraer_client.MigrateAppToV2Request() # MigrateAppToV2Request |  (optional)

    try:
        # Migrate an app from platform V1 to V2
        api_response = api_instance.migrate_to_v2(uuid, migrate_app_to_v2_request=migrate_app_to_v2_request)
        print("The response of ApplicationsApi->migrate_to_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->migrate_to_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the app to migrate | 
 **migrate_app_to_v2_request** | [**MigrateAppToV2Request**](MigrateAppToV2Request.md)|  | [optional] 

### Return type

[**SuccessResponseMapStringObject**](SuccessResponseMapStringObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Migration started or already in progress |  -  |
**400** | Mixed/missing runtimes or invalid request |  -  |
**403** | Not allowed to migrate this app |  -  |
**404** | App not found |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_public_app**
> ShowResponseAppDTO review_public_app(uuid, review_request)

Review a public app

Sets review outcome (approve/reject/changes requested), feedback, and optional reviewer notes. Returns the updated app details as a ShowResponse wrapping an AppDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.review_request import ReviewRequest
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the public app to review
    review_request = caraer_client.ReviewRequest() # ReviewRequest | 

    try:
        # Review a public app
        api_response = api_instance.review_public_app(uuid, review_request)
        print("The response of ApplicationsApi->review_public_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->review_public_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the public app to review | 
 **review_request** | [**ReviewRequest**](ReviewRequest.md)|  | 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully reviewed the public app |  -  |
**404** | Public app not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_app**
> ShowResponseAppDTO rotate_app(uuid)

Rotate application configurations

Rotates the configuration or settings for the specified application by UUID. On success, returns the updated application details as a ShowResponse wrapping an AppDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the application to rotate configurations

    try:
        # Rotate application configurations
        api_response = api_instance.rotate_app(uuid)
        print("The response of ApplicationsApi->rotate_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->rotate_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the application to rotate configurations | 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully rotated application configurations |  -  |
**404** | Application not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_runtime_logs**
> SseEmitter stream_runtime_logs(app_uuid)

Stream app runtime logs (SSE)

Server-Sent Events stream of Cloud Logging entries for the shared V2 app container. Polls every ~2.5s and stops after 5 minutes or client disconnect.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.sse_emitter import SseEmitter
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app

    try:
        # Stream app runtime logs (SSE)
        api_response = api_instance.stream_runtime_logs(app_uuid)
        print("The response of ApplicationsApi->stream_runtime_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->stream_runtime_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app | 

### Return type

[**SseEmitter**](SseEmitter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE stream of log entries |  -  |
**404** | The requested resource was not found. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_public_app**
> ShowResponseAppDTO submit_public_app(uuid)

Submit a public app for review

Submits a public app specified by its UUID for review. Returns the submitted app details as a ShowResponse wrapping an AppDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the public app to submit for review

    try:
        # Submit a public app for review
        api_response = api_instance.submit_public_app(uuid)
        print("The response of ApplicationsApi->submit_public_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->submit_public_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the public app to submit for review | 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully submitted the public app for review |  -  |
**404** | Public app not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_app_webhook**
> str test_app_webhook(app_uuid, webhook_uuid, record_uuid, event_type, property_name=property_name)

Test a webhook for an app

Generates a test webhook payload for a specific record and event type. Uses the same payload generation logic as live webhook delivery.

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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app that owns the webhook
    webhook_uuid = 'webhook_uuid_example' # str | UUID of the webhook to test
    record_uuid = 'record_uuid_example' # str | UUID of the record to include in the webhook payload
    event_type = 'event_type_example' # str | Type of event to simulate. Supported values are the entries returned by /webhooks/events, or property_changed for property webhooks.
    property_name = 'property_name_example' # str | Property name when simulating property_changed (optional)

    try:
        # Test a webhook for an app
        api_response = api_instance.test_app_webhook(app_uuid, webhook_uuid, record_uuid, event_type, property_name=property_name)
        print("The response of ApplicationsApi->test_app_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->test_app_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app that owns the webhook | 
 **webhook_uuid** | **str**| UUID of the webhook to test | 
 **record_uuid** | **str**| UUID of the record to include in the webhook payload | 
 **event_type** | **str**| Type of event to simulate. Supported values are the entries returned by /webhooks/events, or property_changed for property webhooks. | 
 **property_name** | **str**| Property name when simulating property_changed | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook test payload generated successfully |  -  |
**400** | Invalid event type or app not installed |  -  |
**404** | Webhook not found for the specified app or company |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_app_webhook_auto**
> str test_app_webhook_auto(app_uuid, webhook_uuid)

Test a webhook for an app (auto-resolve)

Generates a test webhook payload using the latest matching record for the topic object. Form-submission topics prefer a record that submitted that form; includeRelations prefer a record that has as many of those related objects as possible. If no record exists, a simulated record is used. Missing includeRelations and simulated samples are explained in context.testNote and the X-Webhook-Test-Note header. Uses the event type from the webhook topic (updated when the topic action is all).

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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app that owns the webhook
    webhook_uuid = 'webhook_uuid_example' # str | UUID of the webhook to test

    try:
        # Test a webhook for an app (auto-resolve)
        api_response = api_instance.test_app_webhook_auto(app_uuid, webhook_uuid)
        print("The response of ApplicationsApi->test_app_webhook_auto:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->test_app_webhook_auto: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app that owns the webhook | 
 **webhook_uuid** | **str**| UUID of the webhook to test | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook test payload generated successfully |  -  |
**400** | Webhook topic cannot be used for record testing |  -  |
**404** | Webhook not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_app_webhook_unsaved**
> str test_app_webhook_unsaved(app_uuid, test_webhook_request)

Test an unsaved webhook for an app

Generates a test webhook payload from webhook configuration supplied in the request body without persisting the webhook. When recordUuid is omitted, auto-resolves the latest matching record, prefers records that submitted the topic form and that have as many includeRelations as possible, and uses the event from the webhook topic. If no record exists, a simulated record is used and context.testNote (also X-Webhook-Test-Note) explains that plus any missing includeRelations.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.test_webhook_request import TestWebhookRequest
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app the webhook belongs to
    test_webhook_request = caraer_client.TestWebhookRequest() # TestWebhookRequest | Webhook configuration and optional test event parameters

    try:
        # Test an unsaved webhook for an app
        api_response = api_instance.test_app_webhook_unsaved(app_uuid, test_webhook_request)
        print("The response of ApplicationsApi->test_app_webhook_unsaved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->test_app_webhook_unsaved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app the webhook belongs to | 
 **test_webhook_request** | [**TestWebhookRequest**](TestWebhookRequest.md)| Webhook configuration and optional test event parameters | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook test payload generated successfully |  -  |
**400** | Invalid webhook configuration or event parameters |  -  |
**404** | App not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_app**
> ShowResponseAppDTO uninstall_app(uuid, app_request)

Uninstall an application

Removes the installed application specified by its UUID using the provided settings. The request body should contain an AppRequest with the uninstallation settings. Returns the updated application details as a ShowResponse wrapping an AppDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_request import AppRequest
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the application to uninstall
    app_request = caraer_client.AppRequest() # AppRequest | 

    try:
        # Uninstall an application
        api_response = api_instance.uninstall_app(uuid, app_request)
        print("The response of ApplicationsApi->uninstall_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->uninstall_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the application to uninstall | 
 **app_request** | [**AppRequest**](AppRequest.md)|  | 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully uninstalled the application |  -  |
**404** | Application not found |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_webhook_for_app**
> CreateResponse update_app_webhook_for_app(app_uuid, webhook_uuid, subscribe_webhook_dto)

Update a webhook for an app

Updates an existing webhook that belongs to the specified app and the authenticated user's selected company.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.subscribe_webhook_dto import SubscribeWebhookDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    app_uuid = 'app_uuid_example' # str | UUID of the app that owns the webhook
    webhook_uuid = 'webhook_uuid_example' # str | UUID of the webhook to update
    subscribe_webhook_dto = caraer_client.SubscribeWebhookDTO() # SubscribeWebhookDTO | 

    try:
        # Update a webhook for an app
        api_response = api_instance.update_app_webhook_for_app(app_uuid, webhook_uuid, subscribe_webhook_dto)
        print("The response of ApplicationsApi->update_app_webhook_for_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_app_webhook_for_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_uuid** | **str**| UUID of the app that owns the webhook | 
 **webhook_uuid** | **str**| UUID of the webhook to update | 
 **subscribe_webhook_dto** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md)|  | 

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
**200** | Webhook updated successfully |  -  |
**400** | Invalid input provided or app not installed |  -  |
**404** | Webhook not found for the specified app or company |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_public_app**
> ShowResponseAppDTO update_public_app(uuid, app_dto)

Update a public app (creator edit)

Updates a public app with the full creator payload (label, description, details, pricing, settingsSchema, appBars). Send the entire AppCreatorDTO as returned by GET. Returns the updated app as AppCreatorDTO.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.app_dto import AppDTO
from caraer_client.models.show_response_app_dto import ShowResponseAppDTO
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
    api_instance = caraer_client.ApplicationsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the public app to update
    app_dto = caraer_client.AppDTO() # AppDTO | 

    try:
        # Update a public app (creator edit)
        api_response = api_instance.update_public_app(uuid, app_dto)
        print("The response of ApplicationsApi->update_public_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_public_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the public app to update | 
 **app_dto** | [**AppDTO**](AppDTO.md)|  | 

### Return type

[**ShowResponseAppDTO**](ShowResponseAppDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the public app |  -  |
**404** | Public app not found |  -  |
**403** | You are not allowed to update this app |  -  |
**500** | Internal server error |  -  |
**401** | Authentication is required or the token is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

