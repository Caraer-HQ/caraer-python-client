# MappingItemDTO


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
**source_field** | **str** |  | [optional] 
**target_object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) |  | [optional] 
**target_property** | [**PropertyDTO**](PropertyDTO.md) |  | [optional] 
**conversion_function** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.mapping_item_dto import MappingItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MappingItemDTO from a JSON string
mapping_item_dto_instance = MappingItemDTO.from_json(json)
# print the JSON string representation of the object
print(MappingItemDTO.to_json())

# convert the object into a dict
mapping_item_dto_dict = mapping_item_dto_instance.to_dict()
# create an instance of MappingItemDTO from a dict
mapping_item_dto_from_dict = MappingItemDTO.from_dict(mapping_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


