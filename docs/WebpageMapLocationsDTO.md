# WebpageMapLocationsDTO

Resolved public map markers for a webpage map block

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_locations** | [**List[MapLocationDTO]**](MapLocationDTO.md) | Concrete markers after applying public filters | [optional] 

## Example

```python
from caraer_client.models.webpage_map_locations_dto import WebpageMapLocationsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageMapLocationsDTO from a JSON string
webpage_map_locations_dto_instance = WebpageMapLocationsDTO.from_json(json)
# print the JSON string representation of the object
print(WebpageMapLocationsDTO.to_json())

# convert the object into a dict
webpage_map_locations_dto_dict = webpage_map_locations_dto_instance.to_dict()
# create an instance of WebpageMapLocationsDTO from a dict
webpage_map_locations_dto_from_dict = WebpageMapLocationsDTO.from_dict(webpage_map_locations_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


