# PreviewRelatedObjectDTO

Data transfer object representing a PreviewRelatedObject, constructed using related object and relation data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | The related object data. | [optional] 
**relation** | [**RelationDTO**](RelationDTO.md) | The type of relation between objects. | [optional] 

## Example

```python
from caraer_client.models.preview_related_object_dto import PreviewRelatedObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewRelatedObjectDTO from a JSON string
preview_related_object_dto_instance = PreviewRelatedObjectDTO.from_json(json)
# print the JSON string representation of the object
print(PreviewRelatedObjectDTO.to_json())

# convert the object into a dict
preview_related_object_dto_dict = preview_related_object_dto_instance.to_dict()
# create an instance of PreviewRelatedObjectDTO from a dict
preview_related_object_dto_from_dict = PreviewRelatedObjectDTO.from_dict(preview_related_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


