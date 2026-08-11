# DeployBuildRequest

Request body for deploying a developer project build.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | Deploy target: production or sandbox. Defaults to the build&#39;s target. | [optional] 
**prune** | **bool** | When true, soft-delete remote functions/webhooks/schedules/inbound routes/OAuth providers that are absent from the build archive. Defaults to false. | [optional] 

## Example

```python
from caraer_client.models.deploy_build_request import DeployBuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeployBuildRequest from a JSON string
deploy_build_request_instance = DeployBuildRequest.from_json(json)
# print the JSON string representation of the object
print(DeployBuildRequest.to_json())

# convert the object into a dict
deploy_build_request_dict = deploy_build_request_instance.to_dict()
# create an instance of DeployBuildRequest from a dict
deploy_build_request_from_dict = DeployBuildRequest.from_dict(deploy_build_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


