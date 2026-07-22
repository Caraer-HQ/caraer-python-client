# PageContentSettingsDTO

Data transfer object representing the settings for a content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form** | [**FormDTO**](FormDTO.md) | The form associated with the content | [optional] 
**open_icon** | **str** | The icon to display when the accordion is open | [optional] 
**close_icon** | **str** | The icon to display when the accordion is closed | [optional] 
**alt** | **str** | The alt text of the image | [optional] 
**key** | **str** | The key of the image | [optional] 
**play_video** | **bool** | Whether the video should play automatically | [optional] 
**start_muted** | **bool** | Whether the image should start muted | [optional] 
**loop_video** | **bool** | Whether the video should loop | [optional] 
**start_offset** | **int** | The start offset of the video | [optional] 
**link** | **str** | The link of the button | [optional] 
**style** | **str** | The style of the button. Primary, secondary, tertiary or custom | [optional] 
**cta_id** | **str** | Optional CTA tracking identifier for CMS buttons | [optional] 
**open_in_new_window** | **bool** | Whether the link should open in a new window | [optional] 
**slider_type** | **str** | The slider type. Dots, arrows and swipe | [optional] 
**carousel_speed** | **float** | The carousel speed. | [optional] 
**enable_controls** | **bool** | Whether carousel prev/next controls are shown | [optional] 
**preview_object** | [**CaraerObjectDTO**](CaraerObjectDTO.md) | The object of the previews | [optional] 
**previews** | [**Dict[str, PreviewDTO]**](PreviewDTO.md) | The previews associated with the layouts | [optional] 
**preview_layout_order** | **List[str]** | The order of preview layouts | [optional] 
**filter** | [**Filter**](Filter.md) | The filter associated with the settings | [optional] 
**order_by** | [**PropertyDTO**](PropertyDTO.md) | The order by property associated with the settings | [optional] 
**order_by_direction** | **str** | The order by direction associated with the settings. ASC or DESC, default is ASC | [optional] 
**as_webpages** | **bool** | Whether the previews should be shown as webpages | [optional] 
**loop** | **bool** | Whether the previews should loop | [optional] 
**limit** | **int** | The limit associated with the settings | [optional] 
**group_by** | [**PropertyDTO**](PropertyDTO.md) | The group by property associated with the settings | [optional] 
**hide_on_no_results** | **bool** | Whether the previews should be hidden when there are no results | [optional] 
**filter_type** | **str** | The type of the filter block. left_bar or top_search | [optional] 
**search_result_single_string** | **str** | The single result string of the filter block | [optional] 
**search_result_plural_string** | **str** | The Plural result string of the filter block | [optional] 
**no_results_string** | **str** | The no results string of the filter block | [optional] 
**search_field_enabled** | **bool** | Whether the search field should be enabled | [optional] 
**search_field_placeholder** | **str** | The placeholder of the search field | [optional] 
**filter_block_enabled** | **bool** | Whether the filter block should be enabled | [optional] 
**filter_title** | **str** | The title of the filter block | [optional] 
**filter_subtitle** | **str** | The subtitle of the filter block | [optional] 
**filter_properties** | [**List[PropertyDTO]**](PropertyDTO.md) | The properties of the filter block | [optional] 
**enable_filter_tiles** | **bool** | Whether the filter tiles should be enabled | [optional] 
**enable_filter_query** | **bool** | Whether the filter query should be enabled | [optional] 
**enable_remove_all_filters_button** | **bool** | Whether the remove all filters button should be enabled | [optional] 
**cta_enabled** | **bool** | Whether the CTA should be enabled | [optional] 
**cta_title** | **str** | The title of the CTA | [optional] 
**cta_text** | **str** | The text of the CTA | [optional] 
**cta_button_text** | **str** | The button text of the CTA | [optional] 
**cta_button_link** | **str** | The button link of the CTA | [optional] 
**platforms** | **List[str]** | The platforms shown in the share component | [optional] 

## Example

```python
from caraer_client.models.page_content_settings_dto import PageContentSettingsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PageContentSettingsDTO from a JSON string
page_content_settings_dto_instance = PageContentSettingsDTO.from_json(json)
# print the JSON string representation of the object
print(PageContentSettingsDTO.to_json())

# convert the object into a dict
page_content_settings_dto_dict = page_content_settings_dto_instance.to_dict()
# create an instance of PageContentSettingsDTO from a dict
page_content_settings_dto_from_dict = PageContentSettingsDTO.from_dict(page_content_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


