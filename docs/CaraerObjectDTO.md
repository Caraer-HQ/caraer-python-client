# CaraerObjectDTO

Data transfer object representing a Caraer object with its configuration, properties, relations, and views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | Unique identifier name for the object | [optional] 
**label** | **str** | Display label for the object | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering objects | [optional] 
**plural** | **str** | Plural form of the object&#39;s name, used for display purposes | [optional] 
**description** | **str** | Detailed description of the object&#39;s purpose and usage | [optional] 
**groups** | **List[str]** | Collection of group names this object belongs to | [optional] 
**icon** | **str** | Icon identifier for visual representation of the object | [optional] 
**show_in_menu** | **bool** | Indicates if this object should be displayed in navigation menus | [optional] 
**default_trait** | **str** | Name of the default trait applied to this object | [optional] 
**traits** | **List[str]** | List of trait names associated with this object | [optional] 
**views** | [**List[ViewDTO]**](ViewDTO.md) | List of view configurations for displaying this object | [optional] 
**properties** | [**List[PropertyDTO]**](PropertyDTO.md) | List of properties defined for this object | [optional] 
**relations** | [**List[RelationDTO]**](RelationDTO.md) | List of relations this object has with other objects | [optional] 
**suites** | **List[str]** | List of suite names this object belongs to | [optional] 
**extends_to** | [**List[CaraerObjectDTO]**](CaraerObjectDTO.md) | List of objects this object extends to | [optional] 
**editable** | **bool** | When false, the object schema cannot be updated or deleted via the API | [optional] 

## Example

```python
from caraer_client.models.caraer_object_dto import CaraerObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CaraerObjectDTO from a JSON string
caraer_object_dto_instance = CaraerObjectDTO.from_json(json)
# print the JSON string representation of the object
print(CaraerObjectDTO.to_json())

# convert the object into a dict
caraer_object_dto_dict = caraer_object_dto_instance.to_dict()
# create an instance of CaraerObjectDTO from a dict
caraer_object_dto_from_dict = CaraerObjectDTO.from_dict(caraer_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


