# RelationEdgeRequestDTO

Optional relation edge payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_properties** | **Dict[str, Optional[object]]** | Values for properties declared on the relation schema, stored on the edge itself. A null value clears that key. | [optional] 
**primary** | **bool** | When true, marks this relation edge as primary. Overrides the primary query parameter. | [optional] 

## Example

```python
from caraer_client.models.relation_edge_request_dto import RelationEdgeRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RelationEdgeRequestDTO from a JSON string
relation_edge_request_dto_instance = RelationEdgeRequestDTO.from_json(json)
# print the JSON string representation of the object
print(RelationEdgeRequestDTO.to_json())

# convert the object into a dict
relation_edge_request_dto_dict = relation_edge_request_dto_instance.to_dict()
# create an instance of RelationEdgeRequestDTO from a dict
relation_edge_request_dto_from_dict = RelationEdgeRequestDTO.from_dict(relation_edge_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


