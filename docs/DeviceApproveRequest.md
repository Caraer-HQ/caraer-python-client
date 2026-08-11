# DeviceApproveRequest

Approve a pending device-code login (authenticated browser session)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_code** | **str** | User-facing code shown by the CLI | 

## Example

```python
from caraer_client.models.device_approve_request import DeviceApproveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceApproveRequest from a JSON string
device_approve_request_instance = DeviceApproveRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceApproveRequest.to_json())

# convert the object into a dict
device_approve_request_dict = device_approve_request_instance.to_dict()
# create an instance of DeviceApproveRequest from a dict
device_approve_request_from_dict = DeviceApproveRequest.from_dict(device_approve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


