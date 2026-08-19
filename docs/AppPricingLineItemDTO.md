# AppPricingLineItemDTO

Billable line item on an app pricing plan

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
**count_type** | **str** | Count type: meter or static_query | [optional] 
**counting_source** | **str** | Event sources for meter line items: WEBHOOK, MANUAL, WEBHOOK_AND_MANUAL | [optional] 
**unit** | **str** | Unit label (e.g. webhook, document) | [optional] 
**included_units** | **str** | Included units for FLAT line items | [optional] 
**price_per_unit** | **str** | Base price covering included units (FLAT) | [optional] 
**price_per_extra_unit** | **str** | Price per unit above includedUnits (FLAT) | [optional] 
**static_query** | [**AppStaticQueryDTO**](AppStaticQueryDTO.md) | Scheduled Cypher snapshot for static_query line items | [optional] 
**tiers** | [**List[AppTierDTO]**](AppTierDTO.md) | Tiers for TIERED line items | [optional] 

## Example

```python
from caraer_client.models.app_pricing_line_item_dto import AppPricingLineItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppPricingLineItemDTO from a JSON string
app_pricing_line_item_dto_instance = AppPricingLineItemDTO.from_json(json)
# print the JSON string representation of the object
print(AppPricingLineItemDTO.to_json())

# convert the object into a dict
app_pricing_line_item_dto_dict = app_pricing_line_item_dto_instance.to_dict()
# create an instance of AppPricingLineItemDTO from a dict
app_pricing_line_item_dto_from_dict = AppPricingLineItemDTO.from_dict(app_pricing_line_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


