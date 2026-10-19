# AppSubcategoryDTO

Predefined marketplace subcategory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Stable subcategory key stored on AppDetails.subcategories | [optional] 
**label** | **str** | Human-readable subcategory label | [optional] 

## Example

```python
from caraer_client.models.app_subcategory_dto import AppSubcategoryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubcategoryDTO from a JSON string
app_subcategory_dto_instance = AppSubcategoryDTO.from_json(json)
# print the JSON string representation of the object
print(AppSubcategoryDTO.to_json())

# convert the object into a dict
app_subcategory_dto_dict = app_subcategory_dto_instance.to_dict()
# create an instance of AppSubcategoryDTO from a dict
app_subcategory_dto_from_dict = AppSubcategoryDTO.from_dict(app_subcategory_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


