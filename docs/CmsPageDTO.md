# CmsPageDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**document** | [**CmsPageDocument**](CmsPageDocument.md) |  | [optional] 
**record** | [**RecordSummary**](RecordSummary.md) |  | [optional] 
**protection** | **Dict[str, Optional[object]]** |  | [optional] 
**locales** | **List[str]** |  | [optional] 
**publish_at** | **int** |  | [optional] 
**unpublish_at** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.cms_page_dto import CmsPageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPageDTO from a JSON string
cms_page_dto_instance = CmsPageDTO.from_json(json)
# print the JSON string representation of the object
print(CmsPageDTO.to_json())

# convert the object into a dict
cms_page_dto_dict = cms_page_dto_instance.to_dict()
# create an instance of CmsPageDTO from a dict
cms_page_dto_from_dict = CmsPageDTO.from_dict(cms_page_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


