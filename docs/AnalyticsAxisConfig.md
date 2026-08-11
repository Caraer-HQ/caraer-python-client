# AnalyticsAxisConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**AnalyticsPropertyRef**](AnalyticsPropertyRef.md) |  | [optional] 
**time_bucket** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**window_days** | **int** |  | [optional] 
**bin_count** | **int** |  | [optional] 
**metric** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.analytics_axis_config import AnalyticsAxisConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsAxisConfig from a JSON string
analytics_axis_config_instance = AnalyticsAxisConfig.from_json(json)
# print the JSON string representation of the object
print(AnalyticsAxisConfig.to_json())

# convert the object into a dict
analytics_axis_config_dict = analytics_axis_config_instance.to_dict()
# create an instance of AnalyticsAxisConfig from a dict
analytics_axis_config_from_dict = AnalyticsAxisConfig.from_dict(analytics_axis_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


