# ShowResponseMapStringString

Success response (ShowResponseMapStringString).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_map_string_string import ShowResponseMapStringString

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseMapStringString from a JSON string
show_response_map_string_string_instance = ShowResponseMapStringString.from_json(json)
# print the JSON string representation of the object
print(ShowResponseMapStringString.to_json())

# convert the object into a dict
show_response_map_string_string_dict = show_response_map_string_string_instance.to_dict()
# create an instance of ShowResponseMapStringString from a dict
show_response_map_string_string_from_dict = ShowResponseMapStringString.from_dict(show_response_map_string_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


