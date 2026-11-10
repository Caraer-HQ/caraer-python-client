# ApiTokenDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.api_token_dto import ApiTokenDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTokenDTO from a JSON string
api_token_dto_instance = ApiTokenDTO.from_json(json)
# print the JSON string representation of the object
print(ApiTokenDTO.to_json())

# convert the object into a dict
api_token_dto_dict = api_token_dto_instance.to_dict()
# create an instance of ApiTokenDTO from a dict
api_token_dto_from_dict = ApiTokenDTO.from_dict(api_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


