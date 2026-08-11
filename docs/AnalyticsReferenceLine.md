# AnalyticsReferenceLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**label** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.analytics_reference_line import AnalyticsReferenceLine

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsReferenceLine from a JSON string
analytics_reference_line_instance = AnalyticsReferenceLine.from_json(json)
# print the JSON string representation of the object
print(AnalyticsReferenceLine.to_json())

# convert the object into a dict
analytics_reference_line_dict = analytics_reference_line_instance.to_dict()
# create an instance of AnalyticsReferenceLine from a dict
analytics_reference_line_from_dict = AnalyticsReferenceLine.from_dict(analytics_reference_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


