# SyncDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**mappings** | [**List[MappingDTO]**](MappingDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.sync_dto import SyncDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDTO from a JSON string
sync_dto_instance = SyncDTO.from_json(json)
# print the JSON string representation of the object
print(SyncDTO.to_json())

# convert the object into a dict
sync_dto_dict = sync_dto_instance.to_dict()
# create an instance of SyncDTO from a dict
sync_dto_from_dict = SyncDTO.from_dict(sync_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


