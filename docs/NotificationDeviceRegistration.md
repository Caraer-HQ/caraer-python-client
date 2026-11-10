# NotificationDeviceRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**registration_kind** | **str** |  | [optional] 
**registration** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.notification_device_registration import NotificationDeviceRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDeviceRegistration from a JSON string
notification_device_registration_instance = NotificationDeviceRegistration.from_json(json)
# print the JSON string representation of the object
print(NotificationDeviceRegistration.to_json())

# convert the object into a dict
notification_device_registration_dict = notification_device_registration_instance.to_dict()
# create an instance of NotificationDeviceRegistration from a dict
notification_device_registration_from_dict = NotificationDeviceRegistration.from_dict(notification_device_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


