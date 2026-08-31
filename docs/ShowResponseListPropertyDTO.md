# ShowResponseListPropertyDTO

Success response (ShowResponseListPropertyDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_list_property_dto import ShowResponseListPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListPropertyDTO from a JSON string
show_response_list_property_dto_instance = ShowResponseListPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListPropertyDTO.to_json())

# convert the object into a dict
show_response_list_property_dto_dict = show_response_list_property_dto_instance.to_dict()
# create an instance of ShowResponseListPropertyDTO from a dict
show_response_list_property_dto_from_dict = ShowResponseListPropertyDTO.from_dict(show_response_list_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


