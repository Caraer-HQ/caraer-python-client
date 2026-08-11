# BulkEditRecordsRequest

Request to create or update multiple records in one operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[BulkEditRecordItem]**](BulkEditRecordItem.md) | Records to create or update. | [optional] 

## Example

```python
from caraer_client.models.bulk_edit_records_request import BulkEditRecordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditRecordsRequest from a JSON string
bulk_edit_records_request_instance = BulkEditRecordsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkEditRecordsRequest.to_json())

# convert the object into a dict
bulk_edit_records_request_dict = bulk_edit_records_request_instance.to_dict()
# create an instance of BulkEditRecordsRequest from a dict
bulk_edit_records_request_from_dict = BulkEditRecordsRequest.from_dict(bulk_edit_records_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


