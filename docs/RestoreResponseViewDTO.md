# RestoreResponseViewDTO

Represents the response returned when a restore operation is performed successfully.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**ViewDTO**](ViewDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.restore_response_view_dto import RestoreResponseViewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreResponseViewDTO from a JSON string
restore_response_view_dto_instance = RestoreResponseViewDTO.from_json(json)
# print the JSON string representation of the object
print(RestoreResponseViewDTO.to_json())

# convert the object into a dict
restore_response_view_dto_dict = restore_response_view_dto_instance.to_dict()
# create an instance of RestoreResponseViewDTO from a dict
restore_response_view_dto_from_dict = RestoreResponseViewDTO.from_dict(restore_response_view_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


