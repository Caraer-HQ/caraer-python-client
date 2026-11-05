# CmsPageSeoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seo** | **Dict[str, Optional[object]]** |  | [optional] 
**expected_revision** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.cms_page_seo_request import CmsPageSeoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPageSeoRequest from a JSON string
cms_page_seo_request_instance = CmsPageSeoRequest.from_json(json)
# print the JSON string representation of the object
print(CmsPageSeoRequest.to_json())

# convert the object into a dict
cms_page_seo_request_dict = cms_page_seo_request_instance.to_dict()
# create an instance of CmsPageSeoRequest from a dict
cms_page_seo_request_from_dict = CmsPageSeoRequest.from_dict(cms_page_seo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


