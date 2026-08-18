# AppSettingsSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**settings** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.app_settings_section import AppSettingsSection

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingsSection from a JSON string
app_settings_section_instance = AppSettingsSection.from_json(json)
# print the JSON string representation of the object
print(AppSettingsSection.to_json())

# convert the object into a dict
app_settings_section_dict = app_settings_section_instance.to_dict()
# create an instance of AppSettingsSection from a dict
app_settings_section_from_dict = AppSettingsSection.from_dict(app_settings_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


