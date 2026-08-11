# AnalyticsComparisonMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**main_object** | **str** |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**y_axis** | [**AnalyticsAxisConfig**](AnalyticsAxisConfig.md) |  | [optional] 

## Example

```python
from caraer_client.models.analytics_comparison_metric import AnalyticsComparisonMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsComparisonMetric from a JSON string
analytics_comparison_metric_instance = AnalyticsComparisonMetric.from_json(json)
# print the JSON string representation of the object
print(AnalyticsComparisonMetric.to_json())

# convert the object into a dict
analytics_comparison_metric_dict = analytics_comparison_metric_instance.to_dict()
# create an instance of AnalyticsComparisonMetric from a dict
analytics_comparison_metric_from_dict = AnalyticsComparisonMetric.from_dict(analytics_comparison_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


