# AppBarVisibilityEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | **List[str]** |  | [optional] 
**suites** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.app_bar_visibility_entry import AppBarVisibilityEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AppBarVisibilityEntry from a JSON string
app_bar_visibility_entry_instance = AppBarVisibilityEntry.from_json(json)
# print the JSON string representation of the object
print(AppBarVisibilityEntry.to_json())

# convert the object into a dict
app_bar_visibility_entry_dict = app_bar_visibility_entry_instance.to_dict()
# create an instance of AppBarVisibilityEntry from a dict
app_bar_visibility_entry_from_dict = AppBarVisibilityEntry.from_dict(app_bar_visibility_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


