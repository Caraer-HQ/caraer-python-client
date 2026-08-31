# ShowResponseTraitDTO

Success response (ShowResponseTraitDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_trait_dto import ShowResponseTraitDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseTraitDTO from a JSON string
show_response_trait_dto_instance = ShowResponseTraitDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseTraitDTO.to_json())

# convert the object into a dict
show_response_trait_dto_dict = show_response_trait_dto_instance.to_dict()
# create an instance of ShowResponseTraitDTO from a dict
show_response_trait_dto_from_dict = ShowResponseTraitDTO.from_dict(show_response_trait_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


