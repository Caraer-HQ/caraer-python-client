# PropertyDTO

Data transfer object representing a property with its configuration and metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name identifier of the property | [optional] 
**label** | **str** | Display label for the property | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**description** | **str** | Detailed description of the property&#39;s purpose and usage | [optional] 
**type** | **str** | The data type of the property (e.g., &#39;string&#39;, &#39;number&#39;, &#39;date&#39;, etc.) | [optional] 
**options** | [**List[PropertyOption]**](PropertyOption.md) | List of predefined options for properties that support selection | [optional] 
**group** | **str** | Group name for organizing related properties | [optional] 
**format** | [**PropertyDTOFormat**](PropertyDTOFormat.md) |  | [optional] 
**rules** | **List[str]** | Collection of validation rules applied to the property | [optional] 
**immutable** | **bool** | Indicates if the property value cannot be modified after initial creation | [optional] 
**hidden** | **bool** | Indicates if the property should be hidden from view | [optional] 
**lifecycle_active** | **bool** | When true, property value changes are tracked as lifecycle records | [optional] 
**non_public** | **bool** | Indicates if the property should be excluded from public APIs | [optional] 
**indexed** | **bool** | Indicates if the property should be indexed for searching | [optional] 
**editable** | **bool** | Indicates if the property value can be modified | [optional] 
**format_settings** | **Dict[str, Optional[object]]** | Additional format-specific settings for the property | [optional] 
**used_in** | [**UsedInResult**](UsedInResult.md) | Information about where this property is used in the system | [optional] 
**icon** | **str** | Icon identifier for visual representation of the property | [optional] 
**webpage_public** | **bool** | Indicates if the property can be used in webpages | [optional] 
**embeddable** | **bool** | Indicates if the property can be embedded in other properties | [optional] 
**min_and_max_value** | [**Tuple2LongLong**](Tuple2LongLong.md) | The minimum and maximum value of the property | [optional] 
**pinned** | **bool** | Indicates if the property is pinned by the logged-in user | [optional] 

## Example

```python
from caraer_client.models.property_dto import PropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyDTO from a JSON string
property_dto_instance = PropertyDTO.from_json(json)
# print the JSON string representation of the object
print(PropertyDTO.to_json())

# convert the object into a dict
property_dto_dict = property_dto_instance.to_dict()
# create an instance of PropertyDTO from a dict
property_dto_from_dict = PropertyDTO.from_dict(property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


