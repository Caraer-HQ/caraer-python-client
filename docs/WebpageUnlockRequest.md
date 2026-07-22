# WebpageUnlockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.webpage_unlock_request import WebpageUnlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageUnlockRequest from a JSON string
webpage_unlock_request_instance = WebpageUnlockRequest.from_json(json)
# print the JSON string representation of the object
print(WebpageUnlockRequest.to_json())

# convert the object into a dict
webpage_unlock_request_dict = webpage_unlock_request_instance.to_dict()
# create an instance of WebpageUnlockRequest from a dict
webpage_unlock_request_from_dict = WebpageUnlockRequest.from_dict(webpage_unlock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


