# GridItemDTO

Represents a single cell within a form grid, which can contain a property, text, nested form, or other form elements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**PropertyDTO**](PropertyDTO.md) | The property associated with this grid item, typically representing a form field or input | [optional] 
**text** | **str** | Static text content to be displayed in this grid cell | [optional] 
**form** | [**FormDTO**](FormDTO.md) | A nested form that can be embedded within this grid cell | [optional] 
**submit_button** | **str** | The text of the submit button for this grid item | [optional] 
**settings** | [**GridItemSettingsDTO**](GridItemSettingsDTO.md) | Configuration settings for this grid item, including display and validation rules | [optional] 
**value** | **str** | The value of this grid item, used for form submissions | [optional] 

## Example

```python
from caraer_client.models.grid_item_dto import GridItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GridItemDTO from a JSON string
grid_item_dto_instance = GridItemDTO.from_json(json)
# print the JSON string representation of the object
print(GridItemDTO.to_json())

# convert the object into a dict
grid_item_dto_dict = grid_item_dto_instance.to_dict()
# create an instance of GridItemDTO from a dict
grid_item_dto_from_dict = GridItemDTO.from_dict(grid_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


