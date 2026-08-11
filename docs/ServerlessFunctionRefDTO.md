# ServerlessFunctionRefDTO

Reference to a serverless function by uuid and/or name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.serverless_function_ref_dto import ServerlessFunctionRefDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ServerlessFunctionRefDTO from a JSON string
serverless_function_ref_dto_instance = ServerlessFunctionRefDTO.from_json(json)
# print the JSON string representation of the object
print(ServerlessFunctionRefDTO.to_json())

# convert the object into a dict
serverless_function_ref_dto_dict = serverless_function_ref_dto_instance.to_dict()
# create an instance of ServerlessFunctionRefDTO from a dict
serverless_function_ref_dto_from_dict = ServerlessFunctionRefDTO.from_dict(serverless_function_ref_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


