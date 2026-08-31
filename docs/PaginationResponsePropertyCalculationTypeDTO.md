# PaginationResponsePropertyCalculationTypeDTO

Paginated response (PaginationResponsePropertyCalculationTypeDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 

## Example

```python
from caraer_client.models.pagination_response_property_calculation_type_dto import PaginationResponsePropertyCalculationTypeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponsePropertyCalculationTypeDTO from a JSON string
pagination_response_property_calculation_type_dto_instance = PaginationResponsePropertyCalculationTypeDTO.from_json(json)
# print the JSON string representation of the object
print(PaginationResponsePropertyCalculationTypeDTO.to_json())

# convert the object into a dict
pagination_response_property_calculation_type_dto_dict = pagination_response_property_calculation_type_dto_instance.to_dict()
# create an instance of PaginationResponsePropertyCalculationTypeDTO from a dict
pagination_response_property_calculation_type_dto_from_dict = PaginationResponsePropertyCalculationTypeDTO.from_dict(pagination_response_property_calculation_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


