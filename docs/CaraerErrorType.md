# CaraerErrorType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message providing details about the failure. | 
**type** | **str** | The type of error. | 
**correction_suggestion** | **str** | A suggestion on how to correct the error. | 

## Example

```python
from caraer_client.models.caraer_error_type import CaraerErrorType

# TODO update the JSON string below
json = "{}"
# create an instance of CaraerErrorType from a JSON string
caraer_error_type_instance = CaraerErrorType.from_json(json)
# print the JSON string representation of the object
print(CaraerErrorType.to_json())

# convert the object into a dict
caraer_error_type_dict = caraer_error_type_instance.to_dict()
# create an instance of CaraerErrorType from a dict
caraer_error_type_from_dict = CaraerErrorType.from_dict(caraer_error_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


