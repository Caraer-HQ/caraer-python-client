# ShowResponseListInstalledAppBarDTO

Success response (ShowResponseListInstalledAppBarDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_list_installed_app_bar_dto import ShowResponseListInstalledAppBarDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListInstalledAppBarDTO from a JSON string
show_response_list_installed_app_bar_dto_instance = ShowResponseListInstalledAppBarDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListInstalledAppBarDTO.to_json())

# convert the object into a dict
show_response_list_installed_app_bar_dto_dict = show_response_list_installed_app_bar_dto_instance.to_dict()
# create an instance of ShowResponseListInstalledAppBarDTO from a dict
show_response_list_installed_app_bar_dto_from_dict = ShowResponseListInstalledAppBarDTO.from_dict(show_response_list_installed_app_bar_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


