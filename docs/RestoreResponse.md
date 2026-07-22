# RestoreResponse

Represents the response returned when a restore operation is performed successfully.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from caraer_client.models.restore_response import RestoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreResponse from a JSON string
restore_response_instance = RestoreResponse.from_json(json)
# print the JSON string representation of the object
print(RestoreResponse.to_json())

# convert the object into a dict
restore_response_dict = restore_response_instance.to_dict()
# create an instance of RestoreResponse from a dict
restore_response_from_dict = RestoreResponse.from_dict(restore_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


