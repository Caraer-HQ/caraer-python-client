# AppSettingActionSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**serverless_function_uuid** | **str** |  | [optional] 
**serverless_function_name** | **str** |  | [optional] 
**enqueue** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.app_setting_action_source import AppSettingActionSource

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingActionSource from a JSON string
app_setting_action_source_instance = AppSettingActionSource.from_json(json)
# print the JSON string representation of the object
print(AppSettingActionSource.to_json())

# convert the object into a dict
app_setting_action_source_dict = app_setting_action_source_instance.to_dict()
# create an instance of AppSettingActionSource from a dict
app_setting_action_source_from_dict = AppSettingActionSource.from_dict(app_setting_action_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


