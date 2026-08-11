# AppScheduleDTO

App schedule definition (cron → function)

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
**schedule** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**payload_template** | **str** |  | [optional] 
**serverless_function** | [**ServerlessFunctionRefDTO**](ServerlessFunctionRefDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.app_schedule_dto import AppScheduleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppScheduleDTO from a JSON string
app_schedule_dto_instance = AppScheduleDTO.from_json(json)
# print the JSON string representation of the object
print(AppScheduleDTO.to_json())

# convert the object into a dict
app_schedule_dto_dict = app_schedule_dto_instance.to_dict()
# create an instance of AppScheduleDTO from a dict
app_schedule_dto_from_dict = AppScheduleDTO.from_dict(app_schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


