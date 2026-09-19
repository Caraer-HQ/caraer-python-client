# ShowResponseSignedUrlResultDTO

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**SignedUrlResultDTO**](SignedUrlResultDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_signed_url_result_dto import ShowResponseSignedUrlResultDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseSignedUrlResultDTO from a JSON string
show_response_signed_url_result_dto_instance = ShowResponseSignedUrlResultDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseSignedUrlResultDTO.to_json())

# convert the object into a dict
show_response_signed_url_result_dto_dict = show_response_signed_url_result_dto_instance.to_dict()
# create an instance of ShowResponseSignedUrlResultDTO from a dict
show_response_signed_url_result_dto_from_dict = ShowResponseSignedUrlResultDTO.from_dict(show_response_signed_url_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


