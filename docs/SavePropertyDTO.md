# SavePropertyDTO

DTO representing a property to be saved

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The internal name of the property | [optional] 
**label** | **str** | The display label of the property | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**description** | **str** | A brief description of the property | [optional] 
**type** | **str** | The data type of the property | [optional] 
**options** | [**List[PropertyOption]**](PropertyOption.md) | List of available options for the property | [optional] 
**group** | **str** | The group to which this property belongs | [optional] 
**format** | **str** | Property format type | [optional] 
**rules** | **List[str]** | Collection of rules applied to the property | [optional] 
**hidden** | **bool** | Indicates if the property is hidden by default | [optional] 
**lifecycle_active** | **bool** | When true, property value changes are tracked as lifecycle records | [optional] 
**required_filter** | [**Filter**](Filter.md) | When this filter matches the record being saved, the property becomes required | [optional] 
**non_public** | **bool** | Indicates if the property is not accessible publicly | [optional] 
**indexed** | **bool** | Indicates if the property is indexed | [optional] 
**format_settings** | **Dict[str, Optional[object]]** | Settings to configure the format of the property | [optional] 
**immutable** | **bool** | Indicates if the property is immutable | [optional] 
**editable** | **bool** | Indicates if the property can be edited | [optional] 
**icon** | **str** | The icon associated with the property | [optional] 
**webpage_public** | **bool** | Indicates if the property is webpage public | [optional] 
**embeddable** | **bool** | Deprecated. Use sensitive instead. | [optional] 
**sensitive** | **bool** | When true, exclude from advanced query evidence | [optional] 

## Example

```python
from caraer_client.models.save_property_dto import SavePropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SavePropertyDTO from a JSON string
save_property_dto_instance = SavePropertyDTO.from_json(json)
# print the JSON string representation of the object
print(SavePropertyDTO.to_json())

# convert the object into a dict
save_property_dto_dict = save_property_dto_instance.to_dict()
# create an instance of SavePropertyDTO from a dict
save_property_dto_from_dict = SavePropertyDTO.from_dict(save_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


