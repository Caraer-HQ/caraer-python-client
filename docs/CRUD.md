# CRUD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_type** | **str** |  | [optional] 
**http_session_id** | **str** |  | [optional] 
**turn_off_meta_relationships** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.crud import CRUD

# TODO update the JSON string below
json = "{}"
# create an instance of CRUD from a JSON string
crud_instance = CRUD.from_json(json)
# print the JSON string representation of the object
print(CRUD.to_json())

# convert the object into a dict
crud_dict = crud_instance.to_dict()
# create an instance of CRUD from a dict
crud_from_dict = CRUD.from_dict(crud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


