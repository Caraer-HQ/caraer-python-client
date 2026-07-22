# EngagementBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visitor_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**events** | [**List[TrackingEventRequest]**](TrackingEventRequest.md) |  | [optional] 

## Example

```python
from caraer_client.models.engagement_batch_request import EngagementBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementBatchRequest from a JSON string
engagement_batch_request_instance = EngagementBatchRequest.from_json(json)
# print the JSON string representation of the object
print(EngagementBatchRequest.to_json())

# convert the object into a dict
engagement_batch_request_dict = engagement_batch_request_instance.to_dict()
# create an instance of EngagementBatchRequest from a dict
engagement_batch_request_from_dict = EngagementBatchRequest.from_dict(engagement_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


