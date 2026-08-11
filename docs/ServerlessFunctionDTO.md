# ServerlessFunctionDTO

Data transfer object for a serverless function (runtime and code) owned by an app

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
**runtime** | **str** | Runtime identifier (e.g. javascript, python) | [optional] 
**code** | **str** | Function source code | [optional] 
**source_files** | **Dict[str, str]** | Additional source files relative to the function folder (e.g. shared.js) | [optional] 
**description** | **str** | Optional description of the serverless function | [optional] 

## Example

```python
from caraer_client.models.serverless_function_dto import ServerlessFunctionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ServerlessFunctionDTO from a JSON string
serverless_function_dto_instance = ServerlessFunctionDTO.from_json(json)
# print the JSON string representation of the object
print(ServerlessFunctionDTO.to_json())

# convert the object into a dict
serverless_function_dto_dict = serverless_function_dto_instance.to_dict()
# create an instance of ServerlessFunctionDTO from a dict
serverless_function_dto_from_dict = ServerlessFunctionDTO.from_dict(serverless_function_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


