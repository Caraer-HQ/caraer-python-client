# PaginationResponseAppDTO

Paginated response (PaginationResponseAppDTO).

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
from caraer_client.models.pagination_response_app_dto import PaginationResponseAppDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponseAppDTO from a JSON string
pagination_response_app_dto_instance = PaginationResponseAppDTO.from_json(json)
# print the JSON string representation of the object
print(PaginationResponseAppDTO.to_json())

# convert the object into a dict
pagination_response_app_dto_dict = pagination_response_app_dto_instance.to_dict()
# create an instance of PaginationResponseAppDTO from a dict
pagination_response_app_dto_from_dict = PaginationResponseAppDTO.from_dict(pagination_response_app_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


