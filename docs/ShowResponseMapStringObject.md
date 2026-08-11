# ShowResponseMapStringObject

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **Dict[str, Optional[object]]** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_map_string_object import ShowResponseMapStringObject

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseMapStringObject from a JSON string
show_response_map_string_object_instance = ShowResponseMapStringObject.from_json(json)
# print the JSON string representation of the object
print(ShowResponseMapStringObject.to_json())

# convert the object into a dict
show_response_map_string_object_dict = show_response_map_string_object_instance.to_dict()
# create an instance of ShowResponseMapStringObject from a dict
show_response_map_string_object_from_dict = ShowResponseMapStringObject.from_dict(show_response_map_string_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


