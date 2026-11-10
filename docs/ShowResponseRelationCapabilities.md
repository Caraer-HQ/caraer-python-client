# ShowResponseRelationCapabilities

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**RelationCapabilities**](RelationCapabilities.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_relation_capabilities import ShowResponseRelationCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseRelationCapabilities from a JSON string
show_response_relation_capabilities_instance = ShowResponseRelationCapabilities.from_json(json)
# print the JSON string representation of the object
print(ShowResponseRelationCapabilities.to_json())

# convert the object into a dict
show_response_relation_capabilities_dict = show_response_relation_capabilities_instance.to_dict()
# create an instance of ShowResponseRelationCapabilities from a dict
show_response_relation_capabilities_from_dict = ShowResponseRelationCapabilities.from_dict(show_response_relation_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


