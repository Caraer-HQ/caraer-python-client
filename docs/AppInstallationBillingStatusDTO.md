# AppInstallationBillingStatusDTO

Current-period billing status for one installation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**installation_uuid** | **str** |  | [optional] 
**company_uuid** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**selected_pricing_plan_uuid** | **str** |  | [optional] 
**selected_pricing_plan_title** | **str** |  | [optional] 
**pricing_type** | **str** |  | [optional] 
**billing_commitment** | **str** |  | [optional] 
**pending_pricing_plan_uuid** | **str** |  | [optional] 
**pending_effective_at** | **int** |  | [optional] 
**period** | [**AppBillingPeriodDTO**](AppBillingPeriodDTO.md) |  | [optional] 
**line_items** | [**List[AppBillingLineItemStatusDTO]**](AppBillingLineItemStatusDTO.md) |  | [optional] 
**projected_total** | **float** |  | [optional] 
**subscription** | [**AppSubscriptionDTO**](AppSubscriptionDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.app_installation_billing_status_dto import AppInstallationBillingStatusDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstallationBillingStatusDTO from a JSON string
app_installation_billing_status_dto_instance = AppInstallationBillingStatusDTO.from_json(json)
# print the JSON string representation of the object
print(AppInstallationBillingStatusDTO.to_json())

# convert the object into a dict
app_installation_billing_status_dto_dict = app_installation_billing_status_dto_instance.to_dict()
# create an instance of AppInstallationBillingStatusDTO from a dict
app_installation_billing_status_dto_from_dict = AppInstallationBillingStatusDTO.from_dict(app_installation_billing_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


