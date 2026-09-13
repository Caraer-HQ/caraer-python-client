# CalendarTeamOptionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**members** | [**List[CalendarTeamMemberDTO]**](CalendarTeamMemberDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.calendar_team_option_dto import CalendarTeamOptionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarTeamOptionDTO from a JSON string
calendar_team_option_dto_instance = CalendarTeamOptionDTO.from_json(json)
# print the JSON string representation of the object
print(CalendarTeamOptionDTO.to_json())

# convert the object into a dict
calendar_team_option_dto_dict = calendar_team_option_dto_instance.to_dict()
# create an instance of CalendarTeamOptionDTO from a dict
calendar_team_option_dto_from_dict = CalendarTeamOptionDTO.from_dict(calendar_team_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


