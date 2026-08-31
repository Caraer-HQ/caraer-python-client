# SuccessResponseCollectionRelation

Success response (SuccessResponseCollectionRelation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_collection_relation import SuccessResponseCollectionRelation

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseCollectionRelation from a JSON string
success_response_collection_relation_instance = SuccessResponseCollectionRelation.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseCollectionRelation.to_json())

# convert the object into a dict
success_response_collection_relation_dict = success_response_collection_relation_instance.to_dict()
# create an instance of SuccessResponseCollectionRelation from a dict
success_response_collection_relation_from_dict = SuccessResponseCollectionRelation.from_dict(success_response_collection_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


