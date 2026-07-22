# LoadAppSettingOptionsRequest

Request to load dynamic options for a SINGLE_SELECT or MULTI_SELECT setting field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Name of the setting field to load options for. | 
**query** | **str** | Optional search query typed by the installer. | [optional] 
**settings_schema** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md) | Current draft settings schema with values from the installer UI. | 
**app_bar_uuid** | **str** | When loading options for an app bar field, the app bar UUID. | [optional] 

## Example

```python
from caraer_client.models.load_app_setting_options_request import LoadAppSettingOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoadAppSettingOptionsRequest from a JSON string
load_app_setting_options_request_instance = LoadAppSettingOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(LoadAppSettingOptionsRequest.to_json())

# convert the object into a dict
load_app_setting_options_request_dict = load_app_setting_options_request_instance.to_dict()
# create an instance of LoadAppSettingOptionsRequest from a dict
load_app_setting_options_request_from_dict = LoadAppSettingOptionsRequest.from_dict(load_app_setting_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


