# CopyPropertiesToObjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_uuids** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.copy_properties_to_object_request import CopyPropertiesToObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyPropertiesToObjectRequest from a JSON string
copy_properties_to_object_request_instance = CopyPropertiesToObjectRequest.from_json(json)
# print the JSON string representation of the object
print(CopyPropertiesToObjectRequest.to_json())

# convert the object into a dict
copy_properties_to_object_request_dict = copy_properties_to_object_request_instance.to_dict()
# create an instance of CopyPropertiesToObjectRequest from a dict
copy_properties_to_object_request_from_dict = CopyPropertiesToObjectRequest.from_dict(copy_properties_to_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


