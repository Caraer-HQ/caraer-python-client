# AppOAuthStartResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorize_url** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.app_o_auth_start_response_dto import AppOAuthStartResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppOAuthStartResponseDTO from a JSON string
app_o_auth_start_response_dto_instance = AppOAuthStartResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AppOAuthStartResponseDTO.to_json())

# convert the object into a dict
app_o_auth_start_response_dto_dict = app_o_auth_start_response_dto_instance.to_dict()
# create an instance of AppOAuthStartResponseDTO from a dict
app_o_auth_start_response_dto_from_dict = AppOAuthStartResponseDTO.from_dict(app_o_auth_start_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


