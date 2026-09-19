# CmsPagePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**patches** | [**List[CmsPagePatch]**](CmsPagePatch.md) |  | [optional] 
**expected_revision** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.cms_page_patch_request import CmsPagePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPagePatchRequest from a JSON string
cms_page_patch_request_instance = CmsPagePatchRequest.from_json(json)
# print the JSON string representation of the object
print(CmsPagePatchRequest.to_json())

# convert the object into a dict
cms_page_patch_request_dict = cms_page_patch_request_instance.to_dict()
# create an instance of CmsPagePatchRequest from a dict
cms_page_patch_request_from_dict = CmsPagePatchRequest.from_dict(cms_page_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


