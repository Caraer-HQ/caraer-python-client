# AnalyticsSeriesConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | [**AnalyticsPropertyRef**](AnalyticsPropertyRef.md) |  | [optional] 

## Example

```python
from caraer_client.models.analytics_series_config import AnalyticsSeriesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsSeriesConfig from a JSON string
analytics_series_config_instance = AnalyticsSeriesConfig.from_json(json)
# print the JSON string representation of the object
print(AnalyticsSeriesConfig.to_json())

# convert the object into a dict
analytics_series_config_dict = analytics_series_config_instance.to_dict()
# create an instance of AnalyticsSeriesConfig from a dict
analytics_series_config_from_dict = AnalyticsSeriesConfig.from_dict(analytics_series_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


