# SubscribeWebhookDTO

Data Transfer Object for subscribing to a webhook. This DTO represents the details required to configure a webhook subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the webhook where requests will be sent. | [optional] 
**serverless_function** | [**ServerlessFunctionDTO**](ServerlessFunctionDTO.md) | UUID of the serverless function to invoke when the webhook is triggered (must belong to the same app). | [optional] 
**delivery_mode** | **str** | Delivery mode for this webhook: HTTP (use url) or SERVERLESS (use serverlessFunctionUuid). If omitted, legacy behavior applies based on presence of url/serverlessFunctionUuid. | [optional] 
**wait_until_complete** | **bool** | When true, install or settings save waits for this lifecycle hook to finish and returns the settings it wrote. | [optional] 
**secret** | **str** | The secret used for webhook validation. | [optional] 
**topic** | **str** | The topic for which the webhook is subscribed. | [optional] 
**description** | **str** | Optional human-readable description for this webhook | [optional] 
**webhook_format** | **str** | Webhook payload format (LEGACY, USER_FRIENDLY) | [optional] 
**parse_record** | **bool** | Whether to parse the record before returning it | [optional] 
**filter** | [**Filter**](Filter.md) | Filter criteria for webhook triggers | [optional] 
**include_relations** | **List[str]** | Records to include in webhook payload | [optional] 
**relation_filters** | [**Dict[str, Filter]**](Filter.md) | Filter criteria for relations | [optional] 
**relation_limit** | **int** | Maximum number of relations to include | [optional] 
**retry_enabled** | **bool** | Whether retry is enabled for failed deliveries (defaults to true if omitted) | [optional] 
**max_retries** | **int** | Maximum number of retries | [optional] 
**retry_backoff_ms** | **int** | Retry backoff in milliseconds | [optional] 
**trigger_offset_seconds** | **int** | Offset from the target date in seconds (required for date_due webhooks) | [optional] 
**schedule_direction** | **str** | Whether the webhook fires BEFORE or AFTER the target date | [optional] 
**schedule_recurring** | **str** | Recurrence for date_due webhooks: NONE, DAILY, WEEKLY, MONTHLY, QUARTERLY, HALF_YEARLY, YEARLY, or CRON | [optional] 
**schedule_cron_expression** | **str** | Spring cron expression used when scheduleRecurring is CRON | [optional] 
**schedule_version** | **int** | Internal schedule version incremented when schedule config changes | [optional] 
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 

## Example

```python
from caraer_client.models.subscribe_webhook_dto import SubscribeWebhookDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeWebhookDTO from a JSON string
subscribe_webhook_dto_instance = SubscribeWebhookDTO.from_json(json)
# print the JSON string representation of the object
print(SubscribeWebhookDTO.to_json())

# convert the object into a dict
subscribe_webhook_dto_dict = subscribe_webhook_dto_instance.to_dict()
# create an instance of SubscribeWebhookDTO from a dict
subscribe_webhook_dto_from_dict = SubscribeWebhookDTO.from_dict(subscribe_webhook_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


