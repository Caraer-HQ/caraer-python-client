# AppBillingPeriodDTO

UTC calendar-month billing window, with pro-rata fields when the subscription started mid-month

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**active_start** | **str** |  | [optional] 
**days_active** | **int** |  | [optional] 
**days_in_period** | **int** |  | [optional] 
**proration_factor** | **float** |  | [optional] 

## Example

```python
from caraer_client.models.app_billing_period_dto import AppBillingPeriodDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppBillingPeriodDTO from a JSON string
app_billing_period_dto_instance = AppBillingPeriodDTO.from_json(json)
# print the JSON string representation of the object
print(AppBillingPeriodDTO.to_json())

# convert the object into a dict
app_billing_period_dto_dict = app_billing_period_dto_instance.to_dict()
# create an instance of AppBillingPeriodDTO from a dict
app_billing_period_dto_from_dict = AppBillingPeriodDTO.from_dict(app_billing_period_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


