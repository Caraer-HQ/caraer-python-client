# AdvancedRecordQueryRequest

Advanced record query. Provide either question or plan, not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Natural-language question to plan and execute. | [optional] 
**plan** | [**AdvancedRecordQueryPlan**](AdvancedRecordQueryPlan.md) | Validated declarative query plan. | [optional] 
**main_object** | **str** | Optional main object hint. Use mainObjects for multi-type queries. | [optional] 
**main_objects** | **List[str]** | Optional object list for multi-type queries (e.g. candidate and vacancy together). | [optional] 
**strategy** | **str** |  | [optional] 
**page** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**preview** | **str** |  | [optional] 
**parse** | **object** |  | [optional] 
**archived** | **bool** |  | [optional] 
**explain** | **bool** | When true, include normalized plan, scores, and evidence. | [optional] 
**record_return_format** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.advanced_record_query_request import AdvancedRecordQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedRecordQueryRequest from a JSON string
advanced_record_query_request_instance = AdvancedRecordQueryRequest.from_json(json)
# print the JSON string representation of the object
print(AdvancedRecordQueryRequest.to_json())

# convert the object into a dict
advanced_record_query_request_dict = advanced_record_query_request_instance.to_dict()
# create an instance of AdvancedRecordQueryRequest from a dict
advanced_record_query_request_from_dict = AdvancedRecordQueryRequest.from_dict(advanced_record_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


