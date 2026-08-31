# SuccessResponseTable

Success response (SuccessResponseTable).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_table import SuccessResponseTable

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseTable from a JSON string
success_response_table_instance = SuccessResponseTable.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseTable.to_json())

# convert the object into a dict
success_response_table_dict = success_response_table_instance.to_dict()
# create an instance of SuccessResponseTable from a dict
success_response_table_from_dict = SuccessResponseTable.from_dict(success_response_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


