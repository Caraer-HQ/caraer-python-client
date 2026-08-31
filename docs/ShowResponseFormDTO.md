# ShowResponseFormDTO

Success response (ShowResponseFormDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_form_dto import ShowResponseFormDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseFormDTO from a JSON string
show_response_form_dto_instance = ShowResponseFormDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseFormDTO.to_json())

# convert the object into a dict
show_response_form_dto_dict = show_response_form_dto_instance.to_dict()
# create an instance of ShowResponseFormDTO from a dict
show_response_form_dto_from_dict = ShowResponseFormDTO.from_dict(show_response_form_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


