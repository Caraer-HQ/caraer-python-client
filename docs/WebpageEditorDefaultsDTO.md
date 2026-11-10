# WebpageEditorDefaultsDTO

Read-only style, color and font defaults for an authorized webpage editor. Contains no company administration or executable script configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_styles** | [**Dict[str, PageContentStylingDTO]**](PageContentStylingDTO.md) |  | [optional] 
**palette** | [**Palette**](Palette.md) |  | [optional] 
**fonts** | [**List[CustomFontDTO]**](CustomFontDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.webpage_editor_defaults_dto import WebpageEditorDefaultsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageEditorDefaultsDTO from a JSON string
webpage_editor_defaults_dto_instance = WebpageEditorDefaultsDTO.from_json(json)
# print the JSON string representation of the object
print(WebpageEditorDefaultsDTO.to_json())

# convert the object into a dict
webpage_editor_defaults_dto_dict = webpage_editor_defaults_dto_instance.to_dict()
# create an instance of WebpageEditorDefaultsDTO from a dict
webpage_editor_defaults_dto_from_dict = WebpageEditorDefaultsDTO.from_dict(webpage_editor_defaults_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


