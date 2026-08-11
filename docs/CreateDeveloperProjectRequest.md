# CreateDeveloperProjectRequest

Request body for creating (or fetching an existing) developer project for an app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str** | UUID of the app to link this project to. | [optional] 
**name** | **str** | Project name. | [optional] 
**label** | **str** | Optional human-readable label for the project. | [optional] 

## Example

```python
from caraer_client.models.create_developer_project_request import CreateDeveloperProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeveloperProjectRequest from a JSON string
create_developer_project_request_instance = CreateDeveloperProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDeveloperProjectRequest.to_json())

# convert the object into a dict
create_developer_project_request_dict = create_developer_project_request_instance.to_dict()
# create an instance of CreateDeveloperProjectRequest from a dict
create_developer_project_request_from_dict = CreateDeveloperProjectRequest.from_dict(create_developer_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


