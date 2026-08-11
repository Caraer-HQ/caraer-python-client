# ErrorResponse

Defines the structure of error responses returned by the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message providing details about the failure. | [optional] 
**errors** | [**CaraerErrorType**](CaraerErrorType.md) | A list of error types providing further details about the error. | [optional] 
**status** | **int** | The HTTP status code associated with the error. | [optional] 
**stack_trace** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**request_id** | **str** | Request correlation ID for support and log tracing. | [optional] 

## Example

```python
from caraer_client.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse.to_json())

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_from_dict = ErrorResponse.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


