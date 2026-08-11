# BulkEditRecordResultItem

A successfully saved record from a bulk edit operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the saved record. | [optional] 
**client_ref** | **str** | Client reference echoed from the request, if provided. | [optional] 
**created** | **bool** | True when the record was created; false when updated. | [optional] 

## Example

```python
from caraer_client.models.bulk_edit_record_result_item import BulkEditRecordResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditRecordResultItem from a JSON string
bulk_edit_record_result_item_instance = BulkEditRecordResultItem.from_json(json)
# print the JSON string representation of the object
print(BulkEditRecordResultItem.to_json())

# convert the object into a dict
bulk_edit_record_result_item_dict = bulk_edit_record_result_item_instance.to_dict()
# create an instance of BulkEditRecordResultItem from a dict
bulk_edit_record_result_item_from_dict = BulkEditRecordResultItem.from_dict(bulk_edit_record_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


