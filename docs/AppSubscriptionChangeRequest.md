# AppSubscriptionChangeRequest

Schedule a plan or commitment change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_plan_uuid** | **str** |  | [optional] 
**target_commitment** | **str** | MONTHLY or ANNUAL | [optional] 

## Example

```python
from caraer_client.models.app_subscription_change_request import AppSubscriptionChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionChangeRequest from a JSON string
app_subscription_change_request_instance = AppSubscriptionChangeRequest.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionChangeRequest.to_json())

# convert the object into a dict
app_subscription_change_request_dict = app_subscription_change_request_instance.to_dict()
# create an instance of AppSubscriptionChangeRequest from a dict
app_subscription_change_request_from_dict = AppSubscriptionChangeRequest.from_dict(app_subscription_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


