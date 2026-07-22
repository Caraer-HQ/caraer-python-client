# PageContentStylingDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | [**StyleSetDTO**](StyleSetDTO.md) | The style set for all devices | [optional] 
**mobile** | [**StyleSetDTO**](StyleSetDTO.md) | The style set for the mobile device | [optional] 
**tablet** | [**StyleSetDTO**](StyleSetDTO.md) | The style set for the tablet device | [optional] 
**desktop** | [**StyleSetDTO**](StyleSetDTO.md) | The style set for the desktop device | [optional] 

## Example

```python
from caraer_client.models.page_content_styling_dto import PageContentStylingDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PageContentStylingDTO from a JSON string
page_content_styling_dto_instance = PageContentStylingDTO.from_json(json)
# print the JSON string representation of the object
print(PageContentStylingDTO.to_json())

# convert the object into a dict
page_content_styling_dto_dict = page_content_styling_dto_instance.to_dict()
# create an instance of PageContentStylingDTO from a dict
page_content_styling_dto_from_dict = PageContentStylingDTO.from_dict(page_content_styling_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


