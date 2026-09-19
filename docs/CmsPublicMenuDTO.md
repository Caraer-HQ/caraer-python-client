# CmsPublicMenuDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**items** | [**List[WebMenuItem]**](WebMenuItem.md) |  | [optional] 

## Example

```python
from caraer_client.models.cms_public_menu_dto import CmsPublicMenuDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPublicMenuDTO from a JSON string
cms_public_menu_dto_instance = CmsPublicMenuDTO.from_json(json)
# print the JSON string representation of the object
print(CmsPublicMenuDTO.to_json())

# convert the object into a dict
cms_public_menu_dto_dict = cms_public_menu_dto_instance.to_dict()
# create an instance of CmsPublicMenuDTO from a dict
cms_public_menu_dto_from_dict = CmsPublicMenuDTO.from_dict(cms_public_menu_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


