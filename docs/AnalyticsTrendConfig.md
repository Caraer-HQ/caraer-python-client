# AnalyticsTrendConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**AnalyticsPropertyRef**](AnalyticsPropertyRef.md) |  | [optional] 
**window_days** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.analytics_trend_config import AnalyticsTrendConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsTrendConfig from a JSON string
analytics_trend_config_instance = AnalyticsTrendConfig.from_json(json)
# print the JSON string representation of the object
print(AnalyticsTrendConfig.to_json())

# convert the object into a dict
analytics_trend_config_dict = analytics_trend_config_instance.to_dict()
# create an instance of AnalyticsTrendConfig from a dict
analytics_trend_config_from_dict = AnalyticsTrendConfig.from_dict(analytics_trend_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


