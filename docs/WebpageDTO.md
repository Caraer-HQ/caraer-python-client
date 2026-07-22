# WebpageDTO

Data transfer object representing a webpage with its various states, properties, and associated form/versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The environment of the webpage. | [optional] 
**uuid** | **str** | The UUID of the webpage. | [optional] 
**title** | **str** | The title of the webpage. | [optional] 
**excerpt** | **str** | Short summary or excerpt displayed for the webpage. | [optional] 
**slug** | **str** | URL-friendly identifier for the webpage. | [optional] 
**image** | **str** | URL or identifier of the image associated with the webpage. | [optional] 
**custom_css** | **str** | Custom CSS for the webpage. | [optional] 
**custom_js_head** | **str** | Custom JS for the webpage. | [optional] 
**custom_js_body** | **str** | Custom JS for the webpage. | [optional] 
**content** | [**PageContentDTO**](PageContentDTO.md) | Content of the webpage | [optional] 
**sidebar** | [**PreviewDTO**](PreviewDTO.md) | Preview of the sidebar | [optional] 
**sidebar_relation** | [**RelationDTO**](RelationDTO.md) | Relation of the sidebar | [optional] 
**sidebar_object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | Object of the sidebar | [optional] 
**object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | The Object object associated with the webpage, representing application data. | [optional] 
**record** | [**WebpagePublicRecordDTO**](WebpagePublicRecordDTO.md) | Webpage-public backing record values (internal + parsed). Set only on public page responses. | [optional] 
**options** | [**WebpageOptionsDTO**](WebpageOptionsDTO.md) | Custom options and configurations specific to the webpage. | [optional] 
**meta_data** | **Dict[str, Optional[object]]** | Map of additional metadata and attributes for the webpage. | [optional] 
**published_by** | **str** | Identifier of the user or process that published the webpage | [optional] 
**published_at** | **int** | Timestamp representing when the webpage was published | [optional] 
**unpublished_by** | **str** | Identifier of the user or process that unpublished the webpage | [optional] 
**unpublished_at** | **int** | Timestamp representing when the webpage was unpublished | [optional] 
**publish_at** | **int** | Scheduled timestamp for when the webpage will be published | [optional] 
**unpublish_at** | **int** | Scheduled timestamp for when the webpage will be unpublished | [optional] 
**is_published** | **bool** | Flag indicating whether the webpage is currently published | [optional] [default to False]
**live_url** | **str** | Fully qualified public URL of the webpage, including the page trait root slug. | [optional] 

## Example

```python
from caraer_client.models.webpage_dto import WebpageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageDTO from a JSON string
webpage_dto_instance = WebpageDTO.from_json(json)
# print the JSON string representation of the object
print(WebpageDTO.to_json())

# convert the object into a dict
webpage_dto_dict = webpage_dto_instance.to_dict()
# create an instance of WebpageDTO from a dict
webpage_dto_from_dict = WebpageDTO.from_dict(webpage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


