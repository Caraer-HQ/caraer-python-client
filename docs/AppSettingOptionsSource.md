# AppSettingOptionsSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**serverless_function_uuid** | **str** |  | [optional] 
**serverless_function_name** | **str** |  | [optional] 
**depends_on** | **List[str]** |  | [optional] 
**searchable** | **bool** |  | [optional] 
**min_query_length** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.app_setting_options_source import AppSettingOptionsSource

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingOptionsSource from a JSON string
app_setting_options_source_instance = AppSettingOptionsSource.from_json(json)
# print the JSON string representation of the object
print(AppSettingOptionsSource.to_json())

# convert the object into a dict
app_setting_options_source_dict = app_setting_options_source_instance.to_dict()
# create an instance of AppSettingOptionsSource from a dict
app_setting_options_source_from_dict = AppSettingOptionsSource.from_dict(app_setting_options_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


