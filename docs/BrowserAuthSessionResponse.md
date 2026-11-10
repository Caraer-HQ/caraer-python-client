# BrowserAuthSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**user** | [**UserDTO**](UserDTO.md) |  | [optional] 
**company_uuid** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.browser_auth_session_response import BrowserAuthSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserAuthSessionResponse from a JSON string
browser_auth_session_response_instance = BrowserAuthSessionResponse.from_json(json)
# print the JSON string representation of the object
print(BrowserAuthSessionResponse.to_json())

# convert the object into a dict
browser_auth_session_response_dict = browser_auth_session_response_instance.to_dict()
# create an instance of BrowserAuthSessionResponse from a dict
browser_auth_session_response_from_dict = BrowserAuthSessionResponse.from_dict(browser_auth_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


