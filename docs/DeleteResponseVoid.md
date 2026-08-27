# DeleteResponseVoid

Response class representing the result of a delete operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **object** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.delete_response_void import DeleteResponseVoid

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteResponseVoid from a JSON string
delete_response_void_instance = DeleteResponseVoid.from_json(json)
# print the JSON string representation of the object
print(DeleteResponseVoid.to_json())

# convert the object into a dict
delete_response_void_dict = delete_response_void_instance.to_dict()
# create an instance of DeleteResponseVoid from a dict
delete_response_void_from_dict = DeleteResponseVoid.from_dict(delete_response_void_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


