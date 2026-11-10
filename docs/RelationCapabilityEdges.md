# RelationCapabilityEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_to_target** | [**RelationCapabilityEdge**](RelationCapabilityEdge.md) |  | [optional] 
**target_to_source** | [**RelationCapabilityEdge**](RelationCapabilityEdge.md) |  | [optional] 

## Example

```python
from caraer_client.models.relation_capability_edges import RelationCapabilityEdges

# TODO update the JSON string below
json = "{}"
# create an instance of RelationCapabilityEdges from a JSON string
relation_capability_edges_instance = RelationCapabilityEdges.from_json(json)
# print the JSON string representation of the object
print(RelationCapabilityEdges.to_json())

# convert the object into a dict
relation_capability_edges_dict = relation_capability_edges_instance.to_dict()
# create an instance of RelationCapabilityEdges from a dict
relation_capability_edges_from_dict = RelationCapabilityEdges.from_dict(relation_capability_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


