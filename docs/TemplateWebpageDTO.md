# TemplateWebpageDTO

DTO for Template Webpage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**environment** | **str** | The environment of the webpage. | [optional] 
**title** | **str** | The title of the webpage. | [optional] 
**excerpt** | **str** | Short summary or excerpt displayed for the webpage. | [optional] 
**slug** | **str** | URL-friendly identifier for the webpage. | [optional] 
**image** | **str** | URL or identifier of the image associated with the webpage. | [optional] 
**custom_css** | **str** | Custom CSS for the webpage. | [optional] 
**custom_js_head** | **str** | Custom JS for the webpage. | [optional] 
**custom_js_body** | **str** | Custom JS for the webpage. | [optional] 
**content** | [**PageContentDTO**](PageContentDTO.md) | Content of the webpage | [optional] 
**sidebar** | [**PreviewDTO**](PreviewDTO.md) | Preview of the sidebar | [optional] 
**sidebar_relation** | [**RelationDTO**](RelationDTO.md) | Relation of the sidebar | [optional] 
**sidebar_object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | Object of the sidebar | [optional] 
**options** | [**WebpageOptionsDTO**](WebpageOptionsDTO.md) | Custom options and configurations specific to the webpage. | [optional] 
**meta_data** | **Dict[str, Optional[object]]** | Map of additional metadata and attributes for the webpage. | [optional] 
**object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | Represents the associated Caraer object | [optional] 

## Example

```python
from caraer_client.models.template_webpage_dto import TemplateWebpageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateWebpageDTO from a JSON string
template_webpage_dto_instance = TemplateWebpageDTO.from_json(json)
# print the JSON string representation of the object
print(TemplateWebpageDTO.to_json())

# convert the object into a dict
template_webpage_dto_dict = template_webpage_dto_instance.to_dict()
# create an instance of TemplateWebpageDTO from a dict
template_webpage_dto_from_dict = TemplateWebpageDTO.from_dict(template_webpage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


