# WebpageOptionsDTO

Data Transfer Object representing options for a webpage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_to_template** | **bool** | Indicates if the webpage is related to a template. | [optional] 
**protection_override** | **str** | Page-level protection override: inherit, none, password, signedUrl, caraerAuth | [optional] 
**password_hash** | **str** | Bcrypt hash for per-page password (never returned in public APIs) | [optional] 
**password** | **str** | Recoverable per-page password value for CMS display only | [optional] 
**password_value** | **str** | Stored recoverable per-page password value for CMS display only | [optional] 
**password_smart_content** | **bool** | Whether the per-page password value should be resolved as smart content | [optional] 
**has_password** | **bool** | Whether a per-page password is configured | [optional] 
**inherited_password** | **str** | Recoverable inherited shared password value for CMS display only | [optional] 
**inherited_password_value** | **str** | Stored recoverable inherited shared password value for CMS display only | [optional] 
**inherited_password_smart_content** | **bool** | Whether the inherited shared password value should be resolved as smart content | [optional] 
**inherited_has_password** | **bool** | Whether an inherited shared password is configured | [optional] 

## Example

```python
from caraer_client.models.webpage_options_dto import WebpageOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageOptionsDTO from a JSON string
webpage_options_dto_instance = WebpageOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(WebpageOptionsDTO.to_json())

# convert the object into a dict
webpage_options_dto_dict = webpage_options_dto_instance.to_dict()
# create an instance of WebpageOptionsDTO from a dict
webpage_options_dto_from_dict = WebpageOptionsDTO.from_dict(webpage_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


