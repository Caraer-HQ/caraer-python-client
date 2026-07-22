# PropertyFormat


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

## Example

```python
from caraer_client.models.property_format import PropertyFormat

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFormat from a JSON string
property_format_instance = PropertyFormat.from_json(json)
# print the JSON string representation of the object
print(PropertyFormat.to_json())

# convert the object into a dict
property_format_dict = property_format_instance.to_dict()
# create an instance of PropertyFormat from a dict
property_format_from_dict = PropertyFormat.from_dict(property_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


