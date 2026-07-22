# ObjectAccessGrantSectionDTO

Access grant selection for one principal type (users, teams, or apps).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | UUIDs to grant access to | [optional] 
**global_scopes** | **List[str]** | Record scopes applied to every selected UUID | [optional] 
**overrides** | **Dict[str, List[str]]** | Per-UUID scope overrides merged with globalScopes | [optional] 

## Example

```python
from caraer_client.models.object_access_grant_section_dto import ObjectAccessGrantSectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAccessGrantSectionDTO from a JSON string
object_access_grant_section_dto_instance = ObjectAccessGrantSectionDTO.from_json(json)
# print the JSON string representation of the object
print(ObjectAccessGrantSectionDTO.to_json())

# convert the object into a dict
object_access_grant_section_dto_dict = object_access_grant_section_dto_instance.to_dict()
# create an instance of ObjectAccessGrantSectionDTO from a dict
object_access_grant_section_dto_from_dict = ObjectAccessGrantSectionDTO.from_dict(object_access_grant_section_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


