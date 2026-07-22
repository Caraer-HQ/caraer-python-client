# RecordDTO

Data Transfer Object for representing a record with dynamic properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**properties** | **Dict[str, Optional[object]]** | A map of property names to their corresponding values for this record. | [optional] 
**user** | [**PublicUserDTO**](PublicUserDTO.md) | The user of the record if the user trait is enabled. | [optional] 
**relations** | [**List[RecordRelationRequestDTO]**](RecordRelationRequestDTO.md) | Relations to create or merge after the record is saved. Each item links to an existing record (uuid) or creates a nested record first. | [optional] 

## Example

```python
from caraer_client.models.record_dto import RecordDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RecordDTO from a JSON string
record_dto_instance = RecordDTO.from_json(json)
# print the JSON string representation of the object
print(RecordDTO.to_json())

# convert the object into a dict
record_dto_dict = record_dto_instance.to_dict()
# create an instance of RecordDTO from a dict
record_dto_from_dict = RecordDTO.from_dict(record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


