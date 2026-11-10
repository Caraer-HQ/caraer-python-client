# RelationCapabilityPairCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**link** | [**RelationCapabilityOperation**](RelationCapabilityOperation.md) |  | [optional] 
**unlink** | [**RelationCapabilityOperation**](RelationCapabilityOperation.md) |  | [optional] 
**primary** | [**RelationCapabilityPrimary**](RelationCapabilityPrimary.md) |  | [optional] 
**edges** | [**RelationCapabilityEdges**](RelationCapabilityEdges.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**link_attempt_permitted** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.relation_capability_pair_capability import RelationCapabilityPairCapability

# TODO update the JSON string below
json = "{}"
# create an instance of RelationCapabilityPairCapability from a JSON string
relation_capability_pair_capability_instance = RelationCapabilityPairCapability.from_json(json)
# print the JSON string representation of the object
print(RelationCapabilityPairCapability.to_json())

# convert the object into a dict
relation_capability_pair_capability_dict = relation_capability_pair_capability_instance.to_dict()
# create an instance of RelationCapabilityPairCapability from a dict
relation_capability_pair_capability_from_dict = RelationCapabilityPairCapability.from_dict(relation_capability_pair_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


