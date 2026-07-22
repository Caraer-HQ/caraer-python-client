# AppBarIframeSessionValidateRequest

Request body for validating an iframe session token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Opaque iframe session token from the iframe URL | [optional] 

## Example

```python
from caraer_client.models.app_bar_iframe_session_validate_request import AppBarIframeSessionValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppBarIframeSessionValidateRequest from a JSON string
app_bar_iframe_session_validate_request_instance = AppBarIframeSessionValidateRequest.from_json(json)
# print the JSON string representation of the object
print(AppBarIframeSessionValidateRequest.to_json())

# convert the object into a dict
app_bar_iframe_session_validate_request_dict = app_bar_iframe_session_validate_request_instance.to_dict()
# create an instance of AppBarIframeSessionValidateRequest from a dict
app_bar_iframe_session_validate_request_from_dict = AppBarIframeSessionValidateRequest.from_dict(app_bar_iframe_session_validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


