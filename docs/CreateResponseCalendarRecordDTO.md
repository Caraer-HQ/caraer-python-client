# CreateResponseCalendarRecordDTO

Response for a successful resource creation operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**CalendarRecordDTO**](CalendarRecordDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.create_response_calendar_record_dto import CreateResponseCalendarRecordDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseCalendarRecordDTO from a JSON string
create_response_calendar_record_dto_instance = CreateResponseCalendarRecordDTO.from_json(json)
# print the JSON string representation of the object
print(CreateResponseCalendarRecordDTO.to_json())

# convert the object into a dict
create_response_calendar_record_dto_dict = create_response_calendar_record_dto_instance.to_dict()
# create an instance of CreateResponseCalendarRecordDTO from a dict
create_response_calendar_record_dto_from_dict = CreateResponseCalendarRecordDTO.from_dict(create_response_calendar_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


