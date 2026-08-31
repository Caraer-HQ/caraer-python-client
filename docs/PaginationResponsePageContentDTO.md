# PaginationResponsePageContentDTO

Paginated response (PaginationResponsePageContentDTO).

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
from caraer_client.models.pagination_response_page_content_dto import PaginationResponsePageContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponsePageContentDTO from a JSON string
pagination_response_page_content_dto_instance = PaginationResponsePageContentDTO.from_json(json)
# print the JSON string representation of the object
print(PaginationResponsePageContentDTO.to_json())

# convert the object into a dict
pagination_response_page_content_dto_dict = pagination_response_page_content_dto_instance.to_dict()
# create an instance of PaginationResponsePageContentDTO from a dict
pagination_response_page_content_dto_from_dict = PaginationResponsePageContentDTO.from_dict(pagination_response_page_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


