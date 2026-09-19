# CmsPagePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 
**var_field** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**fields** | **Dict[str, Optional[object]]** |  | [optional] 
**module** | [**CmsPageModuleInstance**](CmsPageModuleInstance.md) |  | [optional] 
**index** | **int** |  | [optional] 
**to_index** | **int** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**modules** | [**List[CmsPageModuleInstance]**](CmsPageModuleInstance.md) |  | [optional] 
**seo** | **Dict[str, Optional[object]]** |  | [optional] 

## Example

```python
from caraer_client.models.cms_page_patch import CmsPagePatch

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPagePatch from a JSON string
cms_page_patch_instance = CmsPagePatch.from_json(json)
# print the JSON string representation of the object
print(CmsPagePatch.to_json())

# convert the object into a dict
cms_page_patch_dict = cms_page_patch_instance.to_dict()
# create an instance of CmsPagePatch from a dict
cms_page_patch_from_dict = CmsPagePatch.from_dict(cms_page_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


