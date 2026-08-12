# RecordRelationRequestDTO

Relation to create when saving a record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation_name** | **str** | Name of the relation type | 
**uuid** | **str** | UUID of an existing record to link to | [optional] 
**properties** | **Dict[str, Optional[object]]** | Properties to update on the existing record referenced by uuid before linking | [optional] 
**edge_properties** | **Dict[str, Optional[object]]** | Values for properties declared on the relation schema, stored on the relation edge itself (not on either record). Omit to leave existing edge values untouched; a null value clears a key. | [optional] 
**record** | [**RecordDTO**](RecordDTO.md) | Nested record to create or update (by uuid or unique properties) before linking | [optional] 
**object_name** | **str** | Object name for nested record create when relation allows multiple target types | [optional] 
**primary** | **bool** | When true, marks this relation edge as primary | [optional] 
**merge** | **bool** | When true, MERGE relation edge instead of CREATE | [optional] 

## Example

```python
from caraer_client.models.record_relation_request_dto import RecordRelationRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RecordRelationRequestDTO from a JSON string
record_relation_request_dto_instance = RecordRelationRequestDTO.from_json(json)
# print the JSON string representation of the object
print(RecordRelationRequestDTO.to_json())

# convert the object into a dict
record_relation_request_dto_dict = record_relation_request_dto_instance.to_dict()
# create an instance of RecordRelationRequestDTO from a dict
record_relation_request_dto_from_dict = RecordRelationRequestDTO.from_dict(record_relation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


