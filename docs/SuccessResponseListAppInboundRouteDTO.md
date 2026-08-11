# SuccessResponseListAppInboundRouteDTO

Represents a standard successful response with a message and optional data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**List[AppInboundRouteDTO]**](AppInboundRouteDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.success_response_list_app_inbound_route_dto import SuccessResponseListAppInboundRouteDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseListAppInboundRouteDTO from a JSON string
success_response_list_app_inbound_route_dto_instance = SuccessResponseListAppInboundRouteDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseListAppInboundRouteDTO.to_json())

# convert the object into a dict
success_response_list_app_inbound_route_dto_dict = success_response_list_app_inbound_route_dto_instance.to_dict()
# create an instance of SuccessResponseListAppInboundRouteDTO from a dict
success_response_list_app_inbound_route_dto_from_dict = SuccessResponseListAppInboundRouteDTO.from_dict(success_response_list_app_inbound_route_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


