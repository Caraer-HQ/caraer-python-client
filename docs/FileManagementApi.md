# caraer_client.FileManagementApi

All URIs are relative to *https://v2.api.caraer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FileManagementApi.md#delete_file) | **DELETE** /api/v2/files/ | Delete file
[**download_file**](FileManagementApi.md#download_file) | **GET** /api/v2/files/ | Download file
[**list_files**](FileManagementApi.md#list_files) | **GET** /api/v2/files/list | List files
[**upload_file2**](FileManagementApi.md#upload_file2) | **POST** /api/v2/files/ | Upload files


# **delete_file**
> SuccessResponse delete_file(key)

Delete file

Deletes a file from the S3-compatible storage identified by its unique key.

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
    api_instance = caraer_client.FileManagementApi(api_client)
    key = 'file12345' # str | The key of the file to delete.

    try:
        # Delete file
        api_response = api_instance.delete_file(key)
        print("The response of FileManagementApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagementApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the file to delete. | 

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
**200** | File deleted successfully. |  -  |
**404** | File not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> SuccessResponse download_file(key, expire_after=expire_after, download=download)

Download file

Generates a pre-signed URL to download a file stored in S3-compatible storage. The URL expiry time and download behavior can be specified using the query parameters.

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
    api_instance = caraer_client.FileManagementApi(api_client)
    key = 'file12345' # str | The key of the file to download.
    expire_after = 86400 # int | The URL expiry period in seconds. (optional) (default to 86400)
    download = False # bool | Whether to download the file in the browser. (optional) (default to False)

    try:
        # Download file
        api_response = api_instance.download_file(key, expire_after=expire_after, download=download)
        print("The response of FileManagementApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagementApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the file to download. | 
 **expire_after** | **int**| The URL expiry period in seconds. | [optional] [default to 86400]
 **download** | **bool**| Whether to download the file in the browser. | [optional] [default to False]

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
**200** | File URL generated successfully. |  -  |
**404** | File not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> SuccessResponse list_files(record_uuid=record_uuid)

List files

Lists all files stored in the system or, if a record UUID is provided, lists the files related to that record.

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
    api_instance = caraer_client.FileManagementApi(api_client)
    record_uuid = 'record12345' # str | An optional record UUID to filter files. (optional)

    try:
        # List files
        api_response = api_instance.list_files(record_uuid=record_uuid)
        print("The response of FileManagementApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagementApi->list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**| An optional record UUID to filter files. | [optional] 

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
**200** | Files listed successfully. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file2**
> SuccessResponse upload_file2(record_uuid=record_uuid)

Upload files

Uploads multiple files to an S3-compatible storage and returns their unique keys. The request must contain one or more files in multipart/form-data format.

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
    api_instance = caraer_client.FileManagementApi(api_client)
    record_uuid = 'record12345' # str | Optional record UUID to directly link uploaded files as attachments. (optional)

    try:
        # Upload files
        api_response = api_instance.upload_file2(record_uuid=record_uuid)
        print("The response of FileManagementApi->upload_file2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileManagementApi->upload_file2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_uuid** | **str**| Optional record UUID to directly link uploaded files as attachments. | [optional] 

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
**200** | Files uploaded successfully. |  -  |
**400** | Invalid input, e.g., file size exceeds the limit. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

