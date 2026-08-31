# PaginationResponseWebMenuDTO

Paginated response (PaginationResponseWebMenuDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.pagination_response_web_menu_dto import PaginationResponseWebMenuDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponseWebMenuDTO from a JSON string
pagination_response_web_menu_dto_instance = PaginationResponseWebMenuDTO.from_json(json)
# print the JSON string representation of the object
print(PaginationResponseWebMenuDTO.to_json())

# convert the object into a dict
pagination_response_web_menu_dto_dict = pagination_response_web_menu_dto_instance.to_dict()
# create an instance of PaginationResponseWebMenuDTO from a dict
pagination_response_web_menu_dto_from_dict = PaginationResponseWebMenuDTO.from_dict(pagination_response_web_menu_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


