# AppBillingLineItemStatusDTO

Current-period usage for one pricing line item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**count_type** | **str** |  | [optional] 
**counting_source** | **str** |  | [optional] 
**usage** | **int** |  | [optional] 
**usage_breakdown** | **Dict[str, int]** |  | [optional] 
**included_units** | **int** |  | [optional] 
**overage_units** | **int** |  | [optional] 
**projected_charge** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_billing_line_item_status_dto import AppBillingLineItemStatusDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppBillingLineItemStatusDTO from a JSON string
app_billing_line_item_status_dto_instance = AppBillingLineItemStatusDTO.from_json(json)
# print the JSON string representation of the object
print(AppBillingLineItemStatusDTO.to_json())

# convert the object into a dict
app_billing_line_item_status_dto_dict = app_billing_line_item_status_dto_instance.to_dict()
# create an instance of AppBillingLineItemStatusDTO from a dict
app_billing_line_item_status_dto_from_dict = AppBillingLineItemStatusDTO.from_dict(app_billing_line_item_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


