# AppExternalOAuthProviderDTO

Third-party OAuth provider declared on an app

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
**preset** | **str** | Ignored. Set authorizeUrl and tokenUrl explicitly. | [optional] 
**logo** | **str** | Optional logo URL shown on the Connect button | [optional] 
**authorize_url** | **str** |  | [optional] 
**token_url** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**has_client_secret** | **bool** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**pkce** | **bool** |  | [optional] 
**connection_owner** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_external_o_auth_provider_dto import AppExternalOAuthProviderDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppExternalOAuthProviderDTO from a JSON string
app_external_o_auth_provider_dto_instance = AppExternalOAuthProviderDTO.from_json(json)
# print the JSON string representation of the object
print(AppExternalOAuthProviderDTO.to_json())

# convert the object into a dict
app_external_o_auth_provider_dto_dict = app_external_o_auth_provider_dto_instance.to_dict()
# create an instance of AppExternalOAuthProviderDTO from a dict
app_external_o_auth_provider_dto_from_dict = AppExternalOAuthProviderDTO.from_dict(app_external_o_auth_provider_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


