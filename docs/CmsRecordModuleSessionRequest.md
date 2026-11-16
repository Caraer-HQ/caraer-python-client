# CmsRecordModuleSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**record_uuid** | **str** |  | [optional] 
**config** | [**CmsPreviewConfiguration**](CmsPreviewConfiguration.md) |  | [optional] 
**parent_origin** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.cms_record_module_session_request import CmsRecordModuleSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CmsRecordModuleSessionRequest from a JSON string
cms_record_module_session_request_instance = CmsRecordModuleSessionRequest.from_json(json)
# print the JSON string representation of the object
print(CmsRecordModuleSessionRequest.to_json())

# convert the object into a dict
cms_record_module_session_request_dict = cms_record_module_session_request_instance.to_dict()
# create an instance of CmsRecordModuleSessionRequest from a dict
cms_record_module_session_request_from_dict = CmsRecordModuleSessionRequest.from_dict(cms_record_module_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


