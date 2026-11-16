# CmsPreviewPresentationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**image** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.cms_preview_presentation_dto import CmsPreviewPresentationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPreviewPresentationDTO from a JSON string
cms_preview_presentation_dto_instance = CmsPreviewPresentationDTO.from_json(json)
# print the JSON string representation of the object
print(CmsPreviewPresentationDTO.to_json())

# convert the object into a dict
cms_preview_presentation_dto_dict = cms_preview_presentation_dto_instance.to_dict()
# create an instance of CmsPreviewPresentationDTO from a dict
cms_preview_presentation_dto_from_dict = CmsPreviewPresentationDTO.from_dict(cms_preview_presentation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


