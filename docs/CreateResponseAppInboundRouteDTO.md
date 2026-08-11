# CreateResponseAppInboundRouteDTO

Response for a successful resource creation operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**AppInboundRouteDTO**](AppInboundRouteDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.create_response_app_inbound_route_dto import CreateResponseAppInboundRouteDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponseAppInboundRouteDTO from a JSON string
create_response_app_inbound_route_dto_instance = CreateResponseAppInboundRouteDTO.from_json(json)
# print the JSON string representation of the object
print(CreateResponseAppInboundRouteDTO.to_json())

# convert the object into a dict
create_response_app_inbound_route_dto_dict = create_response_app_inbound_route_dto_instance.to_dict()
# create an instance of CreateResponseAppInboundRouteDTO from a dict
create_response_app_inbound_route_dto_from_dict = CreateResponseAppInboundRouteDTO.from_dict(create_response_app_inbound_route_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


