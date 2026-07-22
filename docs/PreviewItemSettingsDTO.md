# PreviewItemSettingsDTO

Data Transfer Object for PreviewItemSettings, used for transferring preview item settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_icon** | **bool** | Whether the preview item should show the icon. | [optional] 
**icon_padding** | **float** | The padding of the icon. | [optional] 
**icon_color** | **str** | The color of the icon. | [optional] 
**icon_size** | **float** | The size of the icon. | [optional] 
**default_value** | **str** | The default value of the preview item. | [optional] 
**editable** | **bool** | Whether this preview property is editable inline. | [optional] 
**help_text** | **str** | The help text of the preview item. | [optional] 
**paragraph** | **str** | The paragraph of the preview item p, h1, h2, h3, h4, h5, h6. | [optional] 
**show_color** | **bool** | Whether the preview item should show the color of the select option. | [optional] 
**show_border** | **bool** | Whether the preview item should show the border around the select option. | [optional] 
**button_type** | **str** | What type the button should be (primary, secondary or tertiary) | [optional] 
**show_favicon** | **bool** | Whether to show the favicon of the button URL. | [optional] 

## Example

```python
from caraer_client.models.preview_item_settings_dto import PreviewItemSettingsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewItemSettingsDTO from a JSON string
preview_item_settings_dto_instance = PreviewItemSettingsDTO.from_json(json)
# print the JSON string representation of the object
print(PreviewItemSettingsDTO.to_json())

# convert the object into a dict
preview_item_settings_dto_dict = preview_item_settings_dto_instance.to_dict()
# create an instance of PreviewItemSettingsDTO from a dict
preview_item_settings_dto_from_dict = PreviewItemSettingsDTO.from_dict(preview_item_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


