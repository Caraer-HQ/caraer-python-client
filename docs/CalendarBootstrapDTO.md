# CalendarBootstrapDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_calendar** | [**CalendarRecordDTO**](CalendarRecordDTO.md) |  | [optional] 
**calendars** | [**List[CalendarRecordDTO]**](CalendarRecordDTO.md) |  | [optional] 
**backfilled** | **int** |  | [optional] 
**team_calendars_created** | **int** |  | [optional] 
**company_calendar_created** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.calendar_bootstrap_dto import CalendarBootstrapDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarBootstrapDTO from a JSON string
calendar_bootstrap_dto_instance = CalendarBootstrapDTO.from_json(json)
# print the JSON string representation of the object
print(CalendarBootstrapDTO.to_json())

# convert the object into a dict
calendar_bootstrap_dto_dict = calendar_bootstrap_dto_instance.to_dict()
# create an instance of CalendarBootstrapDTO from a dict
calendar_bootstrap_dto_from_dict = CalendarBootstrapDTO.from_dict(calendar_bootstrap_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


