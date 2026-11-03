# FilledProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.filled_property import FilledProperty

# TODO update the JSON string below
json = "{}"
# create an instance of FilledProperty from a JSON string
filled_property_instance = FilledProperty.from_json(json)
# print the JSON string representation of the object
print(FilledProperty.to_json())

# convert the object into a dict
filled_property_dict = filled_property_instance.to_dict()
# create an instance of FilledProperty from a dict
filled_property_from_dict = FilledProperty.from_dict(filled_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


