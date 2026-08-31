# SuccessResponseListAggregateResponse

Success response (SuccessResponseListAggregateResponse).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_list_aggregate_response import SuccessResponseListAggregateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseListAggregateResponse from a JSON string
success_response_list_aggregate_response_instance = SuccessResponseListAggregateResponse.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseListAggregateResponse.to_json())

# convert the object into a dict
success_response_list_aggregate_response_dict = success_response_list_aggregate_response_instance.to_dict()
# create an instance of SuccessResponseListAggregateResponse from a dict
success_response_list_aggregate_response_from_dict = SuccessResponseListAggregateResponse.from_dict(success_response_list_aggregate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


