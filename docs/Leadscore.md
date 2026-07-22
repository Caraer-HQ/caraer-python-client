# Leadscore

DTO representing a lead score rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The name of the object to which this pagination item belongs. | [optional] 
**relation** | **str** | The relationship between objects. | [optional] 
**var_property** | **str** | The name of the property within the object. | [optional] 
**relation_included** | **bool** | Specifies whether the relation is included. | [optional] 
**operator** | **str** | Defines the operator used in the filter. Available operators are defined in the API documentation. | [optional] 
**value** | **object** |  | [optional] 
**smart_content** | **bool** | When true, filter fields contain smart content placeholders resolved at runtime. | [optional] 
**smart_value** | **bool** | Whether the value is a smart value | [optional] 
**score** | **int** | The score to assign if the rule is met | [optional] 

## Example

```python
from caraer_client.models.leadscore import Leadscore

# TODO update the JSON string below
json = "{}"
# create an instance of Leadscore from a JSON string
leadscore_instance = Leadscore.from_json(json)
# print the JSON string representation of the object
print(Leadscore.to_json())

# convert the object into a dict
leadscore_dict = leadscore_instance.to_dict()
# create an instance of Leadscore from a dict
leadscore_from_dict = Leadscore.from_dict(leadscore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


