# CustomFontDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family_name** | **str** |  | [optional] 
**variants** | [**List[FontVariantDTO]**](FontVariantDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.custom_font_dto import CustomFontDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFontDTO from a JSON string
custom_font_dto_instance = CustomFontDTO.from_json(json)
# print the JSON string representation of the object
print(CustomFontDTO.to_json())

# convert the object into a dict
custom_font_dto_dict = custom_font_dto_instance.to_dict()
# create an instance of CustomFontDTO from a dict
custom_font_dto_from_dict = CustomFontDTO.from_dict(custom_font_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


