# CreateDeveloperSandboxRequest

Request body for creating a developer sandbox.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sandbox name. | [optional] 
**label** | **str** | Optional human-readable label for the sandbox. | [optional] 

## Example

```python
from caraer_client.models.create_developer_sandbox_request import CreateDeveloperSandboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeveloperSandboxRequest from a JSON string
create_developer_sandbox_request_instance = CreateDeveloperSandboxRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDeveloperSandboxRequest.to_json())

# convert the object into a dict
create_developer_sandbox_request_dict = create_developer_sandbox_request_instance.to_dict()
# create an instance of CreateDeveloperSandboxRequest from a dict
create_developer_sandbox_request_from_dict = CreateDeveloperSandboxRequest.from_dict(create_developer_sandbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


