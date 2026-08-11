# QueryEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**polarity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**source_object** | **str** |  | [optional] 
**source_record_uuid** | **str** |  | [optional] 
**relation** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**recency_weight** | **float** |  | [optional] 
**confidence** | **float** |  | [optional] 
**properties** | **Dict[str, Optional[object]]** |  | [optional] 
**paths** | [**List[GraphPathEvidence]**](GraphPathEvidence.md) |  | [optional] 

## Example

```python
from caraer_client.models.query_evidence import QueryEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of QueryEvidence from a JSON string
query_evidence_instance = QueryEvidence.from_json(json)
# print the JSON string representation of the object
print(QueryEvidence.to_json())

# convert the object into a dict
query_evidence_dict = query_evidence_instance.to_dict()
# create an instance of QueryEvidence from a dict
query_evidence_from_dict = QueryEvidence.from_dict(query_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


