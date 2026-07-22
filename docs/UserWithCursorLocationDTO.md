# UserWithCursorLocationDTO

User with cursor location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**cursor_location** | [**CursorLocation**](CursorLocation.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.user_with_cursor_location_dto import UserWithCursorLocationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithCursorLocationDTO from a JSON string
user_with_cursor_location_dto_instance = UserWithCursorLocationDTO.from_json(json)
# print the JSON string representation of the object
print(UserWithCursorLocationDTO.to_json())

# convert the object into a dict
user_with_cursor_location_dto_dict = user_with_cursor_location_dto_instance.to_dict()
# create an instance of UserWithCursorLocationDTO from a dict
user_with_cursor_location_dto_from_dict = UserWithCursorLocationDTO.from_dict(user_with_cursor_location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


