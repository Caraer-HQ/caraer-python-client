# UpdateLifecyclePropertiesDTO

Request body for enabling lifecycle tracking on object properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_uuids** | **List[str]** | UUIDs of properties to track in lifecycle history | [optional] 

## Example

```python
from caraer_client.models.update_lifecycle_properties_dto import UpdateLifecyclePropertiesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLifecyclePropertiesDTO from a JSON string
update_lifecycle_properties_dto_instance = UpdateLifecyclePropertiesDTO.from_json(json)
# print the JSON string representation of the object
print(UpdateLifecyclePropertiesDTO.to_json())

# convert the object into a dict
update_lifecycle_properties_dto_dict = update_lifecycle_properties_dto_instance.to_dict()
# create an instance of UpdateLifecyclePropertiesDTO from a dict
update_lifecycle_properties_dto_from_dict = UpdateLifecyclePropertiesDTO.from_dict(update_lifecycle_properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


