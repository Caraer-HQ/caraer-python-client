# AppRequest

Settings required to uninstall the application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md) | A map of configuration settings. The keys are strings representing the setting names, and the values represent the setting values, which can be different types. | [optional] 

## Example

```python
from caraer_client.models.app_request import AppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppRequest from a JSON string
app_request_instance = AppRequest.from_json(json)
# print the JSON string representation of the object
print(AppRequest.to_json())

# convert the object into a dict
app_request_dict = app_request_instance.to_dict()
# create an instance of AppRequest from a dict
app_request_from_dict = AppRequest.from_dict(app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


