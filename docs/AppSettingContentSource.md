# AppSettingContentSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**serverless_function_uuid** | **str** |  | [optional] 
**serverless_function_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_setting_content_source import AppSettingContentSource

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingContentSource from a JSON string
app_setting_content_source_instance = AppSettingContentSource.from_json(json)
# print the JSON string representation of the object
print(AppSettingContentSource.to_json())

# convert the object into a dict
app_setting_content_source_dict = app_setting_content_source_instance.to_dict()
# create an instance of AppSettingContentSource from a dict
app_setting_content_source_from_dict = AppSettingContentSource.from_dict(app_setting_content_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


