# AppConnectionStatusDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**preset** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**connected** | **bool** |  | [optional] 
**owner_type** | **str** |  | [optional] 
**owner_user_uuid** | **str** |  | [optional] 
**account_label** | **str** |  | [optional] 
**connected_at** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.app_connection_status_dto import AppConnectionStatusDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppConnectionStatusDTO from a JSON string
app_connection_status_dto_instance = AppConnectionStatusDTO.from_json(json)
# print the JSON string representation of the object
print(AppConnectionStatusDTO.to_json())

# convert the object into a dict
app_connection_status_dto_dict = app_connection_status_dto_instance.to_dict()
# create an instance of AppConnectionStatusDTO from a dict
app_connection_status_dto_from_dict = AppConnectionStatusDTO.from_dict(app_connection_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


