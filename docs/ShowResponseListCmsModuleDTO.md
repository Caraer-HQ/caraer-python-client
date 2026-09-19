# ShowResponseListCmsModuleDTO

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**List[CmsModuleDTO]**](CmsModuleDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_list_cms_module_dto import ShowResponseListCmsModuleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListCmsModuleDTO from a JSON string
show_response_list_cms_module_dto_instance = ShowResponseListCmsModuleDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListCmsModuleDTO.to_json())

# convert the object into a dict
show_response_list_cms_module_dto_dict = show_response_list_cms_module_dto_instance.to_dict()
# create an instance of ShowResponseListCmsModuleDTO from a dict
show_response_list_cms_module_dto_from_dict = ShowResponseListCmsModuleDTO.from_dict(show_response_list_cms_module_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


