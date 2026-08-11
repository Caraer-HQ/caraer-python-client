# EventRsvpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partstat** | **str** | Participation status on the attendees edge | 
**scope** | **str** | Series scope for recurring events. Defaults to this. | [optional] 

## Example

```python
from caraer_client.models.event_rsvp_request import EventRsvpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventRsvpRequest from a JSON string
event_rsvp_request_instance = EventRsvpRequest.from_json(json)
# print the JSON string representation of the object
print(EventRsvpRequest.to_json())

# convert the object into a dict
event_rsvp_request_dict = event_rsvp_request_instance.to_dict()
# create an instance of EventRsvpRequest from a dict
event_rsvp_request_from_dict = EventRsvpRequest.from_dict(event_rsvp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


