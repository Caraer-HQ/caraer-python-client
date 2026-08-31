# caraer_client.DeveloperProjectsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](DeveloperProjectsApi.md#create2) | **POST** /api/v2/developer-projects | Create or fetch a developer project
[**create_build**](DeveloperProjectsApi.md#create_build) | **POST** /api/v2/developer-projects/{projectUuid}/builds | Upload a project build
[**deploy**](DeveloperProjectsApi.md#deploy) | **POST** /api/v2/developer-projects/{projectUuid}/builds/{buildUuid}/deploy | Deploy a project build
[**get_build**](DeveloperProjectsApi.md#get_build) | **GET** /api/v2/developer-projects/{projectUuid}/builds/{buildUuid} | Get a project build
[**list_builds**](DeveloperProjectsApi.md#list_builds) | **GET** /api/v2/developer-projects/{projectUuid}/builds | List project builds
[**list_deploys**](DeveloperProjectsApi.md#list_deploys) | **GET** /api/v2/developer-projects/{projectUuid}/deploys | List project deploys
[**show3**](DeveloperProjectsApi.md#show3) | **GET** /api/v2/developer-projects/{uuid} | Get a developer project


# **create2**
> CreateResponse create2(create_developer_project_request)

Create or fetch a developer project

Creates a developer project linked to the given app, or returns the existing one if already linked. Creator company only.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_developer_project_request import CreateDeveloperProjectRequest
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
    api_instance = caraer_client.DeveloperProjectsApi(api_client)
    create_developer_project_request = caraer_client.CreateDeveloperProjectRequest() # CreateDeveloperProjectRequest | 

    try:
        # Create or fetch a developer project
        api_response = api_instance.create2(create_developer_project_request)
        print("The response of DeveloperProjectsApi->create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperProjectsApi->create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_developer_project_request** | [**CreateDeveloperProjectRequest**](CreateDeveloperProjectRequest.md)|  | 

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
**200** | Project created or fetched |  -  |
**400** | appUuid is required |  -  |
**403** | Caller is not the app creator |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build**
> CreateResponse create_build(project_uuid, create_project_build_request)

Upload a project build

Decodes a base64-encoded project archive, parses its manifest, uploads it to Cloud Storage, and records an immutable build.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_project_build_request import CreateProjectBuildRequest
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
    api_instance = caraer_client.DeveloperProjectsApi(api_client)
    project_uuid = 'project_uuid_example' # str | UUID of the developer project
    create_project_build_request = caraer_client.CreateProjectBuildRequest() # CreateProjectBuildRequest | 

    try:
        # Upload a project build
        api_response = api_instance.create_build(project_uuid, create_project_build_request)
        print("The response of DeveloperProjectsApi->create_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperProjectsApi->create_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**| UUID of the developer project | 
 **create_project_build_request** | [**CreateProjectBuildRequest**](CreateProjectBuildRequest.md)|  | 

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
**200** | Build recorded (may still have status FAILED if parsing/upload failed) |  -  |
**400** | archiveBase64 is required |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy**
> CreateResponse deploy(project_uuid, build_uuid, deploy_build_request=deploy_build_request)

Deploy a project build

Reconciles the build's manifest (app details, serverless functions, webhooks, schedules, inbound routes, external OAuth providers) against the linked app. Set prune=true to soft-delete remote resources absent from the archive.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.deploy_build_request import DeployBuildRequest
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
    api_instance = caraer_client.DeveloperProjectsApi(api_client)
    project_uuid = 'project_uuid_example' # str | UUID of the developer project
    build_uuid = 'build_uuid_example' # str | UUID of the build to deploy
    deploy_build_request = caraer_client.DeployBuildRequest() # DeployBuildRequest |  (optional)

    try:
        # Deploy a project build
        api_response = api_instance.deploy(project_uuid, build_uuid, deploy_build_request=deploy_build_request)
        print("The response of DeveloperProjectsApi->deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperProjectsApi->deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**| UUID of the developer project | 
 **build_uuid** | **str**| UUID of the build to deploy | 
 **deploy_build_request** | [**DeployBuildRequest**](DeployBuildRequest.md)|  | [optional] 

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
**200** | Deploy recorded |  -  |
**400** | Build is not ready to deploy |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build**
> get_build(project_uuid, build_uuid)

Get a project build

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
    api_instance = caraer_client.DeveloperProjectsApi(api_client)
    project_uuid = 'project_uuid_example' # str | UUID of the developer project
    build_uuid = 'build_uuid_example' # str | UUID of the build

    try:
        # Get a project build
        api_instance.get_build(project_uuid, build_uuid)
    except Exception as e:
        print("Exception when calling DeveloperProjectsApi->get_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**| UUID of the developer project | 
 **build_uuid** | **str**| UUID of the build | 

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
**404** | Build not found for this project |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_builds**
> SuccessResponseListProjectBuildDTO list_builds(project_uuid)

List project builds

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_project_build_dto import SuccessResponseListProjectBuildDTO
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
    api_instance = caraer_client.DeveloperProjectsApi(api_client)
    project_uuid = 'project_uuid_example' # str | UUID of the developer project

    try:
        # List project builds
        api_response = api_instance.list_builds(project_uuid)
        print("The response of DeveloperProjectsApi->list_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperProjectsApi->list_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**| UUID of the developer project | 

### Return type

[**SuccessResponseListProjectBuildDTO**](SuccessResponseListProjectBuildDTO.md)

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

# **list_deploys**
> SuccessResponseListProjectDeployDTO list_deploys(project_uuid)

List project deploys

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_project_deploy_dto import SuccessResponseListProjectDeployDTO
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
    api_instance = caraer_client.DeveloperProjectsApi(api_client)
    project_uuid = 'project_uuid_example' # str | UUID of the developer project

    try:
        # List project deploys
        api_response = api_instance.list_deploys(project_uuid)
        print("The response of DeveloperProjectsApi->list_deploys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperProjectsApi->list_deploys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**| UUID of the developer project | 

### Return type

[**SuccessResponseListProjectDeployDTO**](SuccessResponseListProjectDeployDTO.md)

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

# **show3**
> ShowResponseDeveloperProjectDTO show3(uuid)

Get a developer project

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_developer_project_dto import ShowResponseDeveloperProjectDTO
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
    api_instance = caraer_client.DeveloperProjectsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the developer project

    try:
        # Get a developer project
        api_response = api_instance.show3(uuid)
        print("The response of DeveloperProjectsApi->show3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperProjectsApi->show3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the developer project | 

### Return type

[**ShowResponseDeveloperProjectDTO**](ShowResponseDeveloperProjectDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project retrieved |  -  |
**404** | Project not found |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

