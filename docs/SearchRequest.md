# SearchRequest

Request DTO for searching records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query to search for. | [optional] 
**object_uuid** | **str** | The UUID of the object to search in. | [optional] 
**limit** | **int** | The limit of the search. | [optional] 
**page** | **int** | The page of the search. | [optional] 
**preview** | **str** | The preview of the search. | [optional] 

## Example

```python
from caraer_client.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print(SearchRequest.to_json())

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_from_dict = SearchRequest.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


