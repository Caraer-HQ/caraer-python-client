# SavedFilterDTO

Data transfer object representing a saved filter configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name identifier of the saved filter | 
**label** | **str** | Display label for the saved filter | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**description** | **str** | Description of what this saved filter is used for | [optional] 
**main_object** | **str** | The main object for the saved filter | [optional] 
**filter** | [**Filter**](Filter.md) | The filter definition used when querying records | [optional] 

## Example

```python
from caraer_client.models.saved_filter_dto import SavedFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SavedFilterDTO from a JSON string
saved_filter_dto_instance = SavedFilterDTO.from_json(json)
# print the JSON string representation of the object
print(SavedFilterDTO.to_json())

# convert the object into a dict
saved_filter_dto_dict = saved_filter_dto_instance.to_dict()
# create an instance of SavedFilterDTO from a dict
saved_filter_dto_from_dict = SavedFilterDTO.from_dict(saved_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


