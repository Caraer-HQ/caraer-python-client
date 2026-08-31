# ShowResponseString

Success response (ShowResponseString).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_string import ShowResponseString

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseString from a JSON string
show_response_string_instance = ShowResponseString.from_json(json)
# print the JSON string representation of the object
print(ShowResponseString.to_json())

# convert the object into a dict
show_response_string_dict = show_response_string_instance.to_dict()
# create an instance of ShowResponseString from a dict
show_response_string_from_dict = ShowResponseString.from_dict(show_response_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


