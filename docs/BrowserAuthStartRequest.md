# BrowserAuthStartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**code_challenge** | **str** |  | [optional] 
**code_challenge_method** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.browser_auth_start_request import BrowserAuthStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserAuthStartRequest from a JSON string
browser_auth_start_request_instance = BrowserAuthStartRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserAuthStartRequest.to_json())

# convert the object into a dict
browser_auth_start_request_dict = browser_auth_start_request_instance.to_dict()
# create an instance of BrowserAuthStartRequest from a dict
browser_auth_start_request_from_dict = BrowserAuthStartRequest.from_dict(browser_auth_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


