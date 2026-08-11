# ShowResponseObject

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_object import ShowResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseObject from a JSON string
show_response_object_instance = ShowResponseObject.from_json(json)
# print the JSON string representation of the object
print(ShowResponseObject.to_json())

# convert the object into a dict
show_response_object_dict = show_response_object_instance.to_dict()
# create an instance of ShowResponseObject from a dict
show_response_object_from_dict = ShowResponseObject.from_dict(show_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


