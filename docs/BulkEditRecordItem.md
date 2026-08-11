# BulkEditRecordItem

A single record to create or update in a bulk edit request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of an existing record to update. Omit to create a new record. | [optional] 
**client_ref** | **str** | Client-side reference for matching the item back after create (e.g. row-3). | [optional] 
**properties** | **Dict[str, Optional[object]]** | Property values to set on the record. | [optional] 

## Example

```python
from caraer_client.models.bulk_edit_record_item import BulkEditRecordItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditRecordItem from a JSON string
bulk_edit_record_item_instance = BulkEditRecordItem.from_json(json)
# print the JSON string representation of the object
print(BulkEditRecordItem.to_json())

# convert the object into a dict
bulk_edit_record_item_dict = bulk_edit_record_item_instance.to_dict()
# create an instance of BulkEditRecordItem from a dict
bulk_edit_record_item_from_dict = BulkEditRecordItem.from_dict(bulk_edit_record_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


