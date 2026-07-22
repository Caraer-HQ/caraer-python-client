# AppDetailsDTO

Detailed DTO representing an application with all available configuration and visibility metadata for the current company context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** | Short marketplace description shown on app cards and detail pages | [optional] 
**image** | **str** |  | [optional] 
**brand_color** | **str** | Hex accent color (#RRGGBB) for installed app-bar action buttons and toolbar icons | [optional] 
**text_color** | **str** | Hex text color (#RRGGBB) for text on brand-colored marketplace UI elements | [optional] 
**url** | **str** |  | [optional] 
**category** | **str** | Main marketplace category key from GET /api/v2/apps/categories | [optional] 
**subcategories** | **List[str]** | Selected subcategory keys under the main category | [optional] 
**privacy_policy** | **str** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**processing_agreement** | **str** |  | [optional] 
**disclaimer** | **str** |  | [optional] 
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
from caraer_client.models.app_details_dto import AppDetailsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppDetailsDTO from a JSON string
app_details_dto_instance = AppDetailsDTO.from_json(json)
# print the JSON string representation of the object
print(AppDetailsDTO.to_json())

# convert the object into a dict
app_details_dto_dict = app_details_dto_instance.to_dict()
# create an instance of AppDetailsDTO from a dict
app_details_dto_from_dict = AppDetailsDTO.from_dict(app_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


