# BulkDeleteRecordsData

Payload of a bulk delete records response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | UUIDs that were successfully deleted. | [optional] 

## Example

```python
from caraer_client.models.bulk_delete_records_data import BulkDeleteRecordsData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteRecordsData from a JSON string
bulk_delete_records_data_instance = BulkDeleteRecordsData.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteRecordsData.to_json())

# convert the object into a dict
bulk_delete_records_data_dict = bulk_delete_records_data_instance.to_dict()
# create an instance of BulkDeleteRecordsData from a dict
bulk_delete_records_data_from_dict = BulkDeleteRecordsData.from_dict(bulk_delete_records_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


