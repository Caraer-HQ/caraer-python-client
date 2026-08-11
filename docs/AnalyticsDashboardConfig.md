# AnalyticsDashboardConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 
**columns** | **int** |  | [optional] 
**widgets** | [**List[AnalyticsWidgetConfig]**](AnalyticsWidgetConfig.md) |  | [optional] 

## Example

```python
from caraer_client.models.analytics_dashboard_config import AnalyticsDashboardConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsDashboardConfig from a JSON string
analytics_dashboard_config_instance = AnalyticsDashboardConfig.from_json(json)
# print the JSON string representation of the object
print(AnalyticsDashboardConfig.to_json())

# convert the object into a dict
analytics_dashboard_config_dict = analytics_dashboard_config_instance.to_dict()
# create an instance of AnalyticsDashboardConfig from a dict
analytics_dashboard_config_from_dict = AnalyticsDashboardConfig.from_dict(analytics_dashboard_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


