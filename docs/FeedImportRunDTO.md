# FeedImportRunDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**item_count** | **int** |  | [optional] 
**created** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 
**failed** | **int** |  | [optional] 
**published** | **int** |  | [optional] 
**unpublished** | **int** |  | [optional] 
**skipped** | **int** |  | [optional] 
**sample_incomplete** | **bool** |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**items** | **List[Dict[str, Optional[object]]]** |  | [optional] 
**keys** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.feed_import_run_dto import FeedImportRunDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FeedImportRunDTO from a JSON string
feed_import_run_dto_instance = FeedImportRunDTO.from_json(json)
# print the JSON string representation of the object
print(FeedImportRunDTO.to_json())

# convert the object into a dict
feed_import_run_dto_dict = feed_import_run_dto_instance.to_dict()
# create an instance of FeedImportRunDTO from a dict
feed_import_run_dto_from_dict = FeedImportRunDTO.from_dict(feed_import_run_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


