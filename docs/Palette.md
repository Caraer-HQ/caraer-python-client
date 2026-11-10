# Palette


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | **Dict[str, str]** |  | [optional] 
**dark** | **Dict[str, str]** |  | [optional] 

## Example

```python
from caraer_client.models.palette import Palette

# TODO update the JSON string below
json = "{}"
# create an instance of Palette from a JSON string
palette_instance = Palette.from_json(json)
# print the JSON string representation of the object
print(Palette.to_json())

# convert the object into a dict
palette_dict = palette_instance.to_dict()
# create an instance of Palette from a dict
palette_from_dict = Palette.from_dict(palette_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


