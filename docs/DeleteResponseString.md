# DeleteResponseString

Response class representing the result of a delete operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **str** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.delete_response_string import DeleteResponseString

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteResponseString from a JSON string
delete_response_string_instance = DeleteResponseString.from_json(json)
# print the JSON string representation of the object
print(DeleteResponseString.to_json())

# convert the object into a dict
delete_response_string_dict = delete_response_string_instance.to_dict()
# create an instance of DeleteResponseString from a dict
delete_response_string_from_dict = DeleteResponseString.from_dict(delete_response_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


