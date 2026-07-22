# AppTierDTO

Data transfer object for a pricing tier (plan) within tiered app pricing

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
**start_units** | **str** | Start of unit range (e.g. 0) | [optional] 
**end_units** | **str** | End of unit range (e.g. 1000 or null for unlimited) | [optional] 
**price_per_month** | **str** | Price per month (e.g. 10.00) | [optional] 
**price_per_year** | **str** | Price per year (e.g. 100.00) | [optional] 
**price_per_extra_unit** | **str** | Price per extra unit beyond tier (e.g. 0.01, typically for last tier) | [optional] 

## Example

```python
from caraer_client.models.app_tier_dto import AppTierDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppTierDTO from a JSON string
app_tier_dto_instance = AppTierDTO.from_json(json)
# print the JSON string representation of the object
print(AppTierDTO.to_json())

# convert the object into a dict
app_tier_dto_dict = app_tier_dto_instance.to_dict()
# create an instance of AppTierDTO from a dict
app_tier_dto_from_dict = AppTierDTO.from_dict(app_tier_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


