# RelationCapabilityPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_uuid** | **str** |  | [optional] 
**relation_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.relation_capability_pair import RelationCapabilityPair

# TODO update the JSON string below
json = "{}"
# create an instance of RelationCapabilityPair from a JSON string
relation_capability_pair_instance = RelationCapabilityPair.from_json(json)
# print the JSON string representation of the object
print(RelationCapabilityPair.to_json())

# convert the object into a dict
relation_capability_pair_dict = relation_capability_pair_instance.to_dict()
# create an instance of RelationCapabilityPair from a dict
relation_capability_pair_from_dict = RelationCapabilityPair.from_dict(relation_capability_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


