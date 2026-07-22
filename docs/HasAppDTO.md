# HasAppDTO

Installation link between a company and an app (per-installation settings and token)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the installation relationship | [optional] 
**token** | **str** | Installation token | [optional] 
**scopes** | **List[str]** | Scopes granted to this installation | [optional] 
**settings_values** | **str** | Per-installation app setting values (JSON object keyed by setting name) | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) | Per-object record filters for this installation (object name → filter) | [optional] 
**app_bar_visibility** | [**Dict[str, AppBarVisibilityEntry]**](AppBarVisibilityEntry.md) | Per-app-bar placement config keyed by app bar UUID | [optional] 
**oauth_connected** | **bool** | Whether OAuth tokens have been issued for this installation | [optional] 
**oauth_access_token_expires_at** | **int** | OAuth access token expiry (epoch ms), if connected via OAuth | [optional] 
**selected_pricing_plan_uuid** | **str** | UUID of the pricing plan selected for this installation | [optional] 

## Example

```python
from caraer_client.models.has_app_dto import HasAppDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HasAppDTO from a JSON string
has_app_dto_instance = HasAppDTO.from_json(json)
# print the JSON string representation of the object
print(HasAppDTO.to_json())

# convert the object into a dict
has_app_dto_dict = has_app_dto_instance.to_dict()
# create an instance of HasAppDTO from a dict
has_app_dto_from_dict = HasAppDTO.from_dict(has_app_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


