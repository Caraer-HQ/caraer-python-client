# TrackingEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visitor_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**ts** | **int** |  | [optional] 
**page_url** | **str** |  | [optional] 
**page_title** | **str** |  | [optional] 
**webpage_uuid** | **str** |  | [optional] 
**record_uuid** | **str** |  | [optional] 
**form_uuid** | **str** |  | [optional] 
**form_name** | **str** |  | [optional] 
**utm** | **Dict[str, str]** |  | [optional] 
**referrer** | **str** |  | [optional] 
**scroll_pct** | **int** |  | [optional] 
**time_on_page** | **int** |  | [optional] 
**active_time** | **int** |  | [optional] 
**cta_id** | **str** |  | [optional] 
**cta_label** | **str** |  | [optional] 
**step_index** | **int** |  | [optional] 
**step_title** | **str** |  | [optional] 
**progress_pct** | **int** |  | [optional] 
**completed_fields_count** | **int** |  | [optional] 
**consent_choice** | **str** |  | [optional] 
**requested_route** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.tracking_event_request import TrackingEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingEventRequest from a JSON string
tracking_event_request_instance = TrackingEventRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingEventRequest.to_json())

# convert the object into a dict
tracking_event_request_dict = tracking_event_request_instance.to_dict()
# create an instance of TrackingEventRequest from a dict
tracking_event_request_from_dict = TrackingEventRequest.from_dict(tracking_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


