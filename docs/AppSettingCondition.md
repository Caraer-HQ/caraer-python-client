# AppSettingCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from caraer_client.models.app_setting_condition import AppSettingCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingCondition from a JSON string
app_setting_condition_instance = AppSettingCondition.from_json(json)
# print the JSON string representation of the object
print(AppSettingCondition.to_json())

# convert the object into a dict
app_setting_condition_dict = app_setting_condition_instance.to_dict()
# create an instance of AppSettingCondition from a dict
app_setting_condition_from_dict = AppSettingCondition.from_dict(app_setting_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


