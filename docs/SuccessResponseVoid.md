# SuccessResponseVoid

Represents a standard successful response with a message and optional data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_void import SuccessResponseVoid

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseVoid from a JSON string
success_response_void_instance = SuccessResponseVoid.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseVoid.to_json())

# convert the object into a dict
success_response_void_dict = success_response_void_instance.to_dict()
# create an instance of SuccessResponseVoid from a dict
success_response_void_from_dict = SuccessResponseVoid.from_dict(success_response_void_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


