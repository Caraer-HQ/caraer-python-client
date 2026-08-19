# AppMeterEventResponse

Recorded meter event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_uuid** | **str** |  | [optional] 
**line_item_name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**period_usage_after** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.app_meter_event_response import AppMeterEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppMeterEventResponse from a JSON string
app_meter_event_response_instance = AppMeterEventResponse.from_json(json)
# print the JSON string representation of the object
print(AppMeterEventResponse.to_json())

# convert the object into a dict
app_meter_event_response_dict = app_meter_event_response_instance.to_dict()
# create an instance of AppMeterEventResponse from a dict
app_meter_event_response_from_dict = AppMeterEventResponse.from_dict(app_meter_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


