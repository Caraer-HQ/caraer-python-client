# DigitalIdentityDTO

A DTO representing the digital identity of a company.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light_primary_color** | **str** | The primary color of the company in light mode. | [optional] 
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
**light_font_color** | **str** | The font color of the company in light mode. | [optional] 
**light_secondary_color** | **str** | The secondary color of the company in light mode. | [optional] 
**light_primary100_color** | **str** | The primary 100 color of the company in light mode. | [optional] 
**light_accent_color** | **str** | The accent color of the company in light mode. | [optional] 
**light_black_color** | **str** | The black color of the company in light mode. | [optional] 
**light_gray900_color** | **str** | The gray 900 color of the company in light mode. | [optional] 
**light_gray800_color** | **str** | The gray 800 color of the company in light mode. | [optional] 
**light_gray700_color** | **str** | The gray 700 color of the company in light mode. | [optional] 
**light_gray600_color** | **str** | The gray 600 color of the company in light mode. | [optional] 
**light_gray500_color** | **str** | The gray 500 color of the company in light mode. | [optional] 
**light_gray400_color** | **str** | The gray 400 color of the company in light mode. | [optional] 
**light_gray300_color** | **str** | The gray 300 color of the company in light mode. | [optional] 
**light_gray200_color** | **str** | The gray 200 color of the company in light mode. | [optional] 
**light_gray100_color** | **str** | The gray 100 color of the company in light mode. | [optional] 
**light_gray50_color** | **str** | The gray 50 color of the company in light mode. | [optional] 
**light_white_color** | **str** | The white color of the company in light mode. | [optional] 
**light_background_color** | **str** | The background color of the company in light mode. | [optional] 
**light_destructive_color** | **str** | The destructive color of the company in light mode. | [optional] 
**dark_font_color** | **str** | The font color of the company in dark mode. | [optional] 
**dark_primary_color** | **str** | The primary color of the company in dark mode. | [optional] 
**dark_secondary_color** | **str** | The secondary color of the company in dark mode. | [optional] 
**dark_primary100_color** | **str** | The primary 100 color of the company in dark mode. | [optional] 
**dark_accent_color** | **str** | The accent color of the company in dark mode. | [optional] 
**dark_black_color** | **str** | The black color of the company in dark mode. | [optional] 
**dark_gray900_color** | **str** | The gray 900 color of the company in dark mode. | [optional] 
**dark_gray800_color** | **str** | The gray 800 color of the company in dark mode. | [optional] 
**dark_gray700_color** | **str** | The gray 700 color of the company in dark mode. | [optional] 
**dark_gray600_color** | **str** | The gray 600 color of the company in dark mode. | [optional] 
**dark_gray500_color** | **str** | The gray 500 color of the company in dark mode. | [optional] 
**dark_gray400_color** | **str** | The gray 400 color of the company in dark mode. | [optional] 
**dark_gray300_color** | **str** | The gray 300 color of the company in dark mode. | [optional] 
**dark_gray200_color** | **str** | The gray 200 color of the company in dark mode. | [optional] 
**dark_gray100_color** | **str** | The gray 100 color of the company in dark mode. | [optional] 
**dark_gray50_color** | **str** | The gray 50 color of the company in dark mode. | [optional] 
**dark_white_color** | **str** | The white color of the company in dark mode. | [optional] 
**dark_background_color** | **str** | The background color of the company in dark mode. | [optional] 
**dark_destructive_color** | **str** | The destructive color of the company in dark mode. | [optional] 

## Example

```python
from caraer_client.models.digital_identity_dto import DigitalIdentityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DigitalIdentityDTO from a JSON string
digital_identity_dto_instance = DigitalIdentityDTO.from_json(json)
# print the JSON string representation of the object
print(DigitalIdentityDTO.to_json())

# convert the object into a dict
digital_identity_dto_dict = digital_identity_dto_instance.to_dict()
# create an instance of DigitalIdentityDTO from a dict
digital_identity_dto_from_dict = DigitalIdentityDTO.from_dict(digital_identity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


