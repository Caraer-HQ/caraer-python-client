# CmsEnvironmentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**routing** | **str** |  | [optional] 
**slug_prefix** | **str** |  | [optional] 
**host_label** | **str** |  | [optional] 
**requires_auth** | **bool** |  | [optional] 
**html_lang** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.cms_environment_dto import CmsEnvironmentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CmsEnvironmentDTO from a JSON string
cms_environment_dto_instance = CmsEnvironmentDTO.from_json(json)
# print the JSON string representation of the object
print(CmsEnvironmentDTO.to_json())

# convert the object into a dict
cms_environment_dto_dict = cms_environment_dto_instance.to_dict()
# create an instance of CmsEnvironmentDTO from a dict
cms_environment_dto_from_dict = CmsEnvironmentDTO.from_dict(cms_environment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


