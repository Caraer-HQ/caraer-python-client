# RelationDTO

Data transfer object representing a relation between Caraer objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | Unique identifier name for the relation | [optional] 
**label** | **str** | Display label for the relation | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**description** | **str** | Detailed description of the relation&#39;s purpose and usage | [optional] 
**objects** | [**List[CaraerObjectDTO]**](CaraerObjectDTO.md) | Set of Caraer objects that are part of this relation | [optional] 
**immutable** | **bool** | Whether the relation is immutable | [optional] 
**editable** | **bool** | Whether the relation is editable | [optional] 

## Example

```python
from caraer_client.models.relation_dto import RelationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RelationDTO from a JSON string
relation_dto_instance = RelationDTO.from_json(json)
# print the JSON string representation of the object
print(RelationDTO.to_json())

# convert the object into a dict
relation_dto_dict = relation_dto_instance.to_dict()
# create an instance of RelationDTO from a dict
relation_dto_from_dict = RelationDTO.from_dict(relation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


