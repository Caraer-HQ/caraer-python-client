# RecordPaginationRequest

Contains pagination details and optional query parameters such as filter, sort, and show options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page index (one-based) to request. | [optional] 
**limit** | **int** | The number of records to retrieve per page. | [optional] 
**filter** | **object** | Filters applied to the query. | [optional] 
**sort** | **List[object]** | Sorting options for the query. | [optional] 
**show** | **List[object]** | Specifies what data to show in the response. | [optional] 
**query** | **str** | A free-text search query applied to the records. | [optional] 
**preview** | **str** | Preview information for the records, if supported. | [optional] 
**main_object** | **str** | The main object for categorization or context. | [optional] 
**column** | **str** | The column to group the records by. | [optional] 

## Example

```python
from caraer_client.models.record_pagination_request import RecordPaginationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordPaginationRequest from a JSON string
record_pagination_request_instance = RecordPaginationRequest.from_json(json)
# print the JSON string representation of the object
print(RecordPaginationRequest.to_json())

# convert the object into a dict
record_pagination_request_dict = record_pagination_request_instance.to_dict()
# create an instance of RecordPaginationRequest from a dict
record_pagination_request_from_dict = RecordPaginationRequest.from_dict(record_pagination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


