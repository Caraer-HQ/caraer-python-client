# ShowResponseListFormObjectSummaryDTO

Success response (ShowResponseListFormObjectSummaryDTO).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from caraer_client.models.show_response_list_form_object_summary_dto import ShowResponseListFormObjectSummaryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ShowResponseListFormObjectSummaryDTO from a JSON string
show_response_list_form_object_summary_dto_instance = ShowResponseListFormObjectSummaryDTO.from_json(json)
# print the JSON string representation of the object
print(ShowResponseListFormObjectSummaryDTO.to_json())

# convert the object into a dict
show_response_list_form_object_summary_dto_dict = show_response_list_form_object_summary_dto_instance.to_dict()
# create an instance of ShowResponseListFormObjectSummaryDTO from a dict
show_response_list_form_object_summary_dto_from_dict = ShowResponseListFormObjectSummaryDTO.from_dict(show_response_list_form_object_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


