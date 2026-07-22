# PaginationResponse

Response object for paginated data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | **List[object]** | The data returned in the current page of the pagination. | [optional] 
**total** | **int** | The total number of items available. | [optional] 
**page** | **int** | The current page number (starts from 1). | [optional] 
**per_page** | **int** | The number of items displayed per page. | [optional] 
**last_page** | **int** | The last page number available for the pagination. | [optional] 

## Example

```python
from caraer_client.models.pagination_response import PaginationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponse from a JSON string
pagination_response_instance = PaginationResponse.from_json(json)
# print the JSON string representation of the object
print(PaginationResponse.to_json())

# convert the object into a dict
pagination_response_dict = pagination_response_instance.to_dict()
# create an instance of PaginationResponse from a dict
pagination_response_from_dict = PaginationResponse.from_dict(pagination_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


