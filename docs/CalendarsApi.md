# caraer_client.CalendarsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bootstrap**](CalendarsApi.md#bootstrap) | **POST** /api/v2/calendars/bootstrap | Ensure calendar schema, default calendar, and event backfill
[**create4**](CalendarsApi.md#create4) | **POST** /api/v2/calendars | Create a calendar owned by the current user
[**list3**](CalendarsApi.md#list3) | **GET** /api/v2/calendars | List calendars visible to the current company
[**list_teams**](CalendarsApi.md#list_teams) | **GET** /api/v2/calendars/teams | List teams that can be linked to a calendar


# **bootstrap**
> SuccessResponseCalendarBootstrapDTO bootstrap()

Ensure calendar schema, default calendar, and event backfill

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_calendar_bootstrap_dto import SuccessResponseCalendarBootstrapDTO
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
    api_instance = caraer_client.CalendarsApi(api_client)

    try:
        # Ensure calendar schema, default calendar, and event backfill
        api_response = api_instance.bootstrap()
        print("The response of CalendarsApi->bootstrap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->bootstrap: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponseCalendarBootstrapDTO**](SuccessResponseCalendarBootstrapDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calendars ready |  -  |
**400** | Invalid request |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create4**
> CreateResponseCalendarRecordDTO create4(calendar_create_request)

Create a calendar owned by the current user

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.calendar_create_request import CalendarCreateRequest
from caraer_client.models.create_response_calendar_record_dto import CreateResponseCalendarRecordDTO
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
    api_instance = caraer_client.CalendarsApi(api_client)
    calendar_create_request = caraer_client.CalendarCreateRequest() # CalendarCreateRequest | 

    try:
        # Create a calendar owned by the current user
        api_response = api_instance.create4(calendar_create_request)
        print("The response of CalendarsApi->create4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->create4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_create_request** | [**CalendarCreateRequest**](CalendarCreateRequest.md)|  | 

### Return type

[**CreateResponseCalendarRecordDTO**](CreateResponseCalendarRecordDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calendar created |  -  |
**400** | Invalid request |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list3**
> SuccessResponseListCalendarRecordDTO list3()

List calendars visible to the current company

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_calendar_record_dto import SuccessResponseListCalendarRecordDTO
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
    api_instance = caraer_client.CalendarsApi(api_client)

    try:
        # List calendars visible to the current company
        api_response = api_instance.list3()
        print("The response of CalendarsApi->list3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->list3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponseListCalendarRecordDTO**](SuccessResponseListCalendarRecordDTO.md)

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

# **list_teams**
> SuccessResponseListCalendarTeamOptionDTO list_teams()

List teams that can be linked to a calendar

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.success_response_list_calendar_team_option_dto import SuccessResponseListCalendarTeamOptionDTO
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
    api_instance = caraer_client.CalendarsApi(api_client)

    try:
        # List teams that can be linked to a calendar
        api_response = api_instance.list_teams()
        print("The response of CalendarsApi->list_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->list_teams: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponseListCalendarTeamOptionDTO**](SuccessResponseListCalendarTeamOptionDTO.md)

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

