# AppDTO

Full app payload (AppCreatorDTO) to apply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**private_app** | **bool** | Indicates whether this app is private (only available to the creator&#39;s company) | [optional] 
**hide_api_key_field** | **bool** | Whether to hide the API token field in app settings UI | [optional] 
**details** | [**AppDetailsDTO**](AppDetailsDTO.md) | Additional details and specifications about the application | [optional] 
**pricing_plans** | [**List[AppPricingDTO]**](AppPricingDTO.md) | Pricing information for the application | [optional] 
**app_bars** | [**List[AppBarDTO]**](AppBarDTO.md) | App bars (location-specific configuration and actions) | [optional] 
**serverless_functions** | [**List[ServerlessFunctionDTO]**](ServerlessFunctionDTO.md) | Serverless functions owned by this app | [optional] 
**install_webhook** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md) | Webhook triggered when the app is installed | [optional] 
**uninstall_webhook** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md) | Webhook triggered when the app is uninstalled | [optional] 
**rotate_webhook** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md) | Webhook triggered when the app installation token is rotated | [optional] 
**update_webhook** | [**SubscribeWebhookDTO**](SubscribeWebhookDTO.md) | Webhook triggered when an already installed app is saved again | [optional] 
**settings_schema** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md) | JSON array of AppSettingFieldSchema (app-level setting field definitions) | [optional] 
**webhook_rate_limit_per_minute** | **int** | Webhook rate limit per minute | [optional] 
**bill_failed_webhook_requests** | **bool** | Whether failed webhook requests are considered billable for this app | [optional] 
**app_publish** | [**AppPublishDTO**](AppPublishDTO.md) | Publish and review state for the app in the marketplace (creator view) | [optional] 
**has_app** | [**HasAppDTO**](HasAppDTO.md) | Installation link (company–app) with token, scopes, and per-installation settingsValues; present when includeSettings is true | [optional] 
**image** | **str** | URL to the application&#39;s image or icon (derived from details.image) | [optional] 
**url** | **str** | URL where the application can be accessed (derived from details.url) | [optional] 
**category** | **str** | Category the application belongs to (derived from details.category) | [optional] 
**installed** | **bool** | Whether the app is installed for the current company | [optional] 
**required_scopes** | **List[str]** | Required scopes requested by the app (macro patterns or concrete scope strings). | [optional] 
**resolved_required_scopes** | **List[str]** | Resolved concrete required scopes derived from requiredScopes and dynamic availableScopes. | [optional] 
**auth_method** | **str** | Authentication method for this app (API_KEY default, OAUTH2 for OAuth 2.0) | [optional] 
**oauth_client_id** | **str** | OAuth 2.0 client identifier (OAuth apps only) | [optional] 
**oauth_client_secret** | **str** | OAuth 2.0 client secret; only returned once on create or secret rotation | [optional] 
**oauth_client_secret_configured** | **bool** | Whether an OAuth client secret is stored for this app (plain value is not re-readable) | [optional] 
**oauth_redirect_uris** | **List[str]** | Registered OAuth redirect URIs (OAuth apps only) | [optional] 
**oauth_authorize_url** | **str** | OAuth authorization endpoint URL | [optional] 
**oauth_token_url** | **str** | OAuth token endpoint URL | [optional] 
**install_url** | **str** | External URL where end users install this app (e.g. ChatGPT connector page) | [optional] 
**brandmark** | **str** | Square brandmark URL used in compact app surfaces | [optional] 
**description** | **str** | Internal app description used in Caraer admin views | [optional] 

## Example

```python
from caraer_client.models.app_dto import AppDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppDTO from a JSON string
app_dto_instance = AppDTO.from_json(json)
# print the JSON string representation of the object
print(AppDTO.to_json())

# convert the object into a dict
app_dto_dict = app_dto_instance.to_dict()
# create an instance of AppDTO from a dict
app_dto_from_dict = AppDTO.from_dict(app_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


