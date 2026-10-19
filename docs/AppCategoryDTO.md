# AppCategoryDTO

Predefined marketplace main category with subcategories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Stable main category key stored on AppDetails.category | [optional] 
**label** | **str** | Human-readable main category label | [optional] 
**subcategories** | [**List[AppSubcategoryDTO]**](AppSubcategoryDTO.md) | Subcategories available under this main category | [optional] 

## Example

```python
from caraer_client.models.app_category_dto import AppCategoryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppCategoryDTO from a JSON string
app_category_dto_instance = AppCategoryDTO.from_json(json)
# print the JSON string representation of the object
print(AppCategoryDTO.to_json())

# convert the object into a dict
app_category_dto_dict = app_category_dto_instance.to_dict()
# create an instance of AppCategoryDTO from a dict
app_category_dto_from_dict = AppCategoryDTO.from_dict(app_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


