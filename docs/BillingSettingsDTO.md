# BillingSettingsDTO

The billing settings of the company.

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
**billing_email** | **str** | The email address of the billing contact. | [optional] 
**address** | **str** | The address of the billing contact. | [optional] 
**city** | **str** | The city of the billing contact. | [optional] 
**state** | **str** | The state of the billing contact. | [optional] 
**zip** | **str** | The zip code of the billing contact. | [optional] 
**country** | **str** | The country of the billing contact. | [optional] 

## Example

```python
from caraer_client.models.billing_settings_dto import BillingSettingsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSettingsDTO from a JSON string
billing_settings_dto_instance = BillingSettingsDTO.from_json(json)
# print the JSON string representation of the object
print(BillingSettingsDTO.to_json())

# convert the object into a dict
billing_settings_dto_dict = billing_settings_dto_instance.to_dict()
# create an instance of BillingSettingsDTO from a dict
billing_settings_dto_from_dict = BillingSettingsDTO.from_dict(billing_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


