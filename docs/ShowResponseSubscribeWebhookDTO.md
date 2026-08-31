# ShowResponseSubscribeWebhookDTO

Success response (ShowResponseSubscribeWebhookDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_subscribe_webhook_dto import ShowResponseSubscribeWebhookDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseSubscribeWebhookDTO from a JSON string
show_response_subscribe_webhook_dto_instance = ShowResponseSubscribeWebhookDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseSubscribeWebhookDTO.to_json())

# convert the object into a dict
show_response_subscribe_webhook_dto_dict = show_response_subscribe_webhook_dto_instance.to_dict()
# create an instance of ShowResponseSubscribeWebhookDTO from a dict
show_response_subscribe_webhook_dto_from_dict = ShowResponseSubscribeWebhookDTO.from_dict(show_response_subscribe_webhook_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


