# MapLocationDTO

A map marker from one source: custom lat/lng, a page location property, or an object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**property_uuid** | **str** | UUID of a location property | [optional] 
**property_name** | **str** | Name of a location property (fallback if uuid missing) | [optional] 
**object_uuid** | **str** | When set, resolve markers from published records of this object. Exclusive with propertyUuid and custom lat/lng. | [optional] 
**object_name** | **str** | Object name fallback when uuid is missing | [optional] 
**icon** | **str** | FontAwesome icon key for the marker | [optional] 
**icon_color** | **str** | Marker icon color (hex or rgba) | [optional] 
**icon_background_color** | **str** | Marker pin background fill color (hex or rgba) | [optional] 
**marker_size** | **float** | Marker pin size in CSS pixels | [optional] 
**icon_size** | **float** | Marker glyph size in CSS pixels | [optional] 
**label** | **str** | Text shown when hovering the marker (supports smart content) | [optional] 
**label_property_uuid** | **str** | UUID of a property whose value is shown as hover text | [optional] 
**label_property_name** | **str** | Name of a property whose value is shown as hover text | [optional] 
**hover_preview_uuid** | **str** | UUID of the preview shown when hovering a bound marker | [optional] 
**hover_preview_name** | **str** | Name of the preview shown when hovering a bound marker | [optional] 
**record_uuid** | **str** | Record this concrete public marker was resolved from | [optional] 
**click_link_type** | **str** | Marker click target: liveUrl, custom, or unset | [optional] 
**click_link_url** | **str** | Custom URL used when clickLinkType is custom | [optional] 
**click_link_open_in_new_window** | **bool** | Open the marker link in a new tab | [optional] 
**href** | **str** | Resolved public URL for this concrete marker | [optional] 
**filter_properties** | [**List[PropertyDTO]**](PropertyDTO.md) | Properties exposed as public filters for object-bound markers | [optional] 
**filter_values** | **Dict[str, Optional[object]]** | Resolved property values used to filter this concrete marker | [optional] 

## Example

```python
from caraer_client.models.map_location_dto import MapLocationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MapLocationDTO from a JSON string
map_location_dto_instance = MapLocationDTO.from_json(json)
# print the JSON string representation of the object
print(MapLocationDTO.to_json())

# convert the object into a dict
map_location_dto_dict = map_location_dto_instance.to_dict()
# create an instance of MapLocationDTO from a dict
map_location_dto_from_dict = MapLocationDTO.from_dict(map_location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


