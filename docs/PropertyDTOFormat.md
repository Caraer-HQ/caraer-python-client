# PropertyDTOFormat

Format configuration for the property's display and validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**settings** | [**List[SettingField]**](SettingField.md) |  | [optional] 
**filters** | **List[str]** |  | [optional] 
**rules** | **List[str]** |  | [optional] 
**linked_property** | [**PropertyDTO**](PropertyDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.property_dto_format import PropertyDTOFormat

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyDTOFormat from a JSON string
property_dto_format_instance = PropertyDTOFormat.from_json(json)
# print the JSON string representation of the object
print(PropertyDTOFormat.to_json())

# convert the object into a dict
property_dto_format_dict = property_dto_format_instance.to_dict()
# create an instance of PropertyDTOFormat from a dict
property_dto_format_from_dict = PropertyDTOFormat.from_dict(property_dto_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


