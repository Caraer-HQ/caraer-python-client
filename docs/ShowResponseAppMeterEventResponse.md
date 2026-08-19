# ShowResponseAppMeterEventResponse

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**AppMeterEventResponse**](AppMeterEventResponse.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_app_meter_event_response import ShowResponseAppMeterEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseAppMeterEventResponse from a JSON string
show_response_app_meter_event_response_instance = ShowResponseAppMeterEventResponse.from_json(json)
# print the JSON string representation of the object
print(ShowResponseAppMeterEventResponse.to_json())

# convert the object into a dict
show_response_app_meter_event_response_dict = show_response_app_meter_event_response_instance.to_dict()
# create an instance of ShowResponseAppMeterEventResponse from a dict
show_response_app_meter_event_response_from_dict = ShowResponseAppMeterEventResponse.from_dict(show_response_app_meter_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


