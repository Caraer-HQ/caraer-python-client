# ProjectBuildDTO

Data transfer object for a developer project build artifact.

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
**status** | **str** | PENDING, READY, or FAILED | [optional] 
**target** | **str** | production or sandbox | [optional] 
**artifact_gcs_path** | **str** | GCS object path of the uploaded build archive | [optional] 
**manifest_json** | **str** | Parsed build manifest (functions, webhooks, app fields), serialized as JSON | [optional] 
**error_message** | **str** | Error message if the build failed | [optional] 
**version** | **str** | Semantic version for this build | [optional] 
**release_notes** | **str** | Release notes for this build | [optional] 

## Example

```python
from caraer_client.models.project_build_dto import ProjectBuildDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBuildDTO from a JSON string
project_build_dto_instance = ProjectBuildDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectBuildDTO.to_json())

# convert the object into a dict
project_build_dto_dict = project_build_dto_instance.to_dict()
# create an instance of ProjectBuildDTO from a dict
project_build_dto_from_dict = ProjectBuildDTO.from_dict(project_build_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


