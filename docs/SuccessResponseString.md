# SuccessResponseString

Represents a standard successful response with a message and optional data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **str** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.success_response_string import SuccessResponseString

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseString from a JSON string
success_response_string_instance = SuccessResponseString.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseString.to_json())

# convert the object into a dict
success_response_string_dict = success_response_string_instance.to_dict()
# create an instance of SuccessResponseString from a dict
success_response_string_from_dict = SuccessResponseString.from_dict(success_response_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


