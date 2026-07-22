# WebMenuDTO

Data transfer object representing the structure of a web menu

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**title** | **str** | The title of the web menu | [optional] 
**active** | **bool** | Indicates whether the web menu is active | [optional] 
**environments** | **List[str]** | The environments of the web menu | [optional] 
**location** | **str** | The location of the web menu in the UI, e.g., &#39;footer_block_1&#39; or &#39;header&#39; | [optional] 
**urls** | **List[Dict[str, str]]** |  | [optional] 
**items** | [**List[WebMenuItem]**](WebMenuItem.md) |  | [optional] 
**text** | **str** | The text of the web menu | [optional] 

## Example

```python
from caraer_client.models.web_menu_dto import WebMenuDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebMenuDTO from a JSON string
web_menu_dto_instance = WebMenuDTO.from_json(json)
# print the JSON string representation of the object
print(WebMenuDTO.to_json())

# convert the object into a dict
web_menu_dto_dict = web_menu_dto_instance.to_dict()
# create an instance of WebMenuDTO from a dict
web_menu_dto_from_dict = WebMenuDTO.from_dict(web_menu_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


