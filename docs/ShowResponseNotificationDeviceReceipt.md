# ShowResponseNotificationDeviceReceipt

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**NotificationDeviceReceipt**](NotificationDeviceReceipt.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_notification_device_receipt import ShowResponseNotificationDeviceReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseNotificationDeviceReceipt from a JSON string
show_response_notification_device_receipt_instance = ShowResponseNotificationDeviceReceipt.from_json(json)
# print the JSON string representation of the object
print(ShowResponseNotificationDeviceReceipt.to_json())

# convert the object into a dict
show_response_notification_device_receipt_dict = show_response_notification_device_receipt_instance.to_dict()
# create an instance of ShowResponseNotificationDeviceReceipt from a dict
show_response_notification_device_receipt_from_dict = ShowResponseNotificationDeviceReceipt.from_dict(show_response_notification_device_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


