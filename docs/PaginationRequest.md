# PaginationRequest

Pagination and filtering options for the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **List[Dict[str, Optional[object]]]** | A list of key-value pairs representing filter criteria for the request. Keys represent fields to filter by, operator can be any of the following: &#39;&#x3D;&#39;, &#39;&gt;&#39;, &#39;&lt;&#39;, &#39;&gt;&#x3D;&#39;, &#39;&lt;&#x3D;&#39;, (not) &#39;in&#39;, &#39;(not) contains&#39;, &#39;(not) startswith&#39;, &#39;(not) endswith&#39;, &#39;(not) isnull&#39;. | [optional] 
**sort** | **List[Dict[str, str]]** | A list of key-value pairs representing sorting criteria. Keys represent fields to sort by, and values define the sort direction (e.g., &#39;asc&#39; or &#39;desc&#39;). | [optional] 
**show** | **List[str]** | A list of field names specifying which fields to include in the response. | [optional] 
**limit** | **int** | The maximum number of items to retrieve per page. | [optional] 
**page** | **int** | The page number to retrieve in the paginated response (1-based index). | [optional] 
**query** | **str** | Optional search query to filter results. This will apply to all properties on the entity. | [optional] 

## Example

```python
from caraer_client.models.pagination_request import PaginationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequest from a JSON string
pagination_request_instance = PaginationRequest.from_json(json)
# print the JSON string representation of the object
print(PaginationRequest.to_json())

# convert the object into a dict
pagination_request_dict = pagination_request_instance.to_dict()
# create an instance of PaginationRequest from a dict
pagination_request_from_dict = PaginationRequest.from_dict(pagination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


