# CmsPageDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 
**revision** | **int** |  | [optional] 
**modules** | [**List[CmsPageModuleInstance]**](CmsPageModuleInstance.md) |  | [optional] 
**seo** | **Dict[str, Optional[object]]** |  | [optional] 
**title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**excerpt** | **str** |  | [optional] 
**css** | **str** |  | [optional] 
**head_js** | **str** |  | [optional] 
**body_js** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.cms_page_document import CmsPageDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPageDocument from a JSON string
cms_page_document_instance = CmsPageDocument.from_json(json)
# print the JSON string representation of the object
print(CmsPageDocument.to_json())

# convert the object into a dict
cms_page_document_dict = cms_page_document_instance.to_dict()
# create an instance of CmsPageDocument from a dict
cms_page_document_from_dict = CmsPageDocument.from_dict(cms_page_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


