# CalendarTeamMemberDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**object_name** | **str** |  | [optional] 
**has_user_trait** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.calendar_team_member_dto import CalendarTeamMemberDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarTeamMemberDTO from a JSON string
calendar_team_member_dto_instance = CalendarTeamMemberDTO.from_json(json)
# print the JSON string representation of the object
print(CalendarTeamMemberDTO.to_json())

# convert the object into a dict
calendar_team_member_dto_dict = calendar_team_member_dto_instance.to_dict()
# create an instance of CalendarTeamMemberDTO from a dict
calendar_team_member_dto_from_dict = CalendarTeamMemberDTO.from_dict(calendar_team_member_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


