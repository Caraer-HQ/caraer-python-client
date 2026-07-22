# CompanyDetailsDTO

A DTO representing the details of a company.

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
**twitter** | **str** | The twitter/X url of the company. | [optional] 
**linked_in** | **str** | The linkedin url of the company. | [optional] 
**facebook** | **str** | The facebook url of the company. | [optional] 
**youtube** | **str** | The youtube url of the company. | [optional] 
**instagram** | **str** | The instagram url of the company. | [optional] 
**address** | **str** | The address of the company. | [optional] 
**city** | **str** | The city of the company. | [optional] 
**state** | **str** | The state of the company. | [optional] 
**zip** | **str** | The zip code of the company. | [optional] 
**country** | **str** | The country of the company. | [optional] 
**phone** | **str** | The phone number of the company. | [optional] 
**email** | **str** | The email of the company. | [optional] 
**website** | **str** | The website of the company. | [optional] 
**unsubscribe_link** | **str** | The unsubscribe link of the company. | [optional] 
**cookie_policy** | **str** | The cookie policy of the company. | [optional] 
**privacy_policy** | **str** | The privacy policy of the company. | [optional] 
**terms_and_conditions** | **str** | The terms and conditions of the company. | [optional] 
**disclaimer** | **str** | The disclaimer of the company. | [optional] 

## Example

```python
from caraer_client.models.company_details_dto import CompanyDetailsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDetailsDTO from a JSON string
company_details_dto_instance = CompanyDetailsDTO.from_json(json)
# print the JSON string representation of the object
print(CompanyDetailsDTO.to_json())

# convert the object into a dict
company_details_dto_dict = company_details_dto_instance.to_dict()
# create an instance of CompanyDetailsDTO from a dict
company_details_dto_from_dict = CompanyDetailsDTO.from_dict(company_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


