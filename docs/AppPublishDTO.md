# AppPublishDTO

Publish and review state for a public app in the marketplace

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
**publish_state** | **str** | Publish state: DRAFT, SUBMITTED, IN_REVIEW, APPROVED, PUBLISHED, REJECTED, CHANGES_REQUESTED | [optional] 
**submitted_at** | **int** | Timestamp when developer submitted for review | [optional] 
**reviewed_at** | **int** | Timestamp when review was completed | [optional] 
**published_at** | **int** | Timestamp when app went live in marketplace | [optional] 
**feedback** | **str** | Feedback shown to developer (e.g. rejection reason) | [optional] 
**reviewer_notes** | **str** | Internal reviewer notes. Only returned for SUPER_ADMIN callers; never exposed to app creators. | [optional] 

## Example

```python
from caraer_client.models.app_publish_dto import AppPublishDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppPublishDTO from a JSON string
app_publish_dto_instance = AppPublishDTO.from_json(json)
# print the JSON string representation of the object
print(AppPublishDTO.to_json())

# convert the object into a dict
app_publish_dto_dict = app_publish_dto_instance.to_dict()
# create an instance of AppPublishDTO from a dict
app_publish_dto_from_dict = AppPublishDTO.from_dict(app_publish_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


