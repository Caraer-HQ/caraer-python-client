# ScoreBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall** | **float** |  | [optional] 
**structured** | **float** |  | [optional] 
**lexical** | **float** |  | [optional] 
**semantic** | **float** |  | [optional] 
**graph** | **float** |  | [optional] 
**evidence_adjustment** | **float** |  | [optional] 
**confidence** | **float** |  | [optional] 
**components** | **Dict[str, float]** |  | [optional] 

## Example

```python
from caraer_client.models.score_breakdown import ScoreBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreBreakdown from a JSON string
score_breakdown_instance = ScoreBreakdown.from_json(json)
# print the JSON string representation of the object
print(ScoreBreakdown.to_json())

# convert the object into a dict
score_breakdown_dict = score_breakdown_instance.to_dict()
# create an instance of ScoreBreakdown from a dict
score_breakdown_from_dict = ScoreBreakdown.from_dict(score_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


