# BulkDeleteRecordsResponse

Response for a bulk delete records operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message. | [optional] 
**data** | [**BulkDeleteRecordsData**](BulkDeleteRecordsData.md) | Successfully deleted record UUIDs. | [optional] 
**errors** | [**List[BulkEditRecordErrorItem]**](BulkEditRecordErrorItem.md) | Per-record errors when one or more items failed. | [optional] 

## Example

```python
from caraer_client.models.bulk_delete_records_response import BulkDeleteRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteRecordsResponse from a JSON string
bulk_delete_records_response_instance = BulkDeleteRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteRecordsResponse.to_json())

# convert the object into a dict
bulk_delete_records_response_dict = bulk_delete_records_response_instance.to_dict()
# create an instance of BulkDeleteRecordsResponse from a dict
bulk_delete_records_response_from_dict = BulkDeleteRecordsResponse.from_dict(bulk_delete_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


