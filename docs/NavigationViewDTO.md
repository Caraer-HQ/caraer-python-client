# NavigationViewDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**trait** | **str** |  | [optional] 
**default_view** | **bool** |  | [optional] 
**index** | **int** |  | [optional] 
**favorite** | **bool** |  | [optional] 
**personal** | **bool** |  | [optional] 
**shared** | **bool** |  | [optional] 
**team** | **bool** |  | [optional] 
**is_internally_public** | **bool** |  | [optional] 
**deleted_at** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.navigation_view_dto import NavigationViewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NavigationViewDTO from a JSON string
navigation_view_dto_instance = NavigationViewDTO.from_json(json)
# print the JSON string representation of the object
print(NavigationViewDTO.to_json())

# convert the object into a dict
navigation_view_dto_dict = navigation_view_dto_instance.to_dict()
# create an instance of NavigationViewDTO from a dict
navigation_view_dto_from_dict = NavigationViewDTO.from_dict(navigation_view_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


