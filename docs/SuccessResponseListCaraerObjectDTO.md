# SuccessResponseListCaraerObjectDTO

Success response (SuccessResponseListCaraerObjectDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_list_caraer_object_dto import SuccessResponseListCaraerObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseListCaraerObjectDTO from a JSON string
success_response_list_caraer_object_dto_instance = SuccessResponseListCaraerObjectDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseListCaraerObjectDTO.to_json())

# convert the object into a dict
success_response_list_caraer_object_dto_dict = success_response_list_caraer_object_dto_instance.to_dict()
# create an instance of SuccessResponseListCaraerObjectDTO from a dict
success_response_list_caraer_object_dto_from_dict = SuccessResponseListCaraerObjectDTO.from_dict(success_response_list_caraer_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


