# SuggestAnalyticsWidgetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_name** | **str** |  | [optional] 
**goal** | **str** |  | [optional] 
**existing_widgets** | [**List[ExistingWidgetSummary]**](ExistingWidgetSummary.md) |  | [optional] 

## Example

```python
from caraer_client.models.suggest_analytics_widgets_request import SuggestAnalyticsWidgetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestAnalyticsWidgetsRequest from a JSON string
suggest_analytics_widgets_request_instance = SuggestAnalyticsWidgetsRequest.from_json(json)
# print the JSON string representation of the object
print(SuggestAnalyticsWidgetsRequest.to_json())

# convert the object into a dict
suggest_analytics_widgets_request_dict = suggest_analytics_widgets_request_instance.to_dict()
# create an instance of SuggestAnalyticsWidgetsRequest from a dict
suggest_analytics_widgets_request_from_dict = SuggestAnalyticsWidgetsRequest.from_dict(suggest_analytics_widgets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


