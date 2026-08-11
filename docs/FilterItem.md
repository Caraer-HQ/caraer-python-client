# FilterItem

DTO representing a filter used in querying records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The name of the object to which this pagination item belongs. | [optional] 
**relation** | **str** | The relationship between objects. | [optional] 
**relation_direction** | **str** | Optional relation direction: outgoing (related→main), incoming (main→related), or omit for undirected. | [optional] 
**var_property** | **str** | The name of the property within the object. | [optional] 
**relation_included** | **bool** | Specifies whether the relation is included. | [optional] 
**operator** | **str** | Defines the operator used in the filter. Available operators are defined in the API documentation. | [optional] 
**value** | **object** |  | [optional] 
**smart_content** | **bool** | When true, filter fields contain smart content placeholders resolved at runtime. | [optional] 
**edge_property** | **bool** | When true, propertyName refers to a property stored on the relation edge itself (declared on the relation schema, e.g. partstat on attendees) instead of a property of the related record. Requires relation and propertyName. | [optional] 

## Example

```python
from caraer_client.models.filter_item import FilterItem

# TODO update the JSON string below
json = "{}"
# create an instance of FilterItem from a JSON string
filter_item_instance = FilterItem.from_json(json)
# print the JSON string representation of the object
print(FilterItem.to_json())

# convert the object into a dict
filter_item_dict = filter_item_instance.to_dict()
# create an instance of FilterItem from a dict
filter_item_from_dict = FilterItem.from_dict(filter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


