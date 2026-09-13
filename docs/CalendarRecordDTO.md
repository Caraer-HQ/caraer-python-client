# CalendarRecordDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** |  | [optional] 
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**color_hex** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**owner_uuid** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 
**owned_by_current_user** | **bool** |  | [optional] 
**team_uuid** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 
**company_calendar** | **bool** |  | [optional] 
**company_name** | **str** |  | [optional] 
**members** | [**List[CalendarTeamMemberDTO]**](CalendarTeamMemberDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.calendar_record_dto import CalendarRecordDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarRecordDTO from a JSON string
calendar_record_dto_instance = CalendarRecordDTO.from_json(json)
# print the JSON string representation of the object
print(CalendarRecordDTO.to_json())

# convert the object into a dict
calendar_record_dto_dict = calendar_record_dto_instance.to_dict()
# create an instance of CalendarRecordDTO from a dict
calendar_record_dto_from_dict = CalendarRecordDTO.from_dict(calendar_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


