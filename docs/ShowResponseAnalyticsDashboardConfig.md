# ShowResponseAnalyticsDashboardConfig

Success response (ShowResponseAnalyticsDashboardConfig).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_analytics_dashboard_config import ShowResponseAnalyticsDashboardConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseAnalyticsDashboardConfig from a JSON string
show_response_analytics_dashboard_config_instance = ShowResponseAnalyticsDashboardConfig.from_json(json)
# print the JSON string representation of the object
print(ShowResponseAnalyticsDashboardConfig.to_json())

# convert the object into a dict
show_response_analytics_dashboard_config_dict = show_response_analytics_dashboard_config_instance.to_dict()
# create an instance of ShowResponseAnalyticsDashboardConfig from a dict
show_response_analytics_dashboard_config_from_dict = ShowResponseAnalyticsDashboardConfig.from_dict(show_response_analytics_dashboard_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


