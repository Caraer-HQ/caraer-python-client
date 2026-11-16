# CmsPreviewConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** |  | [optional] 
**fields** | **Dict[str, Optional[object]]** |  | [optional] 
**environment** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.cms_preview_configuration import CmsPreviewConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CmsPreviewConfiguration from a JSON string
cms_preview_configuration_instance = CmsPreviewConfiguration.from_json(json)
# print the JSON string representation of the object
print(CmsPreviewConfiguration.to_json())

# convert the object into a dict
cms_preview_configuration_dict = cms_preview_configuration_instance.to_dict()
# create an instance of CmsPreviewConfiguration from a dict
cms_preview_configuration_from_dict = CmsPreviewConfiguration.from_dict(cms_preview_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


