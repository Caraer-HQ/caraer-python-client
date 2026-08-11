# DevicePollRequest

Poll a device-code login session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** | Device code returned by /auth/device/start | 

## Example

```python
from caraer_client.models.device_poll_request import DevicePollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePollRequest from a JSON string
device_poll_request_instance = DevicePollRequest.from_json(json)
# print the JSON string representation of the object
print(DevicePollRequest.to_json())

# convert the object into a dict
device_poll_request_dict = device_poll_request_instance.to_dict()
# create an instance of DevicePollRequest from a dict
device_poll_request_from_dict = DevicePollRequest.from_dict(device_poll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


