# AggregateRequest

Aggregation request for analytics charts over Neo4j records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xaxis** | [**AnalyticsAxisConfig**](AnalyticsAxisConfig.md) |  | [optional] 
**yaxis** | [**AnalyticsAxisConfig**](AnalyticsAxisConfig.md) |  | [optional] 
**id** | **str** | Optional client widget id, echoed in batch responses. | [optional] 
**main_object** | **str** |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**query** | **str** |  | [optional] 
**x_axis** | [**AnalyticsAxisConfig**](AnalyticsAxisConfig.md) |  | [optional] 
**y_axis** | [**AnalyticsAxisConfig**](AnalyticsAxisConfig.md) |  | [optional] 
**series** | [**AnalyticsSeriesConfig**](AnalyticsSeriesConfig.md) |  | [optional] 
**limit** | **int** | Optional top-N series limit. For additive metrics (count, countDistinct, sum), keeps the N series with the highest total Y. Null or &lt;&#x3D; 0 means no truncation. | [optional] 
**sort** | **str** |  | [optional] 
**exclude_empty_values** | **bool** | When true, omit null/blank/(empty) category buckets from the response. Useful for bar and pie charts grouped by optional properties. | [optional] 

## Example

```python
from caraer_client.models.aggregate_request import AggregateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateRequest from a JSON string
aggregate_request_instance = AggregateRequest.from_json(json)
# print the JSON string representation of the object
print(AggregateRequest.to_json())

# convert the object into a dict
aggregate_request_dict = aggregate_request_instance.to_dict()
# create an instance of AggregateRequest from a dict
aggregate_request_from_dict = AggregateRequest.from_dict(aggregate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


