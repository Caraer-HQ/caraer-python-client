# CreateOrUpdateEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** |  | [optional] 
**webpage_objects** | [**List[CaraerObjectDTO]**](CaraerObjectDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.create_or_update_environment_request import CreateOrUpdateEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateEnvironmentRequest from a JSON string
create_or_update_environment_request_instance = CreateOrUpdateEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateEnvironmentRequest.to_json())

# convert the object into a dict
create_or_update_environment_request_dict = create_or_update_environment_request_instance.to_dict()
# create an instance of CreateOrUpdateEnvironmentRequest from a dict
create_or_update_environment_request_from_dict = CreateOrUpdateEnvironmentRequest.from_dict(create_or_update_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


