# FileListItemDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**last_modified** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.file_list_item_dto import FileListItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FileListItemDTO from a JSON string
file_list_item_dto_instance = FileListItemDTO.from_json(json)
# print the JSON string representation of the object
print(FileListItemDTO.to_json())

# convert the object into a dict
file_list_item_dto_dict = file_list_item_dto_instance.to_dict()
# create an instance of FileListItemDTO from a dict
file_list_item_dto_from_dict = FileListItemDTO.from_dict(file_list_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


