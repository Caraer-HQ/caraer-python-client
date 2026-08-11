# AdvancedRecordQueryPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 
**main_object** | **str** |  | [optional] 
**main_objects** | **List[str]** |  | [optional] 
**query** | **str** |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**sort** | [**List[SortItem]**](SortItem.md) |  | [optional] 
**show** | [**List[ShowItem]**](ShowItem.md) |  | [optional] 
**strategy** | **str** |  | [optional] 
**anchor_record_uuid** | **str** |  | [optional] 
**criteria** | **List[str]** |  | [optional] 
**graph_traversals** | [**List[GraphTraversalSpec]**](GraphTraversalSpec.md) |  | [optional] 
**score_weights** | **Dict[str, float]** |  | [optional] 
**include_evidence** | **bool** |  | [optional] 
**max_traversal_depth** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.advanced_record_query_plan import AdvancedRecordQueryPlan

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedRecordQueryPlan from a JSON string
advanced_record_query_plan_instance = AdvancedRecordQueryPlan.from_json(json)
# print the JSON string representation of the object
print(AdvancedRecordQueryPlan.to_json())

# convert the object into a dict
advanced_record_query_plan_dict = advanced_record_query_plan_instance.to_dict()
# create an instance of AdvancedRecordQueryPlan from a dict
advanced_record_query_plan_from_dict = AdvancedRecordQueryPlan.from_dict(advanced_record_query_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


