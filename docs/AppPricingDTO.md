# AppPricingDTO

Data transfer object for app pricing (flat or tiered)

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
**title** | **str** | Pricing title | [optional] 
**description** | **str** | Pricing description | [optional] 
**pricing_type** | **str** | Pricing type: TIERED or FLAT | [optional] 
**price_per_unit** | **str** | Price per unit (FLAT, e.g. 10.00) | [optional] 
**unit** | **str** | Unit label (FLAT, e.g. document) | [optional] 
**free_units** | **str** | Free units included (FLAT, e.g. 100) | [optional] 
**free_units_period** | **str** | Free units period (FLAT, e.g. month) | [optional] 
**tiers** | [**List[AppTierDTO]**](AppTierDTO.md) | Tiers for tiered pricing (TIERED) | [optional] 

## Example

```python
from caraer_client.models.app_pricing_dto import AppPricingDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppPricingDTO from a JSON string
app_pricing_dto_instance = AppPricingDTO.from_json(json)
# print the JSON string representation of the object
print(AppPricingDTO.to_json())

# convert the object into a dict
app_pricing_dto_dict = app_pricing_dto_instance.to_dict()
# create an instance of AppPricingDTO from a dict
app_pricing_dto_from_dict = AppPricingDTO.from_dict(app_pricing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


