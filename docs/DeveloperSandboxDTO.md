# DeveloperSandboxDTO

Developer sandbox: a Neo4j DB clone of the owning company. Activate via X-Caraer-Sandbox-Uuid; company identity stays the owner.

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
**owner_company_uuid** | **str** | UUID of the owning company — send this as X-Caraer-Company-Uuid | [optional] 
**database_id** | **str** | Neo4j database id of the sandbox clone | [optional] 

## Example

```python
from caraer_client.models.developer_sandbox_dto import DeveloperSandboxDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperSandboxDTO from a JSON string
developer_sandbox_dto_instance = DeveloperSandboxDTO.from_json(json)
# print the JSON string representation of the object
print(DeveloperSandboxDTO.to_json())

# convert the object into a dict
developer_sandbox_dto_dict = developer_sandbox_dto_instance.to_dict()
# create an instance of DeveloperSandboxDTO from a dict
developer_sandbox_dto_from_dict = DeveloperSandboxDTO.from_dict(developer_sandbox_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


