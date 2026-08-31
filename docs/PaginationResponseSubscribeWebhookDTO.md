# PaginationResponseSubscribeWebhookDTO

Paginated response (PaginationResponseSubscribeWebhookDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.pagination_response_subscribe_webhook_dto import PaginationResponseSubscribeWebhookDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponseSubscribeWebhookDTO from a JSON string
pagination_response_subscribe_webhook_dto_instance = PaginationResponseSubscribeWebhookDTO.from_json(json)
# print the JSON string representation of the object
print(PaginationResponseSubscribeWebhookDTO.to_json())

# convert the object into a dict
pagination_response_subscribe_webhook_dto_dict = pagination_response_subscribe_webhook_dto_instance.to_dict()
# create an instance of PaginationResponseSubscribeWebhookDTO from a dict
pagination_response_subscribe_webhook_dto_from_dict = PaginationResponseSubscribeWebhookDTO.from_dict(pagination_response_subscribe_webhook_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


