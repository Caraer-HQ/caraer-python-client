# AdvancedRecordQueryResponse

Advanced record query response with scores and evidence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**results** | [**List[AdvancedRecordQueryResultItem]**](AdvancedRecordQueryResultItem.md) |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 
**plan** | [**AdvancedRecordQueryPlan**](AdvancedRecordQueryPlan.md) |  | [optional] 
**confidence** | **float** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**diagnostics** | **Dict[str, Optional[object]]** |  | [optional] 

## Example

```python
from caraer_client.models.advanced_record_query_response import AdvancedRecordQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedRecordQueryResponse from a JSON string
advanced_record_query_response_instance = AdvancedRecordQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AdvancedRecordQueryResponse.to_json())

# convert the object into a dict
advanced_record_query_response_dict = advanced_record_query_response_instance.to_dict()
# create an instance of AdvancedRecordQueryResponse from a dict
advanced_record_query_response_from_dict = AdvancedRecordQueryResponse.from_dict(advanced_record_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


