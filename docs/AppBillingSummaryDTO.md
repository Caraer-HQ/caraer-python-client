# AppBillingSummaryDTO

Rollup of installation billing status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_count** | **int** |  | [optional] 
**projected_revenue_total** | **float** |  | [optional] 

## Example

```python
from caraer_client.models.app_billing_summary_dto import AppBillingSummaryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppBillingSummaryDTO from a JSON string
app_billing_summary_dto_instance = AppBillingSummaryDTO.from_json(json)
# print the JSON string representation of the object
print(AppBillingSummaryDTO.to_json())

# convert the object into a dict
app_billing_summary_dto_dict = app_billing_summary_dto_instance.to_dict()
# create an instance of AppBillingSummaryDTO from a dict
app_billing_summary_dto_from_dict = AppBillingSummaryDTO.from_dict(app_billing_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


