# AppBarIframeSessionRequest

Request body for creating an iframe session token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Object name in context | [optional] 
**record_uuid** | **str** | UUID of the record in context | [optional] 
**view_id** | **str** | View ID in context | [optional] 
**trait** | **str** | Trait name in context | [optional] 
**view_data** | **Dict[str, Optional[object]]** | Current view data for rebuilding the active index | [optional] 

## Example

```python
from caraer_client.models.app_bar_iframe_session_request import AppBarIframeSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppBarIframeSessionRequest from a JSON string
app_bar_iframe_session_request_instance = AppBarIframeSessionRequest.from_json(json)
# print the JSON string representation of the object
print(AppBarIframeSessionRequest.to_json())

# convert the object into a dict
app_bar_iframe_session_request_dict = app_bar_iframe_session_request_instance.to_dict()
# create an instance of AppBarIframeSessionRequest from a dict
app_bar_iframe_session_request_from_dict = AppBarIframeSessionRequest.from_dict(app_bar_iframe_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


