# TestWebhookRequest

Webhook configuration and test parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md) | Webhook configuration to test (not saved). | 
**record_uuid** | **str** | UUID of the record to base the event on. Omit to auto-resolve from webhook topic. | [optional] 
**event_type** | **str** | Event type to simulate (created, updated, deleted, etc.). | [optional] 
**property_name** | **str** | Property name when simulating property_changed. | [optional] 

## Example

```python
from caraer_client.models.test_webhook_request import TestWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestWebhookRequest from a JSON string
test_webhook_request_instance = TestWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(TestWebhookRequest.to_json())

# convert the object into a dict
test_webhook_request_dict = test_webhook_request_instance.to_dict()
# create an instance of TestWebhookRequest from a dict
test_webhook_request_from_dict = TestWebhookRequest.from_dict(test_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


