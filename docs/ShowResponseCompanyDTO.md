# ShowResponseCompanyDTO

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**CompanyDTO**](CompanyDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_company_dto import ShowResponseCompanyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseCompanyDTO from a JSON string
show_response_company_dto_instance = ShowResponseCompanyDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseCompanyDTO.to_json())

# convert the object into a dict
show_response_company_dto_dict = show_response_company_dto_instance.to_dict()
# create an instance of ShowResponseCompanyDTO from a dict
show_response_company_dto_from_dict = ShowResponseCompanyDTO.from_dict(show_response_company_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


