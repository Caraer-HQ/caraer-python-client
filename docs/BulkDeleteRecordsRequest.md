# BulkDeleteRecordsRequest

Request to archive, anonymize, or permanently delete multiple records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | Record UUIDs to delete. | 
**mode** | **str** | Deletion mode: &#39;archive&#39;, &#39;anonymize&#39;, or &#39;delete&#39;. | 

## Example

```python
from caraer_client.models.bulk_delete_records_request import BulkDeleteRecordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteRecordsRequest from a JSON string
bulk_delete_records_request_instance = BulkDeleteRecordsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteRecordsRequest.to_json())

# convert the object into a dict
bulk_delete_records_request_dict = bulk_delete_records_request_instance.to_dict()
# create an instance of BulkDeleteRecordsRequest from a dict
bulk_delete_records_request_from_dict = BulkDeleteRecordsRequest.from_dict(bulk_delete_records_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


