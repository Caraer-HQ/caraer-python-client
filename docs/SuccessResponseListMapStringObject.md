# SuccessResponseListMapStringObject

Represents a standard successful response with a message and optional data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **List[Dict[str, Optional[object]]]** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.success_response_list_map_string_object import SuccessResponseListMapStringObject

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseListMapStringObject from a JSON string
success_response_list_map_string_object_instance = SuccessResponseListMapStringObject.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseListMapStringObject.to_json())

# convert the object into a dict
success_response_list_map_string_object_dict = success_response_list_map_string_object_instance.to_dict()
# create an instance of SuccessResponseListMapStringObject from a dict
success_response_list_map_string_object_from_dict = SuccessResponseListMapStringObject.from_dict(success_response_list_map_string_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


