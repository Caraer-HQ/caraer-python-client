# AppBarTriggerRequest

Request body for triggering an action-based app bar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_uuid** | **str** | UUID of the record in context | [optional] 
**object** | **str** | Object name in context | [optional] 
**view_id** | **str** | View ID in context | [optional] 
**trait** | **str** | Trait name in context | [optional] 
**view_data** | **Dict[str, Optional[object]]** | Current view data for rebuilding the active index | [optional] 
**settings_values** | **Dict[str, Optional[object]]** | Values for settingsSchema fields supplied at trigger time | [optional] 

## Example

```python
from caraer_client.models.app_bar_trigger_request import AppBarTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppBarTriggerRequest from a JSON string
app_bar_trigger_request_instance = AppBarTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(AppBarTriggerRequest.to_json())

# convert the object into a dict
app_bar_trigger_request_dict = app_bar_trigger_request_instance.to_dict()
# create an instance of AppBarTriggerRequest from a dict
app_bar_trigger_request_from_dict = AppBarTriggerRequest.from_dict(app_bar_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


