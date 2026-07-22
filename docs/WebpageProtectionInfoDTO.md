# WebpageProtectionInfoDTO

Public protection metadata for a webpage (no content)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_required** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.webpage_protection_info_dto import WebpageProtectionInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageProtectionInfoDTO from a JSON string
webpage_protection_info_dto_instance = WebpageProtectionInfoDTO.from_json(json)
# print the JSON string representation of the object
print(WebpageProtectionInfoDTO.to_json())

# convert the object into a dict
webpage_protection_info_dto_dict = webpage_protection_info_dto_instance.to_dict()
# create an instance of WebpageProtectionInfoDTO from a dict
webpage_protection_info_dto_from_dict = WebpageProtectionInfoDTO.from_dict(webpage_protection_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


