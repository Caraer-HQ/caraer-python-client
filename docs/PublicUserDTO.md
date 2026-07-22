# PublicUserDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**initials** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) |  | [optional] 
**role** | **str** |  | [optional] 
**record** | [**Record**](Record.md) |  | [optional] 

## Example

```python
from caraer_client.models.public_user_dto import PublicUserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PublicUserDTO from a JSON string
public_user_dto_instance = PublicUserDTO.from_json(json)
# print the JSON string representation of the object
print(PublicUserDTO.to_json())

# convert the object into a dict
public_user_dto_dict = public_user_dto_instance.to_dict()
# create an instance of PublicUserDTO from a dict
public_user_dto_from_dict = PublicUserDTO.from_dict(public_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


