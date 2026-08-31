# PaginationResponseObject

Paginated response (PaginationResponseObject).

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
from caraer_client.models.pagination_response_object import PaginationResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponseObject from a JSON string
pagination_response_object_instance = PaginationResponseObject.from_json(json)
# print the JSON string representation of the object
print(PaginationResponseObject.to_json())

# convert the object into a dict
pagination_response_object_dict = pagination_response_object_instance.to_dict()
# create an instance of PaginationResponseObject from a dict
pagination_response_object_from_dict = PaginationResponseObject.from_dict(pagination_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


