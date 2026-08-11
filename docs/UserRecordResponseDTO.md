# UserRecordResponseDTO

Record response for user API endpoints, including linked user data.

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
**deleted** | **bool** | Whether the record is soft-deleted. | [optional] 
**properties** | [**List[FilledProperty]**](FilledProperty.md) | Record properties for display. | [optional] 
**objects** | **Dict[str, Optional[object]]** | Primary and extended object metadata for this record. | [optional] 
**user** | [**PublicUserDTO**](PublicUserDTO.md) | The user linked to this record when the user trait is enabled. | [optional] 

## Example

```python
from caraer_client.models.user_record_response_dto import UserRecordResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecordResponseDTO from a JSON string
user_record_response_dto_instance = UserRecordResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserRecordResponseDTO.to_json())

# convert the object into a dict
user_record_response_dto_dict = user_record_response_dto_instance.to_dict()
# create an instance of UserRecordResponseDTO from a dict
user_record_response_dto_from_dict = UserRecordResponseDTO.from_dict(user_record_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


