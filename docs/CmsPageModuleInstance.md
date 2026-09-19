# CmsPageModuleInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**module** | **str** |  | [optional] 
**fields** | **Dict[str, Optional[object]]** |  | [optional] 
**hidden** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.cms_page_module_instance import CmsPageModuleInstance

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPageModuleInstance from a JSON string
cms_page_module_instance_instance = CmsPageModuleInstance.from_json(json)
# print the JSON string representation of the object
print(CmsPageModuleInstance.to_json())

# convert the object into a dict
cms_page_module_instance_dict = cms_page_module_instance_instance.to_dict()
# create an instance of CmsPageModuleInstance from a dict
cms_page_module_instance_from_dict = CmsPageModuleInstance.from_dict(cms_page_module_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


