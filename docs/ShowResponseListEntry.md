# ShowResponseListEntry

Success response (ShowResponseListEntry).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_list_entry import ShowResponseListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListEntry from a JSON string
show_response_list_entry_instance = ShowResponseListEntry.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListEntry.to_json())

# convert the object into a dict
show_response_list_entry_dict = show_response_list_entry_instance.to_dict()
# create an instance of ShowResponseListEntry from a dict
show_response_list_entry_from_dict = ShowResponseListEntry.from_dict(show_response_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


