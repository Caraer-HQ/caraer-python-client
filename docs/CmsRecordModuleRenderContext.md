# CmsRecordModuleRenderContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_uuid** | **str** |  | [optional] 
**module** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**config** | [**CmsPreviewConfiguration**](CmsPreviewConfiguration.md) |  | [optional] 
**record** | [**RecordSummary**](RecordSummary.md) |  | [optional] 
**parent_origin** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.cms_record_module_render_context import CmsRecordModuleRenderContext

# TODO update the JSON string below
json = "{}"
# create an instance of CmsRecordModuleRenderContext from a JSON string
cms_record_module_render_context_instance = CmsRecordModuleRenderContext.from_json(json)
# print the JSON string representation of the object
print(CmsRecordModuleRenderContext.to_json())

# convert the object into a dict
cms_record_module_render_context_dict = cms_record_module_render_context_instance.to_dict()
# create an instance of CmsRecordModuleRenderContext from a dict
cms_record_module_render_context_from_dict = CmsRecordModuleRenderContext.from_dict(cms_record_module_render_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


