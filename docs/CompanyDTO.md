# CompanyDTO

A DTO representing a company with its various settings and details.

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
**details** | [**CompanyDetailsDTO**](CompanyDetailsDTO.md) | The details of the company. | [optional] 
**digital_identity** | [**DigitalIdentityDTO**](DigitalIdentityDTO.md) | The digital identity of the company. | [optional] 
**website_settings** | [**WebsiteSettingsDTO**](WebsiteSettingsDTO.md) | The website settings of the company. | [optional] 
**billing_settings** | [**BillingSettingsDTO**](BillingSettingsDTO.md) | The billing settings of the company. | [optional] 

## Example

```python
from caraer_client.models.company_dto import CompanyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDTO from a JSON string
company_dto_instance = CompanyDTO.from_json(json)
# print the JSON string representation of the object
print(CompanyDTO.to_json())

# convert the object into a dict
company_dto_dict = company_dto_instance.to_dict()
# create an instance of CompanyDTO from a dict
company_dto_from_dict = CompanyDTO.from_dict(company_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


