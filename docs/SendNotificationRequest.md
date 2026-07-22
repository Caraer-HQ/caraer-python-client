# SendNotificationRequest

Request body for sending an in-app notification to a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_user_uuid** | **str** | UUID of the user who should receive the notification | 
**title** | **str** | Notification title | 
**body** | **str** | Notification body (supports Markdown for links) | 
**type** | **str** | Notification type identifier | [optional] 
**icon** | **str** | Optional icon identifier | [optional] 
**action** | **str** | Optional structured action identifier | [optional] 
**action_title** | **str** | Optional label for the action button | [optional] 
**data** | **Dict[str, Optional[object]]** | Optional action payload | [optional] 

## Example

```python
from caraer_client.models.send_notification_request import SendNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendNotificationRequest from a JSON string
send_notification_request_instance = SendNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(SendNotificationRequest.to_json())

# convert the object into a dict
send_notification_request_dict = send_notification_request_instance.to_dict()
# create an instance of SendNotificationRequest from a dict
send_notification_request_from_dict = SendNotificationRequest.from_dict(send_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


