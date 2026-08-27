# ShowResponse

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **object** | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response import ShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponse from a JSON string
show_response_instance = ShowResponse.from_json(json)
# print the JSON string representation of the object
print(ShowResponse.to_json())

# convert the object into a dict
show_response_dict = show_response_instance.to_dict()
# create an instance of ShowResponse from a dict
show_response_from_dict = ShowResponse.from_dict(show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


