# FormItemDTO

Represents a section or group within a form, containing a grid of form elements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aiprompt** | **str** |  | [optional] 
**title** | **str** | The title or heading of this form section | [optional] 
**description** | **str** | Additional descriptive text explaining the purpose or instructions for this section | [optional] 
**type** | **str** | The type of form section (e.g., &#39;grid&#39;, &#39;section&#39;, etc.) | [optional] 
**ai_prompt** | **str** | The AI prompt for the form section. Only applicable to steps. | [optional] 
**grid** | **List[List[GridItemDTO]]** | A two-dimensional array representing the layout of form elements. Each inner list represents a row of elements | [optional] 

## Example

```python
from caraer_client.models.form_item_dto import FormItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FormItemDTO from a JSON string
form_item_dto_instance = FormItemDTO.from_json(json)
# print the JSON string representation of the object
print(FormItemDTO.to_json())

# convert the object into a dict
form_item_dto_dict = form_item_dto_instance.to_dict()
# create an instance of FormItemDTO from a dict
form_item_dto_from_dict = FormItemDTO.from_dict(form_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


