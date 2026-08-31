# PaginationResponsePropertyFormat

Paginated response (PaginationResponsePropertyFormat).

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
from caraer_client.models.pagination_response_property_format import PaginationResponsePropertyFormat

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponsePropertyFormat from a JSON string
pagination_response_property_format_instance = PaginationResponsePropertyFormat.from_json(json)
# print the JSON string representation of the object
print(PaginationResponsePropertyFormat.to_json())

# convert the object into a dict
pagination_response_property_format_dict = pagination_response_property_format_instance.to_dict()
# create an instance of PaginationResponsePropertyFormat from a dict
pagination_response_property_format_from_dict = PaginationResponsePropertyFormat.from_dict(pagination_response_property_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


