# CursorLocation

Cursor location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 

## Example

```python
from caraer_client.models.cursor_location import CursorLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CursorLocation from a JSON string
cursor_location_instance = CursorLocation.from_json(json)
# print the JSON string representation of the object
print(CursorLocation.to_json())

# convert the object into a dict
cursor_location_dict = cursor_location_instance.to_dict()
# create an instance of CursorLocation from a dict
cursor_location_from_dict = CursorLocation.from_dict(cursor_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


