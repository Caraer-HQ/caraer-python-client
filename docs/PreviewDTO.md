# PreviewDTO

Data transfer object representing a preview entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the preview | [optional] 
**object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | The Caraer object associated with this preview | [optional] 
**record_uuid** | **str** | UUID of the associated record | [optional] 
**primary** | **bool** | Indicates whether this preview is the primary one | [optional] 
**edge_properties** | **Dict[str, Optional[object]]** | Values stored on the relation edge for properties declared on the relation schema. Only present when the preview was loaded through such a relation. | [optional] 
**grid** | **List[List[PreviewItemDTO]]** | Rows of the preview grid | [optional] 
**preview_type** | **str** | Preview type | [optional] 
**profile_image** | [**PropertyDTO**](PropertyDTO.md) | Profile image property | [optional] 
**profile_image_position** | **str** | Profile image position (top, left, right, bottom, background) | [optional] 
**profile_image_styling** | [**PageContentStylingDTO**](PageContentStylingDTO.md) | Style set for the profile image | [optional] 
**first_initial_property** | [**PropertyDTO**](PropertyDTO.md) | First initial property | [optional] 
**second_initial_property** | [**PropertyDTO**](PropertyDTO.md) | Second initial property | [optional] 
**profile_image_value** | **str** | Value of the profile image | [optional] 
**first_initial_property_value** | **str** | Value of the first initial property | [optional] 
**second_initial_property_value** | **str** | Value of the second initial property | [optional] 
**custom_css** | **str** | Custom CSS styles for the preview | [optional] 
**url** | **str** | URL of the preview | [optional] 
**styling** | [**PageContentStylingDTO**](PageContentStylingDTO.md) | The styling of the preview | [optional] 
**sort_property** | **str** | Property name used for server-side list sorting | [optional] 
**sort_value** | **object** |  | [optional] 
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 

## Example

```python
from caraer_client.models.preview_dto import PreviewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewDTO from a JSON string
preview_dto_instance = PreviewDTO.from_json(json)
# print the JSON string representation of the object
print(PreviewDTO.to_json())

# convert the object into a dict
preview_dto_dict = preview_dto_instance.to_dict()
# create an instance of PreviewDTO from a dict
preview_dto_from_dict = PreviewDTO.from_dict(preview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


