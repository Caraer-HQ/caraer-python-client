# SettingField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**dynamic** | **bool** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**options** | [**List[SettingOption]**](SettingOption.md) |  | [optional] 
**value** | **object** |  | [optional] 
**default_value** | **object** |  | [optional] 

## Example

```python
from caraer_client.models.setting_field import SettingField

# TODO update the JSON string below
json = "{}"
# create an instance of SettingField from a JSON string
setting_field_instance = SettingField.from_json(json)
# print the JSON string representation of the object
print(SettingField.to_json())

# convert the object into a dict
setting_field_dict = setting_field_instance.to_dict()
# create an instance of SettingField from a dict
setting_field_from_dict = SettingField.from_dict(setting_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


