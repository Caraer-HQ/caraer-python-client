# ShowResponseLoadAppSettingOptionsResponse

Success response (ShowResponseLoadAppSettingOptionsResponse).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_load_app_setting_options_response import ShowResponseLoadAppSettingOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseLoadAppSettingOptionsResponse from a JSON string
show_response_load_app_setting_options_response_instance = ShowResponseLoadAppSettingOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(ShowResponseLoadAppSettingOptionsResponse.to_json())

# convert the object into a dict
show_response_load_app_setting_options_response_dict = show_response_load_app_setting_options_response_instance.to_dict()
# create an instance of ShowResponseLoadAppSettingOptionsResponse from a dict
show_response_load_app_setting_options_response_from_dict = ShowResponseLoadAppSettingOptionsResponse.from_dict(show_response_load_app_setting_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


