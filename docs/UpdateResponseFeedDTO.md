# UpdateResponseFeedDTO

Represents the response returned after a successful update operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**FeedDTO**](FeedDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.update_response_feed_dto import UpdateResponseFeedDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResponseFeedDTO from a JSON string
update_response_feed_dto_instance = UpdateResponseFeedDTO.from_json(json)
# print the JSON string representation of the object
print(UpdateResponseFeedDTO.to_json())

# convert the object into a dict
update_response_feed_dto_dict = update_response_feed_dto_instance.to_dict()
# create an instance of UpdateResponseFeedDTO from a dict
update_response_feed_dto_from_dict = UpdateResponseFeedDTO.from_dict(update_response_feed_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


