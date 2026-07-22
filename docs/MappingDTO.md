# MappingDTO


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
**source_url** | **str** |  | [optional] 
**sync_rate** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 
**mapping_items** | [**List[MappingItemDTO]**](MappingItemDTO.md) |  | [optional] 
**object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) |  | [optional] 
**unpublish_when_not_in_source** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.mapping_dto import MappingDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MappingDTO from a JSON string
mapping_dto_instance = MappingDTO.from_json(json)
# print the JSON string representation of the object
print(MappingDTO.to_json())

# convert the object into a dict
mapping_dto_dict = mapping_dto_instance.to_dict()
# create an instance of MappingDTO from a dict
mapping_dto_from_dict = MappingDTO.from_dict(mapping_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


