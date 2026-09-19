# ShowResponseCmsEnvironmentDTO

Represents the response for viewing or showing a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message detailing the result of the operation. | [optional] 
**data** | [**CmsEnvironmentDTO**](CmsEnvironmentDTO.md) | The data payload of the response, if any. | [optional] 

## Example

```python
from caraer_client.models.show_response_cms_environment_dto import ShowResponseCmsEnvironmentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseCmsEnvironmentDTO from a JSON string
show_response_cms_environment_dto_instance = ShowResponseCmsEnvironmentDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseCmsEnvironmentDTO.to_json())

# convert the object into a dict
show_response_cms_environment_dto_dict = show_response_cms_environment_dto_instance.to_dict()
# create an instance of ShowResponseCmsEnvironmentDTO from a dict
show_response_cms_environment_dto_from_dict = ShowResponseCmsEnvironmentDTO.from_dict(show_response_cms_environment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


