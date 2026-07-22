# UsedInResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_uuids** | **List[str]** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.used_in_result import UsedInResult

# TODO update the JSON string below
json = "{}"
# create an instance of UsedInResult from a JSON string
used_in_result_instance = UsedInResult.from_json(json)
# print the JSON string representation of the object
print(UsedInResult.to_json())

# convert the object into a dict
used_in_result_dict = used_in_result_instance.to_dict()
# create an instance of UsedInResult from a dict
used_in_result_from_dict = UsedInResult.from_dict(used_in_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


