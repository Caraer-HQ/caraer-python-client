# ConnectionState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.connection_state import ConnectionState

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionState from a JSON string
connection_state_instance = ConnectionState.from_json(json)
# print the JSON string representation of the object
print(ConnectionState.to_json())

# convert the object into a dict
connection_state_dict = connection_state_instance.to_dict()
# create an instance of ConnectionState from a dict
connection_state_from_dict = ConnectionState.from_dict(connection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


