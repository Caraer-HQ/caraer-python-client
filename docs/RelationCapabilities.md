# RelationCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unlink_match** | **str** |  | [optional] 
**primary_reset** | **str** |  | [optional] 
**pairs** | [**List[RelationCapabilityPairCapability]**](RelationCapabilityPairCapability.md) |  | [optional] 
**ensure_link** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.relation_capabilities import RelationCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of RelationCapabilities from a JSON string
relation_capabilities_instance = RelationCapabilities.from_json(json)
# print the JSON string representation of the object
print(RelationCapabilities.to_json())

# convert the object into a dict
relation_capabilities_dict = relation_capabilities_instance.to_dict()
# create an instance of RelationCapabilities from a dict
relation_capabilities_from_dict = RelationCapabilities.from_dict(relation_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


