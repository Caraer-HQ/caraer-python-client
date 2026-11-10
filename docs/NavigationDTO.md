# NavigationDTO

Authorized application navigation for the currently selected company. Contains no record schema or user configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[NavigationObjectDTO]**](NavigationObjectDTO.md) |  | [optional] 
**suites** | **List[str]** |  | [optional] 
**tools** | [**WebMenuDTO**](WebMenuDTO.md) |  | [optional] 
**settings** | [**WebMenuDTO**](WebMenuDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.navigation_dto import NavigationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NavigationDTO from a JSON string
navigation_dto_instance = NavigationDTO.from_json(json)
# print the JSON string representation of the object
print(NavigationDTO.to_json())

# convert the object into a dict
navigation_dto_dict = navigation_dto_instance.to_dict()
# create an instance of NavigationDTO from a dict
navigation_dto_from_dict = NavigationDTO.from_dict(navigation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


