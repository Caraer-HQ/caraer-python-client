# SuccessResponseListPropertyDTO

Success response (SuccessResponseListPropertyDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.success_response_list_property_dto import SuccessResponseListPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseListPropertyDTO from a JSON string
success_response_list_property_dto_instance = SuccessResponseListPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessResponseListPropertyDTO.to_json())

# convert the object into a dict
success_response_list_property_dto_dict = success_response_list_property_dto_instance.to_dict()
# create an instance of SuccessResponseListPropertyDTO from a dict
success_response_list_property_dto_from_dict = SuccessResponseListPropertyDTO.from_dict(success_response_list_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


