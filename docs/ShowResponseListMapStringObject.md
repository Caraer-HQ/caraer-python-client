# ShowResponseListMapStringObject

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **List[Dict[str, Optional[object]]]** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_list_map_string_object import ShowResponseListMapStringObject

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListMapStringObject from a JSON string
show_response_list_map_string_object_instance = ShowResponseListMapStringObject.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListMapStringObject.to_json())

# convert the object into a dict
show_response_list_map_string_object_dict = show_response_list_map_string_object_instance.to_dict()
# create an instance of ShowResponseListMapStringObject from a dict
show_response_list_map_string_object_from_dict = ShowResponseListMapStringObject.from_dict(show_response_list_map_string_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


