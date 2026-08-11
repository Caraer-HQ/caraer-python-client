# CreateProjectBuildRequest

Request body for uploading a developer project build archive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_base64** | **str** | Base64-encoded zip archive containing caraer.project.json and src/app. | [optional] 
**filename** | **str** | Original archive filename, for traceability. | [optional] 
**target** | **str** | Deploy target: production or sandbox. | [optional] 
**version** | **str** | Semantic version for this build (MAJOR.MINOR.PATCH). Auto-bumped when omitted. | [optional] 
**release_notes** | **str** | Release notes for this build. | [optional] 

## Example

```python
from caraer_client.models.create_project_build_request import CreateProjectBuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectBuildRequest from a JSON string
create_project_build_request_instance = CreateProjectBuildRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectBuildRequest.to_json())

# convert the object into a dict
create_project_build_request_dict = create_project_build_request_instance.to_dict()
# create an instance of CreateProjectBuildRequest from a dict
create_project_build_request_from_dict = CreateProjectBuildRequest.from_dict(create_project_build_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


