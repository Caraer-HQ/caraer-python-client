# ShowResponseMapStringBoolean

Success response (ShowResponseMapStringBoolean).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_map_string_boolean import ShowResponseMapStringBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseMapStringBoolean from a JSON string
show_response_map_string_boolean_instance = ShowResponseMapStringBoolean.from_json(json)
# print the JSON string representation of the object
print(ShowResponseMapStringBoolean.to_json())

# convert the object into a dict
show_response_map_string_boolean_dict = show_response_map_string_boolean_instance.to_dict()
# create an instance of ShowResponseMapStringBoolean from a dict
show_response_map_string_boolean_from_dict = ShowResponseMapStringBoolean.from_dict(show_response_map_string_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


