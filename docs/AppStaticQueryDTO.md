# AppStaticQueryDTO

Read-only Cypher snapshot used by static_query line items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | **str** | When the query runs: period_end (default) or period_start | [optional] 
**cypher** | **str** | Read-only Cypher that returns count(...) AS count | [optional] 

## Example

```python
from caraer_client.models.app_static_query_dto import AppStaticQueryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AppStaticQueryDTO from a JSON string
app_static_query_dto_instance = AppStaticQueryDTO.from_json(json)
# print the JSON string representation of the object
print(AppStaticQueryDTO.to_json())

# convert the object into a dict
app_static_query_dto_dict = app_static_query_dto_instance.to_dict()
# create an instance of AppStaticQueryDTO from a dict
app_static_query_dto_from_dict = AppStaticQueryDTO.from_dict(app_static_query_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


