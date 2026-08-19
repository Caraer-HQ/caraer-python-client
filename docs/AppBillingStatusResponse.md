# AppBillingStatusResponse

Billing status for one or more app installations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**period** | [**AppBillingPeriodDTO**](AppBillingPeriodDTO.md) |  | [optional] 
**installations** | [**List[AppInstallationBillingStatusDTO]**](AppInstallationBillingStatusDTO.md) |  | [optional] 
**summary** | [**AppBillingSummaryDTO**](AppBillingSummaryDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.app_billing_status_response import AppBillingStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppBillingStatusResponse from a JSON string
app_billing_status_response_instance = AppBillingStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AppBillingStatusResponse.to_json())

# convert the object into a dict
app_billing_status_response_dict = app_billing_status_response_instance.to_dict()
# create an instance of AppBillingStatusResponse from a dict
app_billing_status_response_from_dict = AppBillingStatusResponse.from_dict(app_billing_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


