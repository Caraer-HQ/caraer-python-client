# RelationPillSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Property of the related object used to order its pills. | [optional] 
**direction** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.relation_pill_sort import RelationPillSort

# TODO update the JSON string below
json = "{}"
# create an instance of RelationPillSort from a JSON string
relation_pill_sort_instance = RelationPillSort.from_json(json)
# print the JSON string representation of the object
print(RelationPillSort.to_json())

# convert the object into a dict
relation_pill_sort_dict = relation_pill_sort_instance.to_dict()
# create an instance of RelationPillSort from a dict
relation_pill_sort_from_dict = RelationPillSort.from_dict(relation_pill_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


