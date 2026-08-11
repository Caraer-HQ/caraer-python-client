# AnalyticsPropertyRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**relation** | **str** |  | [optional] 
**property_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.analytics_property_ref import AnalyticsPropertyRef

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsPropertyRef from a JSON string
analytics_property_ref_instance = AnalyticsPropertyRef.from_json(json)
# print the JSON string representation of the object
print(AnalyticsPropertyRef.to_json())

# convert the object into a dict
analytics_property_ref_dict = analytics_property_ref_instance.to_dict()
# create an instance of AnalyticsPropertyRef from a dict
analytics_property_ref_from_dict = AnalyticsPropertyRef.from_dict(analytics_property_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


