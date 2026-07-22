# CopyPropertyToEnvironmentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_uuid** | **str** |  | [optional] 
**property_uuid** | **str** |  | [optional] 
**property_uuids** | **List[str]** |  | [optional] 
**environments** | **List[str]** |  | [optional] 
**fill_copied_values** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.copy_property_to_environments_request import CopyPropertyToEnvironmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyPropertyToEnvironmentsRequest from a JSON string
copy_property_to_environments_request_instance = CopyPropertyToEnvironmentsRequest.from_json(json)
# print the JSON string representation of the object
print(CopyPropertyToEnvironmentsRequest.to_json())

# convert the object into a dict
copy_property_to_environments_request_dict = copy_property_to_environments_request_instance.to_dict()
# create an instance of CopyPropertyToEnvironmentsRequest from a dict
copy_property_to_environments_request_from_dict = CopyPropertyToEnvironmentsRequest.from_dict(copy_property_to_environments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


