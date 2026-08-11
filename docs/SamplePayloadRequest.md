# SamplePayloadRequest

Request body for generating a sample webhook payload from a record and event type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_uuid** | **str** | UUID of the record to base the sample payload on. | [optional] 
**event_type** | **str** | Event type to simulate (created, updated, deleted, etc.). | [optional] 

## Example

```python
from caraer_client.models.sample_payload_request import SamplePayloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SamplePayloadRequest from a JSON string
sample_payload_request_instance = SamplePayloadRequest.from_json(json)
# print the JSON string representation of the object
print(SamplePayloadRequest.to_json())

# convert the object into a dict
sample_payload_request_dict = sample_payload_request_instance.to_dict()
# create an instance of SamplePayloadRequest from a dict
sample_payload_request_from_dict = SamplePayloadRequest.from_dict(sample_payload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


