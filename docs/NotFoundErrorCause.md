# NotFoundErrorCause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_trace** | [**List[NotFoundErrorCauseStackTraceInner]**](NotFoundErrorCauseStackTraceInner.md) |  | [optional] 
**message** | **str** |  | [optional] 
**localized_message** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.not_found_error_cause import NotFoundErrorCause

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundErrorCause from a JSON string
not_found_error_cause_instance = NotFoundErrorCause.from_json(json)
# print the JSON string representation of the object
print(NotFoundErrorCause.to_json())

# convert the object into a dict
not_found_error_cause_dict = not_found_error_cause_instance.to_dict()
# create an instance of NotFoundErrorCause from a dict
not_found_error_cause_from_dict = NotFoundErrorCause.from_dict(not_found_error_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


