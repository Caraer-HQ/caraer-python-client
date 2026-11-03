# RecordWriteEnvelope

Optional record-write envelope. objectName must match the URL's object context. Query parameters still control parse, ignoreErrors and recordReturnFormat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_name** | **str** | Optional object name; when provided it must match the URL. | [optional] 
**record** | [**RecordDTO**](RecordDTO.md) | The record to create or update. | 

## Example

```python
from caraer_client.models.record_write_envelope import RecordWriteEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RecordWriteEnvelope from a JSON string
record_write_envelope_instance = RecordWriteEnvelope.from_json(json)
# print the JSON string representation of the object
print(RecordWriteEnvelope.to_json())

# convert the object into a dict
record_write_envelope_dict = record_write_envelope_instance.to_dict()
# create an instance of RecordWriteEnvelope from a dict
record_write_envelope_from_dict = RecordWriteEnvelope.from_dict(record_write_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


