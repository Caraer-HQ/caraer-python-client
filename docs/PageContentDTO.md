# PageContentDTO

Data transfer object representing a webpage content

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
**category** | **str** | Category of the content | [optional] 
**parent_uuid** | **str** | Unique identifier for the parent content | [optional] 
**type** | **str** | Type of the content (&#39;box&#39; or &#39;component&#39;) | [optional] 
**display** | **str** | Display of the content for box (&#39;column&#39;, &#39;row&#39; or &#39;wrap&#39;) and for component () | [optional] 
**text** | **str** | Text content of the content | [optional] 
**custom_css** | **str** | Direct CSS for this content node, scoped to data-component-uuid at render time | [optional] 
**styling** | [**PageContentStylingDTO**](PageContentStylingDTO.md) | Styling of the content | [optional] 
**settings** | [**PageContentSettingsDTO**](PageContentSettingsDTO.md) | Settings for the content | [optional] 
**children** | [**List[PageContentDTO]**](PageContentDTO.md) | Children of the content | [optional] 
**scope** | **str** | Module storage scope: company or personal | [optional] 
**module_kind** | **str** | Module kind: content (section/component) or page (full page design) | [optional] 
**page_custom_css** | **str** | Page-level custom CSS for page modules | [optional] 
**page_custom_js_head** | **str** | Page-level custom JS for the head for page modules | [optional] 
**page_custom_js_body** | **str** | Page-level custom JS for the body for page modules | [optional] 
**sidebar_uuid** | **str** | Sidebar preview UUID for page modules | [optional] 
**sidebar_relation_uuid** | **str** | Sidebar relation UUID for page modules | [optional] 
**sidebar_object_uuid** | **str** | Sidebar object UUID for page modules | [optional] 

## Example

```python
from caraer_client.models.page_content_dto import PageContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PageContentDTO from a JSON string
page_content_dto_instance = PageContentDTO.from_json(json)
# print the JSON string representation of the object
print(PageContentDTO.to_json())

# convert the object into a dict
page_content_dto_dict = page_content_dto_instance.to_dict()
# create an instance of PageContentDTO from a dict
page_content_dto_from_dict = PageContentDTO.from_dict(page_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


