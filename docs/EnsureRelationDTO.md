# EnsureRelationDTO

Atomic ensure-link receipt. UNCHANGED leaves every existing edge property untouched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_uuid** | **str** |  | [optional] 
**to_uuid** | **str** |  | [optional] 
**relation_name** | **str** |  | [optional] 
**outcome** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.ensure_relation_dto import EnsureRelationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EnsureRelationDTO from a JSON string
ensure_relation_dto_instance = EnsureRelationDTO.from_json(json)
# print the JSON string representation of the object
print(EnsureRelationDTO.to_json())

# convert the object into a dict
ensure_relation_dto_dict = ensure_relation_dto_instance.to_dict()
# create an instance of EnsureRelationDTO from a dict
ensure_relation_dto_from_dict = EnsureRelationDTO.from_dict(ensure_relation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


