# NotFoundErrorCauseStackTraceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_loader_name** | **str** |  | [optional] 
**module_name** | **str** |  | [optional] 
**module_version** | **str** |  | [optional] 
**method_name** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**line_number** | **int** |  | [optional] 
**class_name** | **str** |  | [optional] 
**native_method** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.not_found_error_cause_stack_trace_inner import NotFoundErrorCauseStackTraceInner

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundErrorCauseStackTraceInner from a JSON string
not_found_error_cause_stack_trace_inner_instance = NotFoundErrorCauseStackTraceInner.from_json(json)
# print the JSON string representation of the object
print(NotFoundErrorCauseStackTraceInner.to_json())

# convert the object into a dict
not_found_error_cause_stack_trace_inner_dict = not_found_error_cause_stack_trace_inner_instance.to_dict()
# create an instance of NotFoundErrorCauseStackTraceInner from a dict
not_found_error_cause_stack_trace_inner_from_dict = NotFoundErrorCauseStackTraceInner.from_dict(not_found_error_cause_stack_trace_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


