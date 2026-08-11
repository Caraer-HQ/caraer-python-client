# BulkEditRecordErrorItem

Validation or processing errors for a single record in a bulk edit operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the record that failed, if known. | [optional] 
**client_ref** | **str** | Client reference echoed from the request, if provided. | [optional] 
**message** | **str** | Summary message for this record&#39;s failure. | [optional] 
**errors** | [**List[CaraerErrorType]**](CaraerErrorType.md) | Field-level validation errors. | [optional] 

## Example

```python
from caraer_client.models.bulk_edit_record_error_item import BulkEditRecordErrorItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditRecordErrorItem from a JSON string
bulk_edit_record_error_item_instance = BulkEditRecordErrorItem.from_json(json)
# print the JSON string representation of the object
print(BulkEditRecordErrorItem.to_json())

# convert the object into a dict
bulk_edit_record_error_item_dict = bulk_edit_record_error_item_instance.to_dict()
# create an instance of BulkEditRecordErrorItem from a dict
bulk_edit_record_error_item_from_dict = BulkEditRecordErrorItem.from_dict(bulk_edit_record_error_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


