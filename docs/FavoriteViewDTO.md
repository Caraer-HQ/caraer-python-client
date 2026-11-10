# FavoriteViewDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**ObjectReferenceDTO**](ObjectReferenceDTO.md) |  | [optional] 
**view** | [**NavigationViewDTO**](NavigationViewDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.favorite_view_dto import FavoriteViewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteViewDTO from a JSON string
favorite_view_dto_instance = FavoriteViewDTO.from_json(json)
# print the JSON string representation of the object
print(FavoriteViewDTO.to_json())

# convert the object into a dict
favorite_view_dto_dict = favorite_view_dto_instance.to_dict()
# create an instance of FavoriteViewDTO from a dict
favorite_view_dto_from_dict = FavoriteViewDTO.from_dict(favorite_view_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


