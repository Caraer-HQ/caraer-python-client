# AppMeterEventRequest

Manual meter event for a billable line item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_name** | **str** |  | 
**quantity** | **int** | Positive unit count; defaults to 1 | [optional] 
**idempotency_key** | **str** |  | [optional] 
**occurred_at** | **str** | ISO-8601 timestamp; defaults to now | [optional] 
**metadata** | **Dict[str, Optional[object]]** |  | [optional] 

## Example

```python
from caraer_client.models.app_meter_event_request import AppMeterEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppMeterEventRequest from a JSON string
app_meter_event_request_instance = AppMeterEventRequest.from_json(json)
# print the JSON string representation of the object
print(AppMeterEventRequest.to_json())

# convert the object into a dict
app_meter_event_request_dict = app_meter_event_request_instance.to_dict()
# create an instance of AppMeterEventRequest from a dict
app_meter_event_request_from_dict = AppMeterEventRequest.from_dict(app_meter_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


