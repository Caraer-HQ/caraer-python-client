# ShowResponseListEnvironmentDTO

Success response (ShowResponseListEnvironmentDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_list_environment_dto import ShowResponseListEnvironmentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListEnvironmentDTO from a JSON string
show_response_list_environment_dto_instance = ShowResponseListEnvironmentDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListEnvironmentDTO.to_json())

# convert the object into a dict
show_response_list_environment_dto_dict = show_response_list_environment_dto_instance.to_dict()
# create an instance of ShowResponseListEnvironmentDTO from a dict
show_response_list_environment_dto_from_dict = ShowResponseListEnvironmentDTO.from_dict(show_response_list_environment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


