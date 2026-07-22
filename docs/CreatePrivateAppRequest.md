# CreatePrivateAppRequest

Private app creation request with label and optional description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The display label for the private app. | 
**description** | **str** | Optional description text for the app. | [optional] 
**auth_method** | **str** | Authentication method (API_KEY default, OAUTH2 for OAuth 2.0) | [optional] 
**oauth_redirect_uris** | **List[str]** | Registered OAuth redirect URIs (required when authMethod is OAUTH2) | [optional] 

## Example

```python
from caraer_client.models.create_private_app_request import CreatePrivateAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrivateAppRequest from a JSON string
create_private_app_request_instance = CreatePrivateAppRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePrivateAppRequest.to_json())

# convert the object into a dict
create_private_app_request_dict = create_private_app_request_instance.to_dict()
# create an instance of CreatePrivateAppRequest from a dict
create_private_app_request_from_dict = CreatePrivateAppRequest.from_dict(create_private_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


