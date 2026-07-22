# FontVariantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **int** |  | [optional] 
**style** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.font_variant_dto import FontVariantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FontVariantDTO from a JSON string
font_variant_dto_instance = FontVariantDTO.from_json(json)
# print the JSON string representation of the object
print(FontVariantDTO.to_json())

# convert the object into a dict
font_variant_dto_dict = font_variant_dto_instance.to_dict()
# create an instance of FontVariantDTO from a dict
font_variant_dto_from_dict = FontVariantDTO.from_dict(font_variant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


