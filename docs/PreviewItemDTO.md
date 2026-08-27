# PreviewItemDTO

Data Transfer Object for PreviewItem, used for transferring preview details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**PropertyDTO**](PropertyDTO.md) | The property details associated with the preview item. | [optional] 
**text** | **str** | The text content associated with the preview item. | [optional] 
**value** | **object** | The value associated with the preview item. This can hold custom data. | [optional] 
**related_object** | [**PreviewRelatedObjectDTO**](PreviewRelatedObjectDTO.md) | The related object information for the preview item. | [optional] 
**related_object_value** | **object** | The related object value associated with this preview item. | [optional] 
**divider** | **str** | Whether the preview item is a divider. (solid, dashed, dotted, spacer) | [optional] 
**button_text** | **str** | The button text associated with the preview item. | [optional] 
**button_url** | **str** | The button url associated with the preview item. | [optional] 
**button_text_value** | **object** | The button text value associated with the preview item. | [optional] 
**button_url_value** | **object** | The button value associated with the preview item. | [optional] 
**settings** | [**PreviewItemSettingsDTO**](PreviewItemSettingsDTO.md) | The settings associated with the preview item. | [optional] 
**styling** | [**PageContentStylingDTO**](PageContentStylingDTO.md) | The styling associated with the preview item. | [optional] 

## Example

```python
from caraer_client.models.preview_item_dto import PreviewItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewItemDTO from a JSON string
preview_item_dto_instance = PreviewItemDTO.from_json(json)
# print the JSON string representation of the object
print(PreviewItemDTO.to_json())

# convert the object into a dict
preview_item_dto_dict = preview_item_dto_instance.to_dict()
# create an instance of PreviewItemDTO from a dict
preview_item_dto_from_dict = PreviewItemDTO.from_dict(preview_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


