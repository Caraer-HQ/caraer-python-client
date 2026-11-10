# RelationCapabilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_uuid** | **str** |  | [optional] 
**pairs** | [**List[RelationCapabilityPair]**](RelationCapabilityPair.md) |  | [optional] 

## Example

```python
from caraer_client.models.relation_capability_request import RelationCapabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelationCapabilityRequest from a JSON string
relation_capability_request_instance = RelationCapabilityRequest.from_json(json)
# print the JSON string representation of the object
print(RelationCapabilityRequest.to_json())

# convert the object into a dict
relation_capability_request_dict = relation_capability_request_instance.to_dict()
# create an instance of RelationCapabilityRequest from a dict
relation_capability_request_from_dict = RelationCapabilityRequest.from_dict(relation_capability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


