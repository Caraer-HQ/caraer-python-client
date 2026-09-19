# CmsModuleDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**preview** | **str** |  | [optional] 
**app_uuid** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**app_label** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**retired** | **bool** |  | [optional] 
**fields** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md) |  | [optional] 
**frameworks** | **Dict[str, str]** |  | [optional] 

## Example

```python
from caraer_client.models.cms_module_dto import CmsModuleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CmsModuleDTO from a JSON string
cms_module_dto_instance = CmsModuleDTO.from_json(json)
# print the JSON string representation of the object
print(CmsModuleDTO.to_json())

# convert the object into a dict
cms_module_dto_dict = cms_module_dto_instance.to_dict()
# create an instance of CmsModuleDTO from a dict
cms_module_dto_from_dict = CmsModuleDTO.from_dict(cms_module_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


