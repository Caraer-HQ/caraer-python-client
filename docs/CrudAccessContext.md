# CrudAccessContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | [**Audience**](Audience.md) |  | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 

## Example

```python
from caraer_client.models.crud_access_context import CrudAccessContext

# TODO update the JSON string below
json = "{}"
# create an instance of CrudAccessContext from a JSON string
crud_access_context_instance = CrudAccessContext.from_json(json)
# print the JSON string representation of the object
print(CrudAccessContext.to_json())

# convert the object into a dict
crud_access_context_dict = crud_access_context_instance.to_dict()
# create an instance of CrudAccessContext from a dict
crud_access_context_from_dict = CrudAccessContext.from_dict(crud_access_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


