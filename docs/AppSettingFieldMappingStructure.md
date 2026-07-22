# AppSettingFieldMappingStructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_name** | **str** |  | [optional] 
**items** | [**List[AppSettingFieldMappingStructureItem]**](AppSettingFieldMappingStructureItem.md) |  | [optional] 

## Example

```python
from caraer_client.models.app_setting_field_mapping_structure import AppSettingFieldMappingStructure

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingFieldMappingStructure from a JSON string
app_setting_field_mapping_structure_instance = AppSettingFieldMappingStructure.from_json(json)
# print the JSON string representation of the object
print(AppSettingFieldMappingStructure.to_json())

# convert the object into a dict
app_setting_field_mapping_structure_dict = app_setting_field_mapping_structure_instance.to_dict()
# create an instance of AppSettingFieldMappingStructure from a dict
app_setting_field_mapping_structure_from_dict = AppSettingFieldMappingStructure.from_dict(app_setting_field_mapping_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


