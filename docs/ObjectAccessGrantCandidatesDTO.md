# ObjectAccessGrantCandidatesDTO

Users, teams, and installed apps available for object access grants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[AccessGrantTargetDTO]**](AccessGrantTargetDTO.md) | Company users with HAS_ACCESS_TO | [optional] 
**teams** | [**List[AccessGrantTargetDTO]**](AccessGrantTargetDTO.md) | Teams in the tenant | [optional] 
**apps** | [**List[AccessGrantTargetDTO]**](AccessGrantTargetDTO.md) | Apps installed for the current company | [optional] 

## Example

```python
from caraer_client.models.object_access_grant_candidates_dto import ObjectAccessGrantCandidatesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAccessGrantCandidatesDTO from a JSON string
object_access_grant_candidates_dto_instance = ObjectAccessGrantCandidatesDTO.from_json(json)
# print the JSON string representation of the object
print(ObjectAccessGrantCandidatesDTO.to_json())

# convert the object into a dict
object_access_grant_candidates_dto_dict = object_access_grant_candidates_dto_instance.to_dict()
# create an instance of ObjectAccessGrantCandidatesDTO from a dict
object_access_grant_candidates_dto_from_dict = ObjectAccessGrantCandidatesDTO.from_dict(object_access_grant_candidates_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


