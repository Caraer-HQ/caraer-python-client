# CmsModuleComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**fields** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.cms_module_component import CmsModuleComponent

# TODO update the JSON string below
json = "{}"
# create an instance of CmsModuleComponent from a JSON string
cms_module_component_instance = CmsModuleComponent.from_json(json)
# print the JSON string representation of the object
print(CmsModuleComponent.to_json())

# convert the object into a dict
cms_module_component_dict = cms_module_component_instance.to_dict()
# create an instance of CmsModuleComponent from a dict
cms_module_component_from_dict = CmsModuleComponent.from_dict(cms_module_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


