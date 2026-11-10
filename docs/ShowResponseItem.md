# ShowResponseItem

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**Item**](Item.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_item import ShowResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseItem from a JSON string
show_response_item_instance = ShowResponseItem.from_json(json)
# print the JSON string representation of the object
print(ShowResponseItem.to_json())

# convert the object into a dict
show_response_item_dict = show_response_item_instance.to_dict()
# create an instance of ShowResponseItem from a dict
show_response_item_from_dict = ShowResponseItem.from_dict(show_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


