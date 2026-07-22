# CreateResponseSignedUrlResultDTO

Response for a successful resource creation operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**SignedUrlResultDTO**](SignedUrlResultDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.create_response_signed_url_result_dto import CreateResponseSignedUrlResultDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseSignedUrlResultDTO from a JSON string
create_response_signed_url_result_dto_instance = CreateResponseSignedUrlResultDTO.from_json(json)
# print the JSON string representation of the object
print(CreateResponseSignedUrlResultDTO.to_json())

# convert the object into a dict
create_response_signed_url_result_dto_dict = create_response_signed_url_result_dto_instance.to_dict()
# create an instance of CreateResponseSignedUrlResultDTO from a dict
create_response_signed_url_result_dto_from_dict = CreateResponseSignedUrlResultDTO.from_dict(create_response_signed_url_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


