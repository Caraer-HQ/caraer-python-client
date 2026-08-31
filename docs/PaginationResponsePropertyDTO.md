# PaginationResponsePropertyDTO

Paginated response (PaginationResponsePropertyDTO).

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
from caraer_client.models.pagination_response_property_dto import PaginationResponsePropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponsePropertyDTO from a JSON string
pagination_response_property_dto_instance = PaginationResponsePropertyDTO.from_json(json)
# print the JSON string representation of the object
print(PaginationResponsePropertyDTO.to_json())

# convert the object into a dict
pagination_response_property_dto_dict = pagination_response_property_dto_instance.to_dict()
# create an instance of PaginationResponsePropertyDTO from a dict
pagination_response_property_dto_from_dict = PaginationResponsePropertyDTO.from_dict(pagination_response_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


