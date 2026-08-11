# ExtendRecordRequest

Request to extend a record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[CaraerObjectDTO]**](CaraerObjectDTO.md) | The objects to extend the record into | [optional] 

## Example

```python
from caraer_client.models.extend_record_request import ExtendRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendRecordRequest from a JSON string
extend_record_request_instance = ExtendRecordRequest.from_json(json)
# print the JSON string representation of the object
print(ExtendRecordRequest.to_json())

# convert the object into a dict
extend_record_request_dict = extend_record_request_instance.to_dict()
# create an instance of ExtendRecordRequest from a dict
extend_record_request_from_dict = ExtendRecordRequest.from_dict(extend_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


