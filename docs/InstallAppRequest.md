# InstallAppRequest

Optional initial configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[AppSettingFieldSchema]**](AppSettingFieldSchema.md) | Optional initial configuration settings (key-value via AppSettingFieldSchema name/value). | [optional] 
**scopes** | **List[str]** | Optional scopes to grant to the app. | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) | Optional per-object record filters for this installation (object name → filter). | [optional] 
**app_bar_visibility** | [**Dict[str, AppBarVisibilityEntry]**](AppBarVisibilityEntry.md) | Optional per-app-bar placement config keyed by app bar UUID. | [optional] 
**selected_pricing_plan_uuid** | **str** | UUID of the pricing plan selected for this installation. | [optional] 

## Example

```python
from caraer_client.models.install_app_request import InstallAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstallAppRequest from a JSON string
install_app_request_instance = InstallAppRequest.from_json(json)
# print the JSON string representation of the object
print(InstallAppRequest.to_json())

# convert the object into a dict
install_app_request_dict = install_app_request_instance.to_dict()
# create an instance of InstallAppRequest from a dict
install_app_request_from_dict = InstallAppRequest.from_dict(install_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


