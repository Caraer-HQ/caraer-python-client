# FormRelationDTO

Data transfer object representing a form relation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the form relation. The options are: CONVERSION_PAGE_RECORD, RELATED_RECORD_TO_CONVERSION_PAGE_RECORD, STATIC | [optional] 
**relation** | [**RelationDTO**](RelationDTO.md) | The relation to be created. | [optional] 
**related_relation** | [**RelationDTO**](RelationDTO.md) | The related relation associated with conversion page record | [optional] 
**related_object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | The related object associated with conversion page record or for static | [optional] 
**record_uuid** | **str** | UUID of the record for the static connection. | [optional] 
**related_object_connection** | **str** | The connection type for the related object. The options are: PRIMARY, ALL | [optional] 

## Example

```python
from caraer_client.models.form_relation_dto import FormRelationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FormRelationDTO from a JSON string
form_relation_dto_instance = FormRelationDTO.from_json(json)
# print the JSON string representation of the object
print(FormRelationDTO.to_json())

# convert the object into a dict
form_relation_dto_dict = form_relation_dto_instance.to_dict()
# create an instance of FormRelationDTO from a dict
form_relation_dto_from_dict = FormRelationDTO.from_dict(form_relation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


