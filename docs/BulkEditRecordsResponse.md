# BulkEditRecordsResponse

Response for a bulk create/update records operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message. | [optional] 
**data** | [**BulkEditRecordsData**](BulkEditRecordsData.md) | Successfully saved records. | [optional] 
**errors** | [**List[BulkEditRecordErrorItem]**](BulkEditRecordErrorItem.md) | Per-record errors when one or more items failed validation. | [optional] 

## Example

```python
from caraer_client.models.bulk_edit_records_response import BulkEditRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditRecordsResponse from a JSON string
bulk_edit_records_response_instance = BulkEditRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkEditRecordsResponse.to_json())

# convert the object into a dict
bulk_edit_records_response_dict = bulk_edit_records_response_instance.to_dict()
# create an instance of BulkEditRecordsResponse from a dict
bulk_edit_records_response_from_dict = BulkEditRecordsResponse.from_dict(bulk_edit_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


