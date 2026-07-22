# NotFoundError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | [**NotFoundErrorCause**](NotFoundErrorCause.md) |  | [optional] 
**stack_trace** | [**List[NotFoundErrorCauseStackTraceInner]**](NotFoundErrorCauseStackTraceInner.md) |  | [optional] 
**errors** | [**List[CaraerErrorType]**](CaraerErrorType.md) | The error message providing details about the failure. | [optional] 
**code** | **int** | The HTTP status code associated with the error. | [optional] 
**correction_suggestion** | **str** | A suggestion on how to correct the error. | 
**message** | **str** | The error message providing details about the failure. | 
**suppressed** | [**List[NotFoundErrorCause]**](NotFoundErrorCause.md) |  | [optional] 
**localized_message** | **str** |  | [optional] 
**resource_kind** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**identifier_type** | **str** |  | [optional] 
**referenced_by** | [**List[Reference]**](Reference.md) |  | [optional] 

## Example

```python
from caraer_client.models.not_found_error import NotFoundError

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundError from a JSON string
not_found_error_instance = NotFoundError.from_json(json)
# print the JSON string representation of the object
print(NotFoundError.to_json())

# convert the object into a dict
not_found_error_dict = not_found_error_instance.to_dict()
# create an instance of NotFoundError from a dict
not_found_error_from_dict = NotFoundError.from_dict(not_found_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


