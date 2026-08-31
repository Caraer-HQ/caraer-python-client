# ShowResponseListWebpagePickerItemDTO

Success response (ShowResponseListWebpagePickerItemDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_list_webpage_picker_item_dto import ShowResponseListWebpagePickerItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListWebpagePickerItemDTO from a JSON string
show_response_list_webpage_picker_item_dto_instance = ShowResponseListWebpagePickerItemDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListWebpagePickerItemDTO.to_json())

# convert the object into a dict
show_response_list_webpage_picker_item_dto_dict = show_response_list_webpage_picker_item_dto_instance.to_dict()
# create an instance of ShowResponseListWebpagePickerItemDTO from a dict
show_response_list_webpage_picker_item_dto_from_dict = ShowResponseListWebpagePickerItemDTO.from_dict(show_response_list_webpage_picker_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


