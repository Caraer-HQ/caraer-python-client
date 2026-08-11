# AppInboundRouteDTO

Public inbound route into an app function

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**auth_mode** | **str** |  | [optional] 
**enqueue** | **bool** |  | [optional] 
**has_shared_secret** | **bool** |  | [optional] 
**shared_secret** | **str** |  | [optional] 
**serverless_function** | [**ServerlessFunctionRefDTO**](ServerlessFunctionRefDTO.md) |  | [optional] 

## Example

```python
from caraer_client.models.app_inbound_route_dto import AppInboundRouteDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppInboundRouteDTO from a JSON string
app_inbound_route_dto_instance = AppInboundRouteDTO.from_json(json)
# print the JSON string representation of the object
print(AppInboundRouteDTO.to_json())

# convert the object into a dict
app_inbound_route_dto_dict = app_inbound_route_dto_instance.to_dict()
# create an instance of AppInboundRouteDTO from a dict
app_inbound_route_dto_from_dict = AppInboundRouteDTO.from_dict(app_inbound_route_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


