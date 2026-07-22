# SettingOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.setting_option import SettingOption

# TODO update the JSON string below
json = "{}"
# create an instance of SettingOption from a JSON string
setting_option_instance = SettingOption.from_json(json)
# print the JSON string representation of the object
print(SettingOption.to_json())

# convert the object into a dict
setting_option_dict = setting_option_instance.to_dict()
# create an instance of SettingOption from a dict
setting_option_from_dict = SettingOption.from_dict(setting_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


