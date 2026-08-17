# AppSettingFieldSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**help_text** | **str** |  | [optional] 
**options** | [**List[SettingOption]**](SettingOption.md) |  | [optional] 
**options_source** | [**AppSettingOptionsSource**](AppSettingOptionsSource.md) |  | [optional] 
**default_value** | **object** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**visible_when** | [**List[AppSettingCondition]**](AppSettingCondition.md) |  | [optional] 
**value** | **object** |  | [optional] 
**has_value** | **bool** |  | [optional] 
**mapping_value** | [**AppSettingFieldMappingStructure**](AppSettingFieldMappingStructure.md) |  | [optional] 
**value_scope** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_setting_field_schema import AppSettingFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingFieldSchema from a JSON string
app_setting_field_schema_instance = AppSettingFieldSchema.from_json(json)
# print the JSON string representation of the object
print(AppSettingFieldSchema.to_json())

# convert the object into a dict
app_setting_field_schema_dict = app_setting_field_schema_instance.to_dict()
# create an instance of AppSettingFieldSchema from a dict
app_setting_field_schema_from_dict = AppSettingFieldSchema.from_dict(app_setting_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


