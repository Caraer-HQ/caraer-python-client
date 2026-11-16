# Record


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**deleted_at** | **int** |  | [optional] 
**created_by_uuid** | **str** |  | [optional] 
**updated_by_uuid** | **str** |  | [optional] 
**deleted_by_uuid** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**complete** | **bool** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**uuid** | **str** |  | 
**properties** | [**List[FilledProperty]**](FilledProperty.md) |  | [optional] 
**objects** | **Dict[str, Optional[object]]** |  | [optional] 
**user** | [**PublicUserDTO**](PublicUserDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print(Record.to_json())

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_from_dict = Record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


