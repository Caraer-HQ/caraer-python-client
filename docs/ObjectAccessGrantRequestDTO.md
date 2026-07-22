# ObjectAccessGrantRequestDTO

Request to grant record-level access on an object to users, teams, and apps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**ObjectAccessGrantSectionDTO**](ObjectAccessGrantSectionDTO.md) | User grants | [optional] 
**teams** | [**ObjectAccessGrantSectionDTO**](ObjectAccessGrantSectionDTO.md) | Team grants | [optional] 
**apps** | [**ObjectAccessGrantSectionDTO**](ObjectAccessGrantSectionDTO.md) | Installed app grants | [optional] 

## Example

```python
from caraer_client.models.object_access_grant_request_dto import ObjectAccessGrantRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAccessGrantRequestDTO from a JSON string
object_access_grant_request_dto_instance = ObjectAccessGrantRequestDTO.from_json(json)
# print the JSON string representation of the object
print(ObjectAccessGrantRequestDTO.to_json())

# convert the object into a dict
object_access_grant_request_dto_dict = object_access_grant_request_dto_instance.to_dict()
# create an instance of ObjectAccessGrantRequestDTO from a dict
object_access_grant_request_dto_from_dict = ObjectAccessGrantRequestDTO.from_dict(object_access_grant_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


