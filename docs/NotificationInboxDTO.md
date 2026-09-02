# NotificationInboxDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | [**List[Item]**](Item.md) |  | [optional] 
**unread_count** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.notification_inbox_dto import NotificationInboxDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationInboxDTO from a JSON string
notification_inbox_dto_instance = NotificationInboxDTO.from_json(json)
# print the JSON string representation of the object
print(NotificationInboxDTO.to_json())

# convert the object into a dict
notification_inbox_dto_dict = notification_inbox_dto_instance.to_dict()
# create an instance of NotificationInboxDTO from a dict
notification_inbox_dto_from_dict = NotificationInboxDTO.from_dict(notification_inbox_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


