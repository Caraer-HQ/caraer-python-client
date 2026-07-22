# WebpageEditingStatusDTO

Whether a webpage is currently being edited by another user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locked** | **bool** | True when another user is actively editing this webpage | [optional] 
**editor** | [**UserWithCursorLocationDTO**](UserWithCursorLocationDTO.md) | The user currently editing, when locked is true | [optional] 
**message** | **str** | Human-readable message for the client UI | [optional] 

## Example

```python
from caraer_client.models.webpage_editing_status_dto import WebpageEditingStatusDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageEditingStatusDTO from a JSON string
webpage_editing_status_dto_instance = WebpageEditingStatusDTO.from_json(json)
# print the JSON string representation of the object
print(WebpageEditingStatusDTO.to_json())

# convert the object into a dict
webpage_editing_status_dto_dict = webpage_editing_status_dto_instance.to_dict()
# create an instance of WebpageEditingStatusDTO from a dict
webpage_editing_status_dto_from_dict = WebpageEditingStatusDTO.from_dict(webpage_editing_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


