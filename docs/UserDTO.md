# UserDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**initials** | **str** |  | [optional] 
**selected_company** | [**CompanyDTO**](CompanyDTO.md) |  | [optional] 
**companies** | [**List[SimpleCompanyDTO]**](SimpleCompanyDTO.md) |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) |  | [optional] 
**role** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**token** | [**ApiTokenDTO**](ApiTokenDTO.md) |  | [optional] 
**record** | [**Record**](Record.md) |  | [optional] 
**easter_eggs** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.user_dto import UserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserDTO from a JSON string
user_dto_instance = UserDTO.from_json(json)
# print the JSON string representation of the object
print(UserDTO.to_json())

# convert the object into a dict
user_dto_dict = user_dto_instance.to_dict()
# create an instance of UserDTO from a dict
user_dto_from_dict = UserDTO.from_dict(user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


