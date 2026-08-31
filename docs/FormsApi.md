# caraer_client.FormsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_field**](FormsApi.md#chat_field) | **POST** /api/v2/forms/public/{companyUuid}/ai/field/{fieldUuid}/{prompt} | AI form field (public)
[**chat_step**](FormsApi.md#chat_step) | **POST** /api/v2/forms/public/{companyUuid}/ai/step/{stepTitle}/{prompt} | AI form step (public)
[**create_form**](FormsApi.md#create_form) | **POST** /api/v2/forms/ | Create a new form
[**delete_form**](FormsApi.md#delete_form) | **DELETE** /api/v2/forms/{formUuid} | Delete a form
[**get_form**](FormsApi.md#get_form) | **GET** /api/v2/forms/{formUuid} | Get form by UUID
[**get_form_public**](FormsApi.md#get_form_public) | **GET** /api/v2/forms/public/{companyUuid}/{formUuid} | Get form by UUID
[**get_forms**](FormsApi.md#get_forms) | **POST** /api/v2/forms/index | Get paginated list of forms
[**get_forms_by_object**](FormsApi.md#get_forms_by_object) | **POST** /api/v2/forms/{objectUuid}/index | Get forms by object UUID
[**get_forms_public**](FormsApi.md#get_forms_public) | **POST** /api/v2/forms/public/{companyUuid}/index | Get all forms for a company
[**get_objects_with_forms**](FormsApi.md#get_objects_with_forms) | **GET** /api/v2/forms/objects | List objects that have forms
[**get_options**](FormsApi.md#get_options) | **POST** /api/v2/forms/public/{companyUuid}/{propertyUuid}/options | Property options (public)
[**restore_form**](FormsApi.md#restore_form) | **POST** /api/v2/forms/{formUuid}/restore | Restore a deleted form
[**submit**](FormsApi.md#submit) | **POST** /api/v2/forms/public/{companyUuid}/{formUuid}/submit | Submit a form
[**update_form**](FormsApi.md#update_form) | **PUT** /api/v2/forms/{formUuid} | Update an existing form
[**upload_files**](FormsApi.md#upload_files) | **POST** /api/v2/forms/public/{companyUuid}/{formUuid}/upload | Submit a file


# **chat_field**
> SuccessResponseString chat_field(company_uuid, field_uuid, prompt, form_with_ai_prompt_dto)

AI form field (public)

When X-CARAER-TOKEN or X-Caraer-Company-Uuid is sent, that value selects the tenant company and overrides the companyUuid path segment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.form_with_ai_prompt_dto import FormWithAiPromptDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    company_uuid = 'company_uuid_example' # str | 
    field_uuid = 'field_uuid_example' # str | 
    prompt = 'prompt_example' # str | 
    form_with_ai_prompt_dto = caraer_client.FormWithAiPromptDTO() # FormWithAiPromptDTO | 

    try:
        # AI form field (public)
        api_response = api_instance.chat_field(company_uuid, field_uuid, prompt, form_with_ai_prompt_dto)
        print("The response of FormsApi->chat_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->chat_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 
 **field_uuid** | **str**|  | 
 **prompt** | **str**|  | 
 **form_with_ai_prompt_dto** | [**FormWithAiPromptDTO**](FormWithAiPromptDTO.md)|  | 

### Return type

[**SuccessResponseString**](SuccessResponseString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_step**
> SuccessResponseListString chat_step(company_uuid, step_title, prompt, form_with_ai_prompt_dto)

AI form step (public)

When X-CARAER-TOKEN or X-Caraer-Company-Uuid is sent, that value selects the tenant company and overrides the companyUuid path segment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.form_with_ai_prompt_dto import FormWithAiPromptDTO
from caraer_client.models.success_response_list_string import SuccessResponseListString
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
    api_instance = caraer_client.FormsApi(api_client)
    company_uuid = 'company_uuid_example' # str | 
    step_title = 'step_title_example' # str | 
    prompt = 'prompt_example' # str | 
    form_with_ai_prompt_dto = caraer_client.FormWithAiPromptDTO() # FormWithAiPromptDTO | 

    try:
        # AI form step (public)
        api_response = api_instance.chat_step(company_uuid, step_title, prompt, form_with_ai_prompt_dto)
        print("The response of FormsApi->chat_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->chat_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 
 **step_title** | **str**|  | 
 **prompt** | **str**|  | 
 **form_with_ai_prompt_dto** | [**FormWithAiPromptDTO**](FormWithAiPromptDTO.md)|  | 

### Return type

[**SuccessResponseListString**](SuccessResponseListString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_form**
> CreateResponse create_form(form_dto)

Create a new form

Creates a new form with the provided data. The request body should contain a valid FormDTO object. On success, returns the created form as a FormDTO wrapped in a CreateResponse. Validation: Form fields are validated according to the Form validation rules. Required fields and format constraints are enforced.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response import CreateResponse
from caraer_client.models.form_dto import FormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    form_dto = caraer_client.FormDTO() # FormDTO | 

    try:
        # Create a new form
        api_response = api_instance.create_form(form_dto)
        print("The response of FormsApi->create_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->create_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_dto** | [**FormDTO**](FormDTO.md)|  | 

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
**201** | Form successfully created |  -  |
**400** | Invalid input |  -  |
**401** | Unauthorized access |  -  |
**403** | Forbidden |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form**
> DeleteResponse delete_form(form_uuid)

Delete a form

Deletes a form identified by its UUID. On success, returns the deleted form's data wrapped in a DeleteResponse.

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
    api_instance = caraer_client.FormsApi(api_client)
    form_uuid = 'form_uuid_example' # str | UUID of the form to delete

    try:
        # Delete a form
        api_response = api_instance.delete_form(form_uuid)
        print("The response of FormsApi->delete_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->delete_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_uuid** | **str**| UUID of the form to delete | 

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
**200** | Form successfully deleted |  -  |
**404** | The requested resource was not found. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form**
> ShowResponseFormDTO get_form(form_uuid)

Get form by UUID

Retrieves a specific form by its UUID. Returns the details of the form in a FormDTO object wrapped in a ShowResponse.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_form_dto import ShowResponseFormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    form_uuid = 'form_uuid_example' # str | UUID of the form to retrieve

    try:
        # Get form by UUID
        api_response = api_instance.get_form(form_uuid)
        print("The response of FormsApi->get_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_uuid** | **str**| UUID of the form to retrieve | 

### Return type

[**ShowResponseFormDTO**](ShowResponseFormDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the form |  -  |
**404** | Form not found |  -  |
**401** | Unauthorized access |  -  |
**403** | Forbidden |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_public**
> ShowResponsePublicFormDTO get_form_public(company_uuid, form_uuid)

Get form by UUID

Retrieves a specific form by its UUID. When X-CARAER-TOKEN or X-Caraer-Company-Uuid is sent, that value selects the tenant company and overrides the companyUuid path segment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_public_form_dto import ShowResponsePublicFormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    company_uuid = 'company_uuid_example' # str | 
    form_uuid = 'form_uuid_example' # str | 

    try:
        # Get form by UUID
        api_response = api_instance.get_form_public(company_uuid, form_uuid)
        print("The response of FormsApi->get_form_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_form_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 
 **form_uuid** | **str**|  | 

### Return type

[**ShowResponsePublicFormDTO**](ShowResponsePublicFormDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the form |  -  |
**404** | The requested resource was not found. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forms**
> PaginationResponseFormDTO get_forms(pagination_request)

Get paginated list of forms

Retrieves a paginated list of forms based on the provided filters, sorting, and search query. This endpoint returns a list of FormDTO objects wrapped in a PaginationResponse containing the current page, limit, total count, and the forms data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_form_dto import PaginationResponseFormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Get paginated list of forms
        api_response = api_instance.get_forms(pagination_request)
        print("The response of FormsApi->get_forms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_forms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponseFormDTO**](PaginationResponseFormDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved forms list |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized access |  -  |
**403** | Forbidden |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forms_by_object**
> PaginationResponseFormDTO get_forms_by_object(object_uuid, pagination_request)

Get forms by object UUID

Retrieves a paginated list of forms associated with a specific object UUID. The endpoint uses a custom Cypher query to match forms linked to the object.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_form_dto import PaginationResponseFormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    object_uuid = 'object_uuid_example' # str | UUID of the object to get forms for
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Get forms by object UUID
        api_response = api_instance.get_forms_by_object(object_uuid, pagination_request)
        print("The response of FormsApi->get_forms_by_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_forms_by_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_uuid** | **str**| UUID of the object to get forms for | 
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponseFormDTO**](PaginationResponseFormDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved forms for the given object |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized access |  -  |
**403** | Forbidden |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forms_public**
> PaginationResponsePublicFormDTO get_forms_public(company_uuid, pagination_request)

Get all forms for a company

When X-CARAER-TOKEN or X-Caraer-Company-Uuid is sent, that value selects the tenant company and overrides the companyUuid path segment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_public_form_dto import PaginationResponsePublicFormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    company_uuid = 'company_uuid_example' # str | 
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Get all forms for a company
        api_response = api_instance.get_forms_public(company_uuid, pagination_request)
        print("The response of FormsApi->get_forms_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_forms_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponsePublicFormDTO**](PaginationResponsePublicFormDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objects_with_forms**
> ShowResponseListFormObjectSummaryDTO get_objects_with_forms()

List objects that have forms

Returns distinct custom objects that have at least one non-deleted form, ordered by object index.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_list_form_object_summary_dto import ShowResponseListFormObjectSummaryDTO
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
    api_instance = caraer_client.FormsApi(api_client)

    try:
        # List objects that have forms
        api_response = api_instance.get_objects_with_forms()
        print("The response of FormsApi->get_objects_with_forms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_objects_with_forms: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponseListFormObjectSummaryDTO**](ShowResponseListFormObjectSummaryDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved objects with forms |  -  |
**401** | Unauthorized access |  -  |
**403** | Forbidden |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_options**
> PaginationResponsePropertyOption get_options(property_uuid, company_uuid, pagination_request)

Property options (public)

When X-CARAER-TOKEN or X-Caraer-Company-Uuid is sent, that value selects the tenant company and overrides the companyUuid path segment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.pagination_request import PaginationRequest
from caraer_client.models.pagination_response_property_option import PaginationResponsePropertyOption
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
    api_instance = caraer_client.FormsApi(api_client)
    property_uuid = 'property_uuid_example' # str | 
    company_uuid = 'company_uuid_example' # str | 
    pagination_request = caraer_client.PaginationRequest() # PaginationRequest | 

    try:
        # Property options (public)
        api_response = api_instance.get_options(property_uuid, company_uuid, pagination_request)
        print("The response of FormsApi->get_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->get_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_uuid** | **str**|  | 
 **company_uuid** | **str**|  | 
 **pagination_request** | [**PaginationRequest**](PaginationRequest.md)|  | 

### Return type

[**PaginationResponsePropertyOption**](PaginationResponsePropertyOption.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_form**
> RestoreResponse restore_form(form_uuid)

Restore a deleted form

Restores a previously deleted form identified by its UUID. Returns the restored form wrapped in a RestoreResponse.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.restore_response import RestoreResponse
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
    api_instance = caraer_client.FormsApi(api_client)
    form_uuid = 'form_uuid_example' # str | UUID of the form to restore

    try:
        # Restore a deleted form
        api_response = api_instance.restore_form(form_uuid)
        print("The response of FormsApi->restore_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->restore_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_uuid** | **str**| UUID of the form to restore | 

### Return type

[**RestoreResponse**](RestoreResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form successfully restored |  -  |
**404** | The requested resource was not found. |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit**
> SuccessResponseString submit(company_uuid, form_uuid, form_dto)

Submit a form

Submits a form with the provided data. Returns a SuccessResponse upon successful submission. When X-CARAER-TOKEN or X-Caraer-Company-Uuid is sent, that value selects the tenant company and overrides the companyUuid path segment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.form_dto import FormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    company_uuid = 'company_uuid_example' # str | 
    form_uuid = 'form_uuid_example' # str | 
    form_dto = caraer_client.FormDTO() # FormDTO | 

    try:
        # Submit a form
        api_response = api_instance.submit(company_uuid, form_uuid, form_dto)
        print("The response of FormsApi->submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 
 **form_uuid** | **str**|  | 
 **form_dto** | [**FormDTO**](FormDTO.md)|  | 

### Return type

[**SuccessResponseString**](SuccessResponseString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form successfully submitted |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_form**
> UpdateResponse update_form(form_uuid, form_dto)

Update an existing form

Updates an existing form identified by its UUID with the provided data. The request body should include the updated fields in a FormDTO. Returns the updated form wrapped in an UpdateResponse. Validation: Form fields are validated according to the Form validation rules. Required fields and format constraints are enforced.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.form_dto import FormDTO
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
    api_instance = caraer_client.FormsApi(api_client)
    form_uuid = 'form_uuid_example' # str | UUID of the form to update
    form_dto = caraer_client.FormDTO() # FormDTO | 

    try:
        # Update an existing form
        api_response = api_instance.update_form(form_uuid, form_dto)
        print("The response of FormsApi->update_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->update_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_uuid** | **str**| UUID of the form to update | 
 **form_dto** | [**FormDTO**](FormDTO.md)|  | 

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
**200** | Form successfully updated |  -  |
**400** | Invalid input |  -  |
**404** | Form not found |  -  |
**401** | Unauthorized access |  -  |
**403** | Forbidden |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_files**
> SuccessResponseListString upload_files(company_uuid, form_uuid, files)

Submit a file

Submits a file with the provided data. Returns a SuccessResponse upon successful submission. When X-CARAER-TOKEN or X-Caraer-Company-Uuid is sent, that value selects the tenant company and overrides the companyUuid path segment.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_string import SuccessResponseListString
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
    api_instance = caraer_client.FormsApi(api_client)
    company_uuid = 'company_uuid_example' # str | 
    form_uuid = 'form_uuid_example' # str | 
    files = None # List[bytes] | 

    try:
        # Submit a file
        api_response = api_instance.upload_files(company_uuid, form_uuid, files)
        print("The response of FormsApi->upload_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->upload_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  | 
 **form_uuid** | **str**|  | 
 **files** | [**List[bytes]**](bytes.md)|  | 

### Return type

[**SuccessResponseListString**](SuccessResponseListString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File successfully submitted |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

