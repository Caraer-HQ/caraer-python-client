# ValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | [**NotFoundErrorCause**](NotFoundErrorCause.md) |  | [optional] 
**stack_trace** | [**List[NotFoundErrorCauseStackTraceInner]**](NotFoundErrorCauseStackTraceInner.md) |  | [optional] 
**suppressed** | [**List[NotFoundErrorCause]**](NotFoundErrorCause.md) |  | [optional] 
**localized_message** | **str** |  | [optional] 
**type** | **str** | The type of error. | 
**var_field** | **str** |  | [optional] 
**message** | **str** | The error message providing details about the failure. | 
**correction_suggestion** | **str** | A suggestion on how to correct the error. | 
**var_class** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.validation_error import ValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError from a JSON string
validation_error_instance = ValidationError.from_json(json)
# print the JSON string representation of the object
print(ValidationError.to_json())

# convert the object into a dict
validation_error_dict = validation_error_instance.to_dict()
# create an instance of ValidationError from a dict
validation_error_from_dict = ValidationError.from_dict(validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


