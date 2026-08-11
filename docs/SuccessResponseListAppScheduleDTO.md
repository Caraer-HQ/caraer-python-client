# SuccessResponseListAppScheduleDTO

Represents a standard successful response with a message and optional data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**List[AppScheduleDTO]**](AppScheduleDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.success_response_list_app_schedule_dto import SuccessResponseListAppScheduleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseListAppScheduleDTO from a JSON string
success_response_list_app_schedule_dto_instance = SuccessResponseListAppScheduleDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseListAppScheduleDTO.to_json())

# convert the object into a dict
success_response_list_app_schedule_dto_dict = success_response_list_app_schedule_dto_instance.to_dict()
# create an instance of SuccessResponseListAppScheduleDTO from a dict
success_response_list_app_schedule_dto_from_dict = SuccessResponseListAppScheduleDTO.from_dict(success_response_list_app_schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


