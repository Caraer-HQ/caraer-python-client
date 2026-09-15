# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**deleted_at** | **int** |  | [optional] 
**created_by_uuid** | **str** |  | [optional] 
**updated_by_uuid** | **str** |  | [optional] 
**deleted_by_uuid** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**filters_string** | **str** |  | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) |  | [optional] 
**member_count** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**complete** | **bool** |  | [optional] 
**uuid** | **str** |  | 

## Example

```python
from caraer_client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


