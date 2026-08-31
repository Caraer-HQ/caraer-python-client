# SuccessResponseObject

Success response (SuccessResponseObject).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_object import SuccessResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseObject from a JSON string
success_response_object_instance = SuccessResponseObject.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseObject.to_json())

# convert the object into a dict
success_response_object_dict = success_response_object_instance.to_dict()
# create an instance of SuccessResponseObject from a dict
success_response_object_from_dict = SuccessResponseObject.from_dict(success_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


