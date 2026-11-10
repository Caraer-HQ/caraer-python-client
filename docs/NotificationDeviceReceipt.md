# NotificationDeviceReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_id** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.notification_device_receipt import NotificationDeviceReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDeviceReceipt from a JSON string
notification_device_receipt_instance = NotificationDeviceReceipt.from_json(json)
# print the JSON string representation of the object
print(NotificationDeviceReceipt.to_json())

# convert the object into a dict
notification_device_receipt_dict = notification_device_receipt_instance.to_dict()
# create an instance of NotificationDeviceReceipt from a dict
notification_device_receipt_from_dict = NotificationDeviceReceipt.from_dict(notification_device_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


