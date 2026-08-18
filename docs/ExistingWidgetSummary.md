# ExistingWidgetSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yproperty** | **str** |  | [optional] 
**xproperty** | **str** |  | [optional] 
**ymetric** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**chart_type** | **str** |  | [optional] 
**x_property** | **str** |  | [optional] 
**y_metric** | **str** |  | [optional] 
**y_property** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.existing_widget_summary import ExistingWidgetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingWidgetSummary from a JSON string
existing_widget_summary_instance = ExistingWidgetSummary.from_json(json)
# print the JSON string representation of the object
print(ExistingWidgetSummary.to_json())

# convert the object into a dict
existing_widget_summary_dict = existing_widget_summary_instance.to_dict()
# create an instance of ExistingWidgetSummary from a dict
existing_widget_summary_from_dict = ExistingWidgetSummary.from_dict(existing_widget_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


