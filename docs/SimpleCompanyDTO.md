# SimpleCompanyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.simple_company_dto import SimpleCompanyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCompanyDTO from a JSON string
simple_company_dto_instance = SimpleCompanyDTO.from_json(json)
# print the JSON string representation of the object
print(SimpleCompanyDTO.to_json())

# convert the object into a dict
simple_company_dto_dict = simple_company_dto_instance.to_dict()
# create an instance of SimpleCompanyDTO from a dict
simple_company_dto_from_dict = SimpleCompanyDTO.from_dict(simple_company_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


