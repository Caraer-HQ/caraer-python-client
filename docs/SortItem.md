# SortItem

Represents a sortable item, including object, relation, property, and sort direction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The name of the object to which this pagination item belongs. | [optional] 
**relation** | **str** | The relationship between objects. | [optional] 
**var_property** | **str** | The name of the property within the object. | [optional] 
**direction** | **str** | The direction for sorting. Can be ASC (ascending) or DESC (descending). | [optional] 

## Example

```python
from caraer_client.models.sort_item import SortItem

# TODO update the JSON string below
json = "{}"
# create an instance of SortItem from a JSON string
sort_item_instance = SortItem.from_json(json)
# print the JSON string representation of the object
print(SortItem.to_json())

# convert the object into a dict
sort_item_dict = sort_item_instance.to_dict()
# create an instance of SortItem from a dict
sort_item_from_dict = SortItem.from_dict(sort_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


