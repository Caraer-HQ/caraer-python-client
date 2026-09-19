# MapMarkerPreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_uuid** | **str** |  | [optional] 
**preview_uuid** | **str** |  | [optional] 
**preview_name** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.map_marker_preview_request import MapMarkerPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapMarkerPreviewRequest from a JSON string
map_marker_preview_request_instance = MapMarkerPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(MapMarkerPreviewRequest.to_json())

# convert the object into a dict
map_marker_preview_request_dict = map_marker_preview_request_instance.to_dict()
# create an instance of MapMarkerPreviewRequest from a dict
map_marker_preview_request_from_dict = MapMarkerPreviewRequest.from_dict(map_marker_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


