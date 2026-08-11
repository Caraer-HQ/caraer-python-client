# CriterionScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**rationale** | **str** |  | [optional] 
**supporting_evidence** | [**List[QueryEvidence]**](QueryEvidence.md) |  | [optional] 
**contradicting_evidence** | [**List[QueryEvidence]**](QueryEvidence.md) |  | [optional] 

## Example

```python
from caraer_client.models.criterion_score import CriterionScore

# TODO update the JSON string below
json = "{}"
# create an instance of CriterionScore from a JSON string
criterion_score_instance = CriterionScore.from_json(json)
# print the JSON string representation of the object
print(CriterionScore.to_json())

# convert the object into a dict
criterion_score_dict = criterion_score_instance.to_dict()
# create an instance of CriterionScore from a dict
criterion_score_from_dict = CriterionScore.from_dict(criterion_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


