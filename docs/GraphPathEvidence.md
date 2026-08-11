# GraphPathEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[Dict[str, Optional[object]]]** |  | [optional] 
**summary** | **str** |  | [optional] 
**relation** | **str** |  | [optional] 
**target_object** | **str** |  | [optional] 
**record_uuid** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.graph_path_evidence import GraphPathEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of GraphPathEvidence from a JSON string
graph_path_evidence_instance = GraphPathEvidence.from_json(json)
# print the JSON string representation of the object
print(GraphPathEvidence.to_json())

# convert the object into a dict
graph_path_evidence_dict = graph_path_evidence_instance.to_dict()
# create an instance of GraphPathEvidence from a dict
graph_path_evidence_from_dict = GraphPathEvidence.from_dict(graph_path_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


