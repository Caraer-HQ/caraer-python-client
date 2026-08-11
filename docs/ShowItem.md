# ShowItem

DTO representing an item with properties defined for displaying and handling in UI related operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The name of the object to which this pagination item belongs. | [optional] 
**relation** | **str** | The relationship between objects. | [optional] 
**relation_direction** | **str** | Optional relation direction: outgoing (related→main), incoming (main→related), or omit for undirected. | [optional] 
**var_property** | **str** | The name of the property within the object. | [optional] 
**separator** | **str** | Separator string used to visually separate this item. | [optional] 
**sticky** | **bool** | Flag indicating whether this item is sticky and will stay fixed in the list. | [optional] [default to False]
**width** | **int** | Width of the item in pixels. | [optional] 
**calculation_function** | **str** | Calculation function used to calculate the value of the item. | [optional] 
**calculation_result** | **object** |  | [optional] 

## Example

```python
from caraer_client.models.show_item import ShowItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShowItem from a JSON string
show_item_instance = ShowItem.from_json(json)
# print the JSON string representation of the object
print(ShowItem.to_json())

# convert the object into a dict
show_item_dict = show_item_instance.to_dict()
# create an instance of ShowItem from a dict
show_item_from_dict = ShowItem.from_dict(show_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


