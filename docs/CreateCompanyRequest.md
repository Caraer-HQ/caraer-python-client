# CreateCompanyRequest

DTO representing a request to create a new company, including the company's name and subdomain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the company to be created. | [optional] 
**subdomain** | **str** | The desired subdomain for the company. This will be used for company-specific URLs. | [optional] 
**company_name** | **str** | The company name. | [optional] 
**copy_database_id** | **str** | The copy database id. | [optional] 
**include_records** | **bool** | Whether to include records in the company. | [optional] 
**cms_version** | **int** | CMS version for the new company: 1 &#x3D; CMS v1, 2 &#x3D; CMS v2. When omitted, the server&#39;s configured default is used. | [optional] 

## Example

```python
from caraer_client.models.create_company_request import CreateCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequest from a JSON string
create_company_request_instance = CreateCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequest.to_json())

# convert the object into a dict
create_company_request_dict = create_company_request_instance.to_dict()
# create an instance of CreateCompanyRequest from a dict
create_company_request_from_dict = CreateCompanyRequest.from_dict(create_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


