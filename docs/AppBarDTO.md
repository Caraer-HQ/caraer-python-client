# AppBarDTO

Data transfer object for an app bar (location-specific settings and action config)

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
**location** | **str** | Bar location: RECORD_PREVIEW, RECORD_OVERVIEW, RECORD_DETAIL, TOOL_BAR, TRAIT_BAR, RECORD_TRAIT | [optional] 
**iframe_url** | **str** | URL for iframe-based locations (supports {recordUuid}, {object}, {viewId}, {trait}, {companyUuid} placeholders) | [optional] 
**icon** | **str** | Optional icon name/key for this app bar | [optional] 
**description** | **str** | Description shown under the dialog title for action-based bars | [optional] 
**tooltip_label** | **str** | Tooltip label for buttons and sidebar entries | [optional] 
**action_label** | **str** | Primary button label in the action dialog | [optional] 
**settings_schema** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md) | JSON array of AppSettingFieldSchema (field definitions for action locations) | [optional] 
**webhook** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md) | Webhook configuration for action-based locations | [optional] 

## Example

```python
from caraer_client.models.app_bar_dto import AppBarDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppBarDTO from a JSON string
app_bar_dto_instance = AppBarDTO.from_json(json)
# print the JSON string representation of the object
print(AppBarDTO.to_json())

# convert the object into a dict
app_bar_dto_dict = app_bar_dto_instance.to_dict()
# create an instance of AppBarDTO from a dict
app_bar_dto_from_dict = AppBarDTO.from_dict(app_bar_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


