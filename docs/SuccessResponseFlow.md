# SuccessResponseFlow

Success response (SuccessResponseFlow).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_flow import SuccessResponseFlow

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseFlow from a JSON string
success_response_flow_instance = SuccessResponseFlow.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseFlow.to_json())

# convert the object into a dict
success_response_flow_dict = success_response_flow_instance.to_dict()
# create an instance of SuccessResponseFlow from a dict
success_response_flow_from_dict = SuccessResponseFlow.from_dict(success_response_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


