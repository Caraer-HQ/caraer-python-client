# ShowResponseAppOAuthStartResponseDTO

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**AppOAuthStartResponseDTO**](AppOAuthStartResponseDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_app_o_auth_start_response_dto import ShowResponseAppOAuthStartResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseAppOAuthStartResponseDTO from a JSON string
show_response_app_o_auth_start_response_dto_instance = ShowResponseAppOAuthStartResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseAppOAuthStartResponseDTO.to_json())

# convert the object into a dict
show_response_app_o_auth_start_response_dto_dict = show_response_app_o_auth_start_response_dto_instance.to_dict()
# create an instance of ShowResponseAppOAuthStartResponseDTO from a dict
show_response_app_o_auth_start_response_dto_from_dict = ShowResponseAppOAuthStartResponseDTO.from_dict(show_response_app_o_auth_start_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


