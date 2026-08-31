# FlowPaginationRequest

Request DTO for paginated data flow with filters, sorting, displayed items, and related information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crud** | [**CRUD**](CRUD.md) |  | [optional] 
**show_items** | [**List[ShowItem]**](ShowItem.md) |  | [optional] 
**page** | **int** | The page index (one-based) to request. | [optional] 
**limit** | **int** | The number of records to retrieve per page. | [optional] 
**filter** | [**Filter**](Filter.md) | Filters applied to the query. | [optional] 
**sort** | [**List[SortItem]**](SortItem.md) | Sorting options for the query. | [optional] 
**show** | [**List[ShowItem]**](ShowItem.md) | Specifies what data to show in the response. | [optional] 
**query** | **str** | A free-text search query applied to the records. | [optional] 
**preview** | **str** | Preview information for the records, if supported. | [optional] 
**main_object** | **str** | The main object for categorization or context. | [optional] 
**column** | **str** | Column name for sorting or filtering data | [optional] 
**var_property** | **str** | UUID of the property used in the request | [optional] 

## Example

```python
from caraer_client.models.flow_pagination_request import FlowPaginationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowPaginationRequest from a JSON string
flow_pagination_request_instance = FlowPaginationRequest.from_json(json)
# print the JSON string representation of the object
print(FlowPaginationRequest.to_json())

# convert the object into a dict
flow_pagination_request_dict = flow_pagination_request_instance.to_dict()
# create an instance of FlowPaginationRequest from a dict
flow_pagination_request_from_dict = FlowPaginationRequest.from_dict(flow_pagination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


