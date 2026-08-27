# OAuthRegistrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uris** | **List[str]** |  | [optional] 
**client_name** | **str** |  | [optional] 
**token_endpoint_auth_method** | **str** |  | [optional] 
**application_type** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.o_auth_registration_request import OAuthRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthRegistrationRequest from a JSON string
o_auth_registration_request_instance = OAuthRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthRegistrationRequest.to_json())

# convert the object into a dict
o_auth_registration_request_dict = o_auth_registration_request_instance.to_dict()
# create an instance of OAuthRegistrationRequest from a dict
o_auth_registration_request_from_dict = OAuthRegistrationRequest.from_dict(o_auth_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


