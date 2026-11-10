# ViewNavigationPreferencesRequest

Personal view navigation overrides. Omitted entries preserve their values; a null entry clears that override and restores the legacy sharing default. Does not change sharing or record access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** |  | [optional] 
**favorites** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from caraer_client.models.view_navigation_preferences_request import ViewNavigationPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ViewNavigationPreferencesRequest from a JSON string
view_navigation_preferences_request_instance = ViewNavigationPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(ViewNavigationPreferencesRequest.to_json())

# convert the object into a dict
view_navigation_preferences_request_dict = view_navigation_preferences_request_instance.to_dict()
# create an instance of ViewNavigationPreferencesRequest from a dict
view_navigation_preferences_request_from_dict = ViewNavigationPreferencesRequest.from_dict(view_navigation_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


