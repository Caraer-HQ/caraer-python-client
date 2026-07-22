# ViewDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** |  | [optional] 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**favorite** | **bool** |  | [optional] 
**team** | **bool** |  | [optional] 
**shared** | **bool** |  | [optional] 
**personal** | **bool** |  | [optional] 
**trait** | **str** |  | [optional] 
**filters** | [**Filter**](Filter.md) |  | [optional] 
**shows** | [**List[ShowItem]**](ShowItem.md) |  | [optional] 
**sorts** | [**List[SortItem]**](SortItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**show_icons** | **bool** |  | [optional] 
**row_height** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**flow_property** | **str** |  | [optional] 
**flow_preview** | **str** |  | [optional] 
**default_view** | **bool** |  | [optional] 
**is_internally_public** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.view_dto import ViewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDTO from a JSON string
view_dto_instance = ViewDTO.from_json(json)
# print the JSON string representation of the object
print(ViewDTO.to_json())

# convert the object into a dict
view_dto_dict = view_dto_instance.to_dict()
# create an instance of ViewDTO from a dict
view_dto_from_dict = ViewDTO.from_dict(view_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


