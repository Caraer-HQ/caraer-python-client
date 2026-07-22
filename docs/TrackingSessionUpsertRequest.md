# TrackingSessionUpsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visitor_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.tracking_session_upsert_request import TrackingSessionUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingSessionUpsertRequest from a JSON string
tracking_session_upsert_request_instance = TrackingSessionUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(TrackingSessionUpsertRequest.to_json())

# convert the object into a dict
tracking_session_upsert_request_dict = tracking_session_upsert_request_instance.to_dict()
# create an instance of TrackingSessionUpsertRequest from a dict
tracking_session_upsert_request_from_dict = TrackingSessionUpsertRequest.from_dict(tracking_session_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


