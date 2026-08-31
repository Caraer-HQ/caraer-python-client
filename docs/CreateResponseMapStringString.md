# CreateResponseMapStringString

Success response (CreateResponseMapStringString).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.create_response_map_string_string import CreateResponseMapStringString

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseMapStringString from a JSON string
create_response_map_string_string_instance = CreateResponseMapStringString.from_json(json)
# print the JSON string representation of the object
print(CreateResponseMapStringString.to_json())

# convert the object into a dict
create_response_map_string_string_dict = create_response_map_string_string_instance.to_dict()
# create an instance of CreateResponseMapStringString from a dict
create_response_map_string_string_from_dict = CreateResponseMapStringString.from_dict(create_response_map_string_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


