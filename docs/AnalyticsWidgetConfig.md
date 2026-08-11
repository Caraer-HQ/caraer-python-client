# AnalyticsWidgetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**chart_type** | **str** |  | [optional] 
**main_object** | **str** |  | [optional] 
**x** | **int** |  | [optional] 
**y** | **int** |  | [optional] 
**w** | **int** |  | [optional] 
**h** | **int** |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**x_axis** | [**AnalyticsAxisConfig**](AnalyticsAxisConfig.md) |  | [optional] 
**y_axis** | [**AnalyticsAxisConfig**](AnalyticsAxisConfig.md) |  | [optional] 
**series** | [**AnalyticsSeriesConfig**](AnalyticsSeriesConfig.md) |  | [optional] 
**comparison_metrics** | [**List[AnalyticsComparisonMetric]**](AnalyticsComparisonMetric.md) |  | [optional] 
**trend** | [**AnalyticsTrendConfig**](AnalyticsTrendConfig.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**sort** | **str** |  | [optional] 
**exclude_empty_values** | **bool** |  | [optional] 
**style** | [**AnalyticsWidgetStyle**](AnalyticsWidgetStyle.md) |  | [optional] 

## Example

```python
from caraer_client.models.analytics_widget_config import AnalyticsWidgetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsWidgetConfig from a JSON string
analytics_widget_config_instance = AnalyticsWidgetConfig.from_json(json)
# print the JSON string representation of the object
print(AnalyticsWidgetConfig.to_json())

# convert the object into a dict
analytics_widget_config_dict = analytics_widget_config_instance.to_dict()
# create an instance of AnalyticsWidgetConfig from a dict
analytics_widget_config_from_dict = AnalyticsWidgetConfig.from_dict(analytics_widget_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


