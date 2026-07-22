# AccessGrantTargetDTO

A user, team, or app that can receive record access on an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the principal | [optional] 
**label** | **str** | Primary display label | [optional] 
**subtitle** | **str** | Secondary line (e.g. email) | [optional] 

## Example

```python
from caraer_client.models.access_grant_target_dto import AccessGrantTargetDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AccessGrantTargetDTO from a JSON string
access_grant_target_dto_instance = AccessGrantTargetDTO.from_json(json)
# print the JSON string representation of the object
print(AccessGrantTargetDTO.to_json())

# convert the object into a dict
access_grant_target_dto_dict = access_grant_target_dto_instance.to_dict()
# create an instance of AccessGrantTargetDTO from a dict
access_grant_target_dto_from_dict = AccessGrantTargetDTO.from_dict(access_grant_target_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


