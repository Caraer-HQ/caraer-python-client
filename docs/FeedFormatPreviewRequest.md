# FeedFormatPreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample** | **str** |  | [optional] 
**format_pattern** | **str** |  | [optional] 
**format_replacement** | **str** |  | [optional] 
**property_name** | **str** |  | [optional] 
**object_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.feed_format_preview_request import FeedFormatPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeedFormatPreviewRequest from a JSON string
feed_format_preview_request_instance = FeedFormatPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(FeedFormatPreviewRequest.to_json())

# convert the object into a dict
feed_format_preview_request_dict = feed_format_preview_request_instance.to_dict()
# create an instance of FeedFormatPreviewRequest from a dict
feed_format_preview_request_from_dict = FeedFormatPreviewRequest.from_dict(feed_format_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


