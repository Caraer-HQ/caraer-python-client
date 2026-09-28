# FeedFormatSuggestionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed** | [**FeedDTO**](FeedDTO.md) |  | [optional] 
**field_name** | **str** |  | [optional] 
**property_name** | **str** |  | [optional] 
**object_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.feed_format_suggestion_request import FeedFormatSuggestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeedFormatSuggestionRequest from a JSON string
feed_format_suggestion_request_instance = FeedFormatSuggestionRequest.from_json(json)
# print the JSON string representation of the object
print(FeedFormatSuggestionRequest.to_json())

# convert the object into a dict
feed_format_suggestion_request_dict = feed_format_suggestion_request_instance.to_dict()
# create an instance of FeedFormatSuggestionRequest from a dict
feed_format_suggestion_request_from_dict = FeedFormatSuggestionRequest.from_dict(feed_format_suggestion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


