# TestServerlessFunctionRequest

Request body for testing a serverless function with a specific record and event type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_uuid** | **str** | UUID of the record to base the event on. | [optional] 
**event_type** | **str** | Event type to simulate (created, updated, deleted, etc.). | [optional] 
**force_provision** | **bool** | If true, forces re-provisioning of the serverless function before invocation. | [optional] 

## Example

```python
from caraer_client.models.test_serverless_function_request import TestServerlessFunctionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestServerlessFunctionRequest from a JSON string
test_serverless_function_request_instance = TestServerlessFunctionRequest.from_json(json)
# print the JSON string representation of the object
print(TestServerlessFunctionRequest.to_json())

# convert the object into a dict
test_serverless_function_request_dict = test_serverless_function_request_instance.to_dict()
# create an instance of TestServerlessFunctionRequest from a dict
test_serverless_function_request_from_dict = TestServerlessFunctionRequest.from_dict(test_serverless_function_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


