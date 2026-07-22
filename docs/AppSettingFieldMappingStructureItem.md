# AppSettingFieldMappingStructureItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_label** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**field_help_text** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**allowed_property_types** | **List[str]** |  | [optional] 
**allowed_property_formats** | **List[str]** |  | [optional] 
**property_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_setting_field_mapping_structure_item import AppSettingFieldMappingStructureItem

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingFieldMappingStructureItem from a JSON string
app_setting_field_mapping_structure_item_instance = AppSettingFieldMappingStructureItem.from_json(json)
# print the JSON string representation of the object
print(AppSettingFieldMappingStructureItem.to_json())

# convert the object into a dict
app_setting_field_mapping_structure_item_dict = app_setting_field_mapping_structure_item_instance.to_dict()
# create an instance of AppSettingFieldMappingStructureItem from a dict
app_setting_field_mapping_structure_item_from_dict = AppSettingFieldMappingStructureItem.from_dict(app_setting_field_mapping_structure_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


