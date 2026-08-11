# GraphTraversalSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | [optional] 
**target_object** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**max_depth** | **int** |  | [optional] 
**include_lifecycle** | **bool** |  | [optional] 
**include_activities** | **bool** |  | [optional] 
**per_relation_limit** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.graph_traversal_spec import GraphTraversalSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GraphTraversalSpec from a JSON string
graph_traversal_spec_instance = GraphTraversalSpec.from_json(json)
# print the JSON string representation of the object
print(GraphTraversalSpec.to_json())

# convert the object into a dict
graph_traversal_spec_dict = graph_traversal_spec_instance.to_dict()
# create an instance of GraphTraversalSpec from a dict
graph_traversal_spec_from_dict = GraphTraversalSpec.from_dict(graph_traversal_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


