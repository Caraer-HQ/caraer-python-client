# AppExternalOAuthProviderSummaryDTO

Lightweight external OAuth provider summary (no secrets)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**connection_owner** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_external_o_auth_provider_summary_dto import AppExternalOAuthProviderSummaryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppExternalOAuthProviderSummaryDTO from a JSON string
app_external_o_auth_provider_summary_dto_instance = AppExternalOAuthProviderSummaryDTO.from_json(json)
# print the JSON string representation of the object
print(AppExternalOAuthProviderSummaryDTO.to_json())

# convert the object into a dict
app_external_o_auth_provider_summary_dto_dict = app_external_o_auth_provider_summary_dto_instance.to_dict()
# create an instance of AppExternalOAuthProviderSummaryDTO from a dict
app_external_o_auth_provider_summary_dto_from_dict = AppExternalOAuthProviderSummaryDTO.from_dict(app_external_o_auth_provider_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


