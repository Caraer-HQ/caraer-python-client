# SuccessResponseFeedFormatPreviewDTO

Represents a standard successful response with a message and optional data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**FeedFormatPreviewDTO**](FeedFormatPreviewDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.success_response_feed_format_preview_dto import SuccessResponseFeedFormatPreviewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseFeedFormatPreviewDTO from a JSON string
success_response_feed_format_preview_dto_instance = SuccessResponseFeedFormatPreviewDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseFeedFormatPreviewDTO.to_json())

# convert the object into a dict
success_response_feed_format_preview_dto_dict = success_response_feed_format_preview_dto_instance.to_dict()
# create an instance of SuccessResponseFeedFormatPreviewDTO from a dict
success_response_feed_format_preview_dto_from_dict = SuccessResponseFeedFormatPreviewDTO.from_dict(success_response_feed_format_preview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


