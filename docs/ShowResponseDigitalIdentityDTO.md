# ShowResponseDigitalIdentityDTO

Success response (ShowResponseDigitalIdentityDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_digital_identity_dto import ShowResponseDigitalIdentityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseDigitalIdentityDTO from a JSON string
show_response_digital_identity_dto_instance = ShowResponseDigitalIdentityDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseDigitalIdentityDTO.to_json())

# convert the object into a dict
show_response_digital_identity_dto_dict = show_response_digital_identity_dto_instance.to_dict()
# create an instance of ShowResponseDigitalIdentityDTO from a dict
show_response_digital_identity_dto_from_dict = ShowResponseDigitalIdentityDTO.from_dict(show_response_digital_identity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


