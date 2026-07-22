# MorphRecordRequest

Request to morph a record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[CaraerObjectDTO]**](CaraerObjectDTO.md) | The objects to morph the record into | [optional] 

## Example

```python
from caraer_client.models.morph_record_request import MorphRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MorphRecordRequest from a JSON string
morph_record_request_instance = MorphRecordRequest.from_json(json)
# print the JSON string representation of the object
print(MorphRecordRequest.to_json())

# convert the object into a dict
morph_record_request_dict = morph_record_request_instance.to_dict()
# create an instance of MorphRecordRequest from a dict
morph_record_request_from_dict = MorphRecordRequest.from_dict(morph_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


