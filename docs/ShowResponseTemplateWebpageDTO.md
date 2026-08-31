# ShowResponseTemplateWebpageDTO

Success response (ShowResponseTemplateWebpageDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_template_webpage_dto import ShowResponseTemplateWebpageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseTemplateWebpageDTO from a JSON string
show_response_template_webpage_dto_instance = ShowResponseTemplateWebpageDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseTemplateWebpageDTO.to_json())

# convert the object into a dict
show_response_template_webpage_dto_dict = show_response_template_webpage_dto_instance.to_dict()
# create an instance of ShowResponseTemplateWebpageDTO from a dict
show_response_template_webpage_dto_from_dict = ShowResponseTemplateWebpageDTO.from_dict(show_response_template_webpage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


