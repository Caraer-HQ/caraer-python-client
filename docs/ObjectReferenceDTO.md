# ObjectReferenceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**plural** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**default_trait** | **str** |  | [optional] 
**traits** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.object_reference_dto import ObjectReferenceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectReferenceDTO from a JSON string
object_reference_dto_instance = ObjectReferenceDTO.from_json(json)
# print the JSON string representation of the object
print(ObjectReferenceDTO.to_json())

# convert the object into a dict
object_reference_dto_dict = object_reference_dto_instance.to_dict()
# create an instance of ObjectReferenceDTO from a dict
object_reference_dto_from_dict = ObjectReferenceDTO.from_dict(object_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


