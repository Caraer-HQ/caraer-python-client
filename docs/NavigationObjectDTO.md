# NavigationObjectDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**plural** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**default_trait** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**suites** | **List[str]** |  | [optional] 
**views** | [**List[NavigationViewDTO]**](NavigationViewDTO.md) |  | [optional] 
**traits** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.navigation_object_dto import NavigationObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NavigationObjectDTO from a JSON string
navigation_object_dto_instance = NavigationObjectDTO.from_json(json)
# print the JSON string representation of the object
print(NavigationObjectDTO.to_json())

# convert the object into a dict
navigation_object_dto_dict = navigation_object_dto_instance.to_dict()
# create an instance of NavigationObjectDTO from a dict
navigation_object_dto_from_dict = NavigationObjectDTO.from_dict(navigation_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


