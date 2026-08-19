# ShowResponseAppInstallationBillingStatusDTO

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**AppInstallationBillingStatusDTO**](AppInstallationBillingStatusDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_app_installation_billing_status_dto import ShowResponseAppInstallationBillingStatusDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseAppInstallationBillingStatusDTO from a JSON string
show_response_app_installation_billing_status_dto_instance = ShowResponseAppInstallationBillingStatusDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseAppInstallationBillingStatusDTO.to_json())

# convert the object into a dict
show_response_app_installation_billing_status_dto_dict = show_response_app_installation_billing_status_dto_instance.to_dict()
# create an instance of ShowResponseAppInstallationBillingStatusDTO from a dict
show_response_app_installation_billing_status_dto_from_dict = ShowResponseAppInstallationBillingStatusDTO.from_dict(show_response_app_installation_billing_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


