# AppSubscriptionDTO

Current and pending subscription state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_pricing_plan_uuid** | **str** |  | [optional] 
**billing_commitment** | **str** |  | [optional] 
**contract_start** | **int** |  | [optional] 
**contract_end** | **int** |  | [optional] 
**pending_pricing_plan_uuid** | **str** |  | [optional] 
**pending_billing_commitment** | **str** |  | [optional] 
**pending_effective_at** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_subscription_dto import AppSubscriptionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionDTO from a JSON string
app_subscription_dto_instance = AppSubscriptionDTO.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionDTO.to_json())

# convert the object into a dict
app_subscription_dto_dict = app_subscription_dto_instance.to_dict()
# create an instance of AppSubscriptionDTO from a dict
app_subscription_dto_from_dict = AppSubscriptionDTO.from_dict(app_subscription_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


