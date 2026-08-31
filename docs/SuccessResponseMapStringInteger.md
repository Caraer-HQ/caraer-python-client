# SuccessResponseMapStringInteger

Success response (SuccessResponseMapStringInteger).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_map_string_integer import SuccessResponseMapStringInteger

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseMapStringInteger from a JSON string
success_response_map_string_integer_instance = SuccessResponseMapStringInteger.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseMapStringInteger.to_json())

# convert the object into a dict
success_response_map_string_integer_dict = success_response_map_string_integer_instance.to_dict()
# create an instance of SuccessResponseMapStringInteger from a dict
success_response_map_string_integer_from_dict = SuccessResponseMapStringInteger.from_dict(success_response_map_string_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


