# AggregateBatchRequest

Batch aggregation request for loading a dashboard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[AggregateRequest]**](AggregateRequest.md) |  | [optional] 

## Example

```python
from caraer_client.models.aggregate_batch_request import AggregateBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateBatchRequest from a JSON string
aggregate_batch_request_instance = AggregateBatchRequest.from_json(json)
# print the JSON string representation of the object
print(AggregateBatchRequest.to_json())

# convert the object into a dict
aggregate_batch_request_dict = aggregate_batch_request_instance.to_dict()
# create an instance of AggregateBatchRequest from a dict
aggregate_batch_request_from_dict = AggregateBatchRequest.from_dict(aggregate_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


