# FormWithAiPromptDTO

Data transfer object representing a form with its associated properties and structure

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
**object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | The associated Caraer object that this form belongs to | [optional] 
**grids** | [**List[FormItemDTO]**](FormItemDTO.md) | List of form items that make up the form&#39;s structure. Each grid represents a section or group of form elements | [optional] 
**description** | **str** | Descriptive text providing additional information about the form | [optional] 
**styling** | **str** | The styling of the form. Can be &#39;standard&#39;, &#39;underline&#39; or &#39;plain&#39; | [optional] 
**leadscores** | [**List[Leadscore]**](Leadscore.md) | List of lead scoring rules associated with this form. Used to evaluate and score form submissions | [optional] 
**relations** | [**List[FormRelationDTO]**](FormRelationDTO.md) | List of form relations that define the relationships between this form conversion record and other records in the system | [optional] 
**wizard** | **bool** | Indicates if the form should be displayed as a step-by-step wizard interface | [optional] 
**metadata** | **Dict[str, str]** | Metadata associated with the form | [optional] 
**thank_you_message** | **str** | Thank you message to be displayed after the form is submitted | [optional] 
**redirect_url** | **str** | Redirect URL to be displayed after the form is submitted | [optional] 
**ai_prompt** | **str** | AI prompt to be used for the form | [optional] 

## Example

```python
from caraer_client.models.form_with_ai_prompt_dto import FormWithAiPromptDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FormWithAiPromptDTO from a JSON string
form_with_ai_prompt_dto_instance = FormWithAiPromptDTO.from_json(json)
# print the JSON string representation of the object
print(FormWithAiPromptDTO.to_json())

# convert the object into a dict
form_with_ai_prompt_dto_dict = form_with_ai_prompt_dto_instance.to_dict()
# create an instance of FormWithAiPromptDTO from a dict
form_with_ai_prompt_dto_from_dict = FormWithAiPromptDTO.from_dict(form_with_ai_prompt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


