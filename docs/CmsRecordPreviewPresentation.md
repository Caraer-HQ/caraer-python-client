# CmsRecordPreviewPresentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title_field** | **str** |  | [optional] 
**subtitle_field** | **str** |  | [optional] 
**image_field** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.cms_record_preview_presentation import CmsRecordPreviewPresentation

# TODO update the JSON string below
json = "{}"
# create an instance of CmsRecordPreviewPresentation from a JSON string
cms_record_preview_presentation_instance = CmsRecordPreviewPresentation.from_json(json)
# print the JSON string representation of the object
print(CmsRecordPreviewPresentation.to_json())

# convert the object into a dict
cms_record_preview_presentation_dict = cms_record_preview_presentation_instance.to_dict()
# create an instance of CmsRecordPreviewPresentation from a dict
cms_record_preview_presentation_from_dict = CmsRecordPreviewPresentation.from_dict(cms_record_preview_presentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


