# FilterGroup

A DTO that defines a group of filter items used for record filtering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**FilterItem**](FilterItem.md) | A set of filter items included in the group. | [optional] 

## Example

```python
from caraer_client.models.filter_group import FilterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FilterGroup from a JSON string
filter_group_instance = FilterGroup.from_json(json)
# print the JSON string representation of the object
print(FilterGroup.to_json())

# convert the object into a dict
filter_group_dict = filter_group_instance.to_dict()
# create an instance of FilterGroup from a dict
filter_group_from_dict = FilterGroup.from_dict(filter_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


