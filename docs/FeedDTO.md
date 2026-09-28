# FeedDTO


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
**slug** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**main_object** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**public_token** | **str** |  | [optional] 
**filter** | **object** |  | [optional] 
**filter_json** | **str** |  | [optional] 
**mapping** | **object** |  | [optional] 
**mapping_json** | **str** |  | [optional] 
**parse_record** | **bool** |  | [optional] 
**root_element** | **str** |  | [optional] 
**item_element** | **str** |  | [optional] 
**item_path** | **str** |  | [optional] 
**cache_ttl_seconds** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 
**direction** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**source_auth_type** | **str** |  | [optional] 
**source_auth_key** | **str** |  | [optional] 
**source_auth_value** | **str** |  | [optional] 
**source_auth_username** | **str** |  | [optional] 
**import_interval** | **str** |  | [optional] 
**publish_mode** | **str** |  | [optional] 
**publish_environment** | **str** |  | [optional] 
**publish_filter** | **object** |  | [optional] 
**publish_filter_json** | **str** |  | [optional] 
**unpublish_filter** | **object** |  | [optional] 
**unpublish_filter_json** | **str** |  | [optional] 
**last_import_at** | **int** |  | [optional] 
**last_import_status** | **str** |  | [optional] 
**last_import_message** | **str** |  | [optional] 
**last_import_json** | **str** |  | [optional] 
**import_running_at** | **int** |  | [optional] 
**next_import_at** | **int** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**available_environments** | **List[str]** |  | [optional] 
**sibling_import_feeds** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.feed_dto import FeedDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FeedDTO from a JSON string
feed_dto_instance = FeedDTO.from_json(json)
# print the JSON string representation of the object
print(FeedDTO.to_json())

# convert the object into a dict
feed_dto_dict = feed_dto_instance.to_dict()
# create an instance of FeedDTO from a dict
feed_dto_from_dict = FeedDTO.from_dict(feed_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


