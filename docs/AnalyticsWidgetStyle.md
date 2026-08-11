# AnalyticsWidgetStyle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_legend** | **bool** |  | [optional] 
**show_grid** | **bool** |  | [optional] 
**show_value_labels** | **bool** |  | [optional] 
**bar_orientation** | **str** |  | [optional] 
**bar_grouping** | **str** |  | [optional] 
**colors** | **Dict[str, str]** |  | [optional] 
**reference_lines** | [**List[AnalyticsReferenceLine]**](AnalyticsReferenceLine.md) |  | [optional] 

## Example

```python
from caraer_client.models.analytics_widget_style import AnalyticsWidgetStyle

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsWidgetStyle from a JSON string
analytics_widget_style_instance = AnalyticsWidgetStyle.from_json(json)
# print the JSON string representation of the object
print(AnalyticsWidgetStyle.to_json())

# convert the object into a dict
analytics_widget_style_dict = analytics_widget_style_instance.to_dict()
# create an instance of AnalyticsWidgetStyle from a dict
analytics_widget_style_from_dict = AnalyticsWidgetStyle.from_dict(analytics_widget_style_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


