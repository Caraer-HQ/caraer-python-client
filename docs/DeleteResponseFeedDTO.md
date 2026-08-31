# DeleteResponseFeedDTO

Response class representing the result of a delete operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**FeedDTO**](FeedDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.delete_response_feed_dto import DeleteResponseFeedDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteResponseFeedDTO from a JSON string
delete_response_feed_dto_instance = DeleteResponseFeedDTO.from_json(json)
# print the JSON string representation of the object
print(DeleteResponseFeedDTO.to_json())

# convert the object into a dict
delete_response_feed_dto_dict = delete_response_feed_dto_instance.to_dict()
# create an instance of DeleteResponseFeedDTO from a dict
delete_response_feed_dto_from_dict = DeleteResponseFeedDTO.from_dict(delete_response_feed_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


