# PaginationResponseSavedFilterDTO

Paginated response (PaginationResponseSavedFilterDTO).

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
from caraer_client.models.pagination_response_saved_filter_dto import PaginationResponseSavedFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponseSavedFilterDTO from a JSON string
pagination_response_saved_filter_dto_instance = PaginationResponseSavedFilterDTO.from_json(json)
# print the JSON string representation of the object
print(PaginationResponseSavedFilterDTO.to_json())

# convert the object into a dict
pagination_response_saved_filter_dto_dict = pagination_response_saved_filter_dto_instance.to_dict()
# create an instance of PaginationResponseSavedFilterDTO from a dict
pagination_response_saved_filter_dto_from_dict = PaginationResponseSavedFilterDTO.from_dict(pagination_response_saved_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


