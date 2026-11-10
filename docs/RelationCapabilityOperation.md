# RelationCapabilityOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** |  | [optional] 
**var_from** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.relation_capability_operation import RelationCapabilityOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RelationCapabilityOperation from a JSON string
relation_capability_operation_instance = RelationCapabilityOperation.from_json(json)
# print the JSON string representation of the object
print(RelationCapabilityOperation.to_json())

# convert the object into a dict
relation_capability_operation_dict = relation_capability_operation_instance.to_dict()
# create an instance of RelationCapabilityOperation from a dict
relation_capability_operation_from_dict = RelationCapabilityOperation.from_dict(relation_capability_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


