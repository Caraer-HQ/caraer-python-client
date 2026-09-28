# FeedFormatPreviewDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample** | **str** |  | [optional] 
**format_pattern** | **str** |  | [optional] 
**format_replacement** | **str** |  | [optional] 
**output** | **str** |  | [optional] 
**matches** | **bool** |  | [optional] 
**stored_value_pattern** | **str** |  | [optional] 
**stored_value_hint** | **str** |  | [optional] 
**format_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.feed_format_preview_dto import FeedFormatPreviewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FeedFormatPreviewDTO from a JSON string
feed_format_preview_dto_instance = FeedFormatPreviewDTO.from_json(json)
# print the JSON string representation of the object
print(FeedFormatPreviewDTO.to_json())

# convert the object into a dict
feed_format_preview_dto_dict = feed_format_preview_dto_instance.to_dict()
# create an instance of FeedFormatPreviewDTO from a dict
feed_format_preview_dto_from_dict = FeedFormatPreviewDTO.from_dict(feed_format_preview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


