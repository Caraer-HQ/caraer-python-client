# ShowResponseRelationDTO

Success response (ShowResponseRelationDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_relation_dto import ShowResponseRelationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseRelationDTO from a JSON string
show_response_relation_dto_instance = ShowResponseRelationDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseRelationDTO.to_json())

# convert the object into a dict
show_response_relation_dto_dict = show_response_relation_dto_instance.to_dict()
# create an instance of ShowResponseRelationDTO from a dict
show_response_relation_dto_from_dict = ShowResponseRelationDTO.from_dict(show_response_relation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


