# GridItemSettingsDTO

Configuration settings for a grid item in a form, including property settings and form-related settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | [**RelationDTO**](RelationDTO.md) | Defines the relationship between this form field and other entities or forms | [optional] 
**record** | [**Record**](Record.md) | UUID of a record to be pre-filled in this form field | [optional] 
**aiprompt** | **str** |  | [optional] 
**label** | **str** | The display label for the form field | [optional] 
**default_value** | **str** | The default value to be pre-filled in the form field | [optional] 
**is_required** | **bool** | Indicates whether this field must be filled out before form submission | [optional] 
**hidden** | **bool** | Indicates whether this field should be hidden from view | [optional] 
**placeholder** | **str** | The placeholder text for the form field | [optional] 
**help_text** | **str** | The help text for the form field | [optional] 
**ai_prompt** | **str** | The AI prompt for the form field. Only applicable to text fields. | [optional] 
**styling** | **str** | The styling for the form field. Can be &#39;dropdown&#39;, &#39;grid&#39; or &#39;boxes&#39; | [optional] 
**stretch** | **bool** | Whether the form field should be stretched to the full width of the form | [optional] 
**align** | **str** | The alignment of the form field. Can be &#39;left&#39;, &#39;center&#39; or &#39;right&#39; | [optional] 
**range_min** | **int** | The minimum value for the slider field | [optional] 
**range_max** | **int** | The maximum value for the slider field | [optional] 

## Example

```python
from caraer_client.models.grid_item_settings_dto import GridItemSettingsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GridItemSettingsDTO from a JSON string
grid_item_settings_dto_instance = GridItemSettingsDTO.from_json(json)
# print the JSON string representation of the object
print(GridItemSettingsDTO.to_json())

# convert the object into a dict
grid_item_settings_dto_dict = grid_item_settings_dto_instance.to_dict()
# create an instance of GridItemSettingsDTO from a dict
grid_item_settings_dto_from_dict = GridItemSettingsDTO.from_dict(grid_item_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


