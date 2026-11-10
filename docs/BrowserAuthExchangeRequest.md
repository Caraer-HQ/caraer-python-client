# BrowserAuthExchangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**code_verifier** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.browser_auth_exchange_request import BrowserAuthExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserAuthExchangeRequest from a JSON string
browser_auth_exchange_request_instance = BrowserAuthExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(BrowserAuthExchangeRequest.to_json())

# convert the object into a dict
browser_auth_exchange_request_dict = browser_auth_exchange_request_instance.to_dict()
# create an instance of BrowserAuthExchangeRequest from a dict
browser_auth_exchange_request_from_dict = BrowserAuthExchangeRequest.from_dict(browser_auth_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


