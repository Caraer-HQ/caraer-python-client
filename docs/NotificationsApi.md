# caraer_client.NotificationsApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dismiss_notification**](NotificationsApi.md#dismiss_notification) | **DELETE** /api/v2/notifications/{notificationId} | Dismiss a notification
[**firebase_token**](NotificationsApi.md#firebase_token) | **GET** /api/v2/notifications/firebase-token | Mint a Firebase custom token so the app can listen to its inbox
[**get_notification**](NotificationsApi.md#get_notification) | **GET** /api/v2/notifications/{notificationId} | Get an authoritative notification by ID
[**list_notifications**](NotificationsApi.md#list_notifications) | **GET** /api/v2/notifications | List in-app notifications for the logged-in user
[**mark_all_as_read**](NotificationsApi.md#mark_all_as_read) | **PATCH** /api/v2/notifications/read-all | Mark all notifications as read
[**mark_as_read**](NotificationsApi.md#mark_as_read) | **PATCH** /api/v2/notifications/{notificationId}/read | Mark a notification as read
[**register_device**](NotificationsApi.md#register_device) | **PUT** /api/v2/notifications/devices/{deviceInstallationId} | Register this user&#39;s native notification device
[**send_notification**](NotificationsApi.md#send_notification) | **POST** /api/v2/notifications | Send a notification (app token)
[**unregister_device**](NotificationsApi.md#unregister_device) | **DELETE** /api/v2/notifications/devices/{deviceInstallationId} | Unregister this user&#39;s native notification device


# **dismiss_notification**
> DeleteResponseString dismiss_notification(notification_id)

Dismiss a notification

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.delete_response_string import DeleteResponseString
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
    api_instance = caraer_client.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | Firestore notification document ID

    try:
        # Dismiss a notification
        api_response = api_instance.dismiss_notification(notification_id)
        print("The response of NotificationsApi->dismiss_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->dismiss_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| Firestore notification document ID | 

### Return type

[**DeleteResponseString**](DeleteResponseString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification dismissed |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firebase_token**
> ShowResponseMapStringString firebase_token()

Mint a Firebase custom token so the app can listen to its inbox

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_map_string_string import ShowResponseMapStringString
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
    api_instance = caraer_client.NotificationsApi(api_client)

    try:
        # Mint a Firebase custom token so the app can listen to its inbox
        api_response = api_instance.firebase_token()
        print("The response of NotificationsApi->firebase_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->firebase_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ShowResponseMapStringString**](ShowResponseMapStringString.md)

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

# **get_notification**
> ShowResponseItem get_notification(notification_id)

Get an authoritative notification by ID

Returns an inbox entry only for its human recipient in the authorized selected company, including entries outside the inbox page.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_item import ShowResponseItem
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
    api_instance = caraer_client.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | 

    try:
        # Get an authoritative notification by ID
        api_response = api_instance.get_notification(notification_id)
        print("The response of NotificationsApi->get_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 

### Return type

[**ShowResponseItem**](ShowResponseItem.md)

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

# **list_notifications**
> ShowResponseNotificationInboxDTO list_notifications(company=company, limit=limit)

List in-app notifications for the logged-in user

Returns notifications for the selected company plus user-general notifications that have no company. Other companies are never included.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.show_response_notification_inbox_dto import ShowResponseNotificationInboxDTO
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
    api_instance = caraer_client.NotificationsApi(api_client)
    company = 'company_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List in-app notifications for the logged-in user
        api_response = api_instance.list_notifications(company=company, limit=limit)
        print("The response of NotificationsApi->list_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ShowResponseNotificationInboxDTO**](ShowResponseNotificationInboxDTO.md)

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

# **mark_all_as_read**
> SuccessResponseString mark_all_as_read()

Mark all notifications as read

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
    api_instance = caraer_client.NotificationsApi(api_client)

    try:
        # Mark all notifications as read
        api_response = api_instance.mark_all_as_read()
        print("The response of NotificationsApi->mark_all_as_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->mark_all_as_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **mark_as_read**
> SuccessResponseString mark_as_read(notification_id)

Mark a notification as read

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
    api_instance = caraer_client.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | Firestore notification document ID

    try:
        # Mark a notification as read
        api_response = api_instance.mark_as_read(notification_id)
        print("The response of NotificationsApi->mark_as_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->mark_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| Firestore notification document ID | 

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
**200** | Notification marked as read |  -  |
**404** | Notification not found |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**403** | The caller is missing a required role or scope. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_device**
> ShowResponseNotificationDeviceReceipt register_device(device_installation_id, notification_device_registration)

Register this user's native notification device

Idempotently registers an allowed native application. Human authentication required. Does not accept a target user or company. Rotate the registration when moving between accounts.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.notification_device_registration import NotificationDeviceRegistration
from caraer_client.models.show_response_notification_device_receipt import ShowResponseNotificationDeviceReceipt
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
    api_instance = caraer_client.NotificationsApi(api_client)
    device_installation_id = 'device_installation_id_example' # str | 
    notification_device_registration = caraer_client.NotificationDeviceRegistration() # NotificationDeviceRegistration | 

    try:
        # Register this user's native notification device
        api_response = api_instance.register_device(device_installation_id, notification_device_registration)
        print("The response of NotificationsApi->register_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->register_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_installation_id** | **str**|  | 
 **notification_device_registration** | [**NotificationDeviceRegistration**](NotificationDeviceRegistration.md)|  | 

### Return type

[**ShowResponseNotificationDeviceReceipt**](ShowResponseNotificationDeviceReceipt.md)

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

# **send_notification**
> CreateResponseMapStringString send_notification(send_notification_request)

Send a notification (app token)

Installed apps call this endpoint after async work completes. Authenticate with the installation token (Authorization: Bearer or X-CARAER-TOKEN). Every notification is scoped to the app's company. Omit targetUserUuid to notify every user in that company, or set it to aim the notification at one member.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import caraer_client
from caraer_client.models.create_response_map_string_string import CreateResponseMapStringString
from caraer_client.models.send_notification_request import SendNotificationRequest
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
    api_instance = caraer_client.NotificationsApi(api_client)
    send_notification_request = caraer_client.SendNotificationRequest() # SendNotificationRequest | 

    try:
        # Send a notification (app token)
        api_response = api_instance.send_notification(send_notification_request)
        print("The response of NotificationsApi->send_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->send_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification_request** | [**SendNotificationRequest**](SendNotificationRequest.md)|  | 

### Return type

[**CreateResponseMapStringString**](CreateResponseMapStringString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notification created |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**401** | Authentication is required or the token is invalid. |  -  |
**404** | The requested resource was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_device**
> SuccessResponseString unregister_device(device_installation_id)

Unregister this user's native notification device

Idempotent. Call before logout; other users' device registrations are inaccessible.

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
    api_instance = caraer_client.NotificationsApi(api_client)
    device_installation_id = 'device_installation_id_example' # str | 

    try:
        # Unregister this user's native notification device
        api_response = api_instance.unregister_device(device_installation_id)
        print("The response of NotificationsApi->unregister_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->unregister_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_installation_id** | **str**|  | 

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

