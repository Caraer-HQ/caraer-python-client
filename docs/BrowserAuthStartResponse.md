# BrowserAuthStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.browser_auth_start_response import BrowserAuthStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserAuthStartResponse from a JSON string
browser_auth_start_response_instance = BrowserAuthStartResponse.from_json(json)
# print the JSON string representation of the object
print(BrowserAuthStartResponse.to_json())

# convert the object into a dict
browser_auth_start_response_dict = browser_auth_start_response_instance.to_dict()
# create an instance of BrowserAuthStartResponse from a dict
browser_auth_start_response_from_dict = BrowserAuthStartResponse.from_dict(browser_auth_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


