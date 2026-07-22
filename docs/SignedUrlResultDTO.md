# SignedUrlResultDTO

Generated signed URL for a protected webpage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_uuid** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**var_query_params** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.signed_url_result_dto import SignedUrlResultDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SignedUrlResultDTO from a JSON string
signed_url_result_dto_instance = SignedUrlResultDTO.from_json(json)
# print the JSON string representation of the object
print(SignedUrlResultDTO.to_json())

# convert the object into a dict
signed_url_result_dto_dict = signed_url_result_dto_instance.to_dict()
# create an instance of SignedUrlResultDTO from a dict
signed_url_result_dto_from_dict = SignedUrlResultDTO.from_dict(signed_url_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


