# TeamDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**member_count** | **int** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**members** | [**List[UserRecordResponseDTO]**](UserRecordResponseDTO.md) |  | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) |  | [optional] 
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

## Example

```python
from caraer_client.models.team_dto import TeamDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDTO from a JSON string
team_dto_instance = TeamDTO.from_json(json)
# print the JSON string representation of the object
print(TeamDTO.to_json())

# convert the object into a dict
team_dto_dict = team_dto_instance.to_dict()
# create an instance of TeamDTO from a dict
team_dto_from_dict = TeamDTO.from_dict(team_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


