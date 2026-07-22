# WebpagePublicRecordDTO

Webpage-public record values with internal and parsed property maps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the webpage backing record | [optional] 
**properties** | **Dict[str, Optional[object]]** | Internal/plain property values keyed by property name | [optional] 
**parsed_properties** | **Dict[str, Optional[object]]** | Parsed/display property values keyed by property name | [optional] 

## Example

```python
from caraer_client.models.webpage_public_record_dto import WebpagePublicRecordDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpagePublicRecordDTO from a JSON string
webpage_public_record_dto_instance = WebpagePublicRecordDTO.from_json(json)
# print the JSON string representation of the object
print(WebpagePublicRecordDTO.to_json())

# convert the object into a dict
webpage_public_record_dto_dict = webpage_public_record_dto_instance.to_dict()
# create an instance of WebpagePublicRecordDTO from a dict
webpage_public_record_dto_from_dict = WebpagePublicRecordDTO.from_dict(webpage_public_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


