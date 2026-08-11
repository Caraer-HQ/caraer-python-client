# CrossObjectRecordSearchRequest

Request DTO for searching records across multiple objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Free-text search query. | [optional] 
**from_object_uuid** | **str** | Event (or source) object UUID used with relationName to resolve target objects. | [optional] 
**relation_name** | **str** | Relation name whose connected target objects are searched (e.g. attendees). | [optional] 
**object_uuids** | **List[str]** | Object UUIDs to search. Used on their own when relationName is omitted; combined with relationName they narrow the relation&#39;s target objects. | [optional] 
**object_names** | **List[str]** | Object internal names to search. Behaves like objectUuids and may be combined with it. | [optional] 
**preview** | **str** | Preview template name. | [optional] 
**page** | **int** | Page number (1-based). | [optional] 
**limit** | **int** | Maximum records returned. | [optional] 
**exclude_record_uuid** | **str** | Optional record UUID to exclude from results. | [optional] 

## Example

```python
from caraer_client.models.cross_object_record_search_request import CrossObjectRecordSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossObjectRecordSearchRequest from a JSON string
cross_object_record_search_request_instance = CrossObjectRecordSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CrossObjectRecordSearchRequest.to_json())

# convert the object into a dict
cross_object_record_search_request_dict = cross_object_record_search_request_instance.to_dict()
# create an instance of CrossObjectRecordSearchRequest from a dict
cross_object_record_search_request_from_dict = CrossObjectRecordSearchRequest.from_dict(cross_object_record_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


