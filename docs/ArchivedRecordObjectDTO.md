# ArchivedRecordObjectDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.archived_record_object_dto import ArchivedRecordObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivedRecordObjectDTO from a JSON string
archived_record_object_dto_instance = ArchivedRecordObjectDTO.from_json(json)
# print the JSON string representation of the object
print(ArchivedRecordObjectDTO.to_json())

# convert the object into a dict
archived_record_object_dto_dict = archived_record_object_dto_instance.to_dict()
# create an instance of ArchivedRecordObjectDTO from a dict
archived_record_object_dto_from_dict = ArchivedRecordObjectDTO.from_dict(archived_record_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


