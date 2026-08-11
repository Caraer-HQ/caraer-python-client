# AdvancedRecordQueryResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | **object** |  | [optional] 
**record_uuid** | **str** |  | [optional] 
**object_name** | **str** |  | [optional] 
**scores** | [**ScoreBreakdown**](ScoreBreakdown.md) |  | [optional] 
**criteria** | [**List[CriterionScore]**](CriterionScore.md) |  | [optional] 
**supporting_evidence** | [**List[QueryEvidence]**](QueryEvidence.md) |  | [optional] 
**contradicting_evidence** | [**List[QueryEvidence]**](QueryEvidence.md) |  | [optional] 

## Example

```python
from caraer_client.models.advanced_record_query_result_item import AdvancedRecordQueryResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedRecordQueryResultItem from a JSON string
advanced_record_query_result_item_instance = AdvancedRecordQueryResultItem.from_json(json)
# print the JSON string representation of the object
print(AdvancedRecordQueryResultItem.to_json())

# convert the object into a dict
advanced_record_query_result_item_dict = advanced_record_query_result_item_instance.to_dict()
# create an instance of AdvancedRecordQueryResultItem from a dict
advanced_record_query_result_item_from_dict = AdvancedRecordQueryResultItem.from_dict(advanced_record_query_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


