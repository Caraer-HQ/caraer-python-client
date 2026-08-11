# BulkEditRecordsData

Payload of a bulk edit records response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[BulkEditRecordResultItem]**](BulkEditRecordResultItem.md) | Successfully saved records. | [optional] 

## Example

```python
from caraer_client.models.bulk_edit_records_data import BulkEditRecordsData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditRecordsData from a JSON string
bulk_edit_records_data_instance = BulkEditRecordsData.from_json(json)
# print the JSON string representation of the object
print(BulkEditRecordsData.to_json())

# convert the object into a dict
bulk_edit_records_data_dict = bulk_edit_records_data_instance.to_dict()
# create an instance of BulkEditRecordsData from a dict
bulk_edit_records_data_from_dict = BulkEditRecordsData.from_dict(bulk_edit_records_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


