# ProjectDeployDTO

Data transfer object for a developer project deploy.

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
**project_uuid** | **str** | UUID of the owning developer project | [optional] 
**build_uuid** | **str** | UUID of the build that was deployed | [optional] 
**version** | **str** | Semantic version of the deployed build | [optional] 
**status** | **str** | PENDING, SUCCEEDED, FAILED, or PARTIAL | [optional] 
**target** | **str** | production or sandbox | [optional] 
**results_json** | **str** | Per-component reconciliation results (app, functions, webhooks), serialized as JSON | [optional] 
**activated_at** | **int** | Unix timestamp (ms) when this deploy was activated | [optional] 

## Example

```python
from caraer_client.models.project_deploy_dto import ProjectDeployDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeployDTO from a JSON string
project_deploy_dto_instance = ProjectDeployDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectDeployDTO.to_json())

# convert the object into a dict
project_deploy_dto_dict = project_deploy_dto_instance.to_dict()
# create an instance of ProjectDeployDTO from a dict
project_deploy_dto_from_dict = ProjectDeployDTO.from_dict(project_deploy_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


