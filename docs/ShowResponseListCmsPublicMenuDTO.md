# ShowResponseListCmsPublicMenuDTO

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**List[CmsPublicMenuDTO]**](CmsPublicMenuDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_list_cms_public_menu_dto import ShowResponseListCmsPublicMenuDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListCmsPublicMenuDTO from a JSON string
show_response_list_cms_public_menu_dto_instance = ShowResponseListCmsPublicMenuDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListCmsPublicMenuDTO.to_json())

# convert the object into a dict
show_response_list_cms_public_menu_dto_dict = show_response_list_cms_public_menu_dto_instance.to_dict()
# create an instance of ShowResponseListCmsPublicMenuDTO from a dict
show_response_list_cms_public_menu_dto_from_dict = ShowResponseListCmsPublicMenuDTO.from_dict(show_response_list_cms_public_menu_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


