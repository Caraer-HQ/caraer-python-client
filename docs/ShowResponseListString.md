# ShowResponseListString

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **List[str]** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_list_string import ShowResponseListString

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListString from a JSON string
show_response_list_string_instance = ShowResponseListString.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListString.to_json())

# convert the object into a dict
show_response_list_string_dict = show_response_list_string_instance.to_dict()
# create an instance of ShowResponseListString from a dict
show_response_list_string_from_dict = ShowResponseListString.from_dict(show_response_list_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


