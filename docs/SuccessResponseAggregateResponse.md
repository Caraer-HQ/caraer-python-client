# SuccessResponseAggregateResponse

Success response (SuccessResponseAggregateResponse).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_aggregate_response import SuccessResponseAggregateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseAggregateResponse from a JSON string
success_response_aggregate_response_instance = SuccessResponseAggregateResponse.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseAggregateResponse.to_json())

# convert the object into a dict
success_response_aggregate_response_dict = success_response_aggregate_response_instance.to_dict()
# create an instance of SuccessResponseAggregateResponse from a dict
success_response_aggregate_response_from_dict = SuccessResponseAggregateResponse.from_dict(success_response_aggregate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


