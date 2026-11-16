# PortalAppearanceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.portal_appearance_dto import PortalAppearanceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PortalAppearanceDTO from a JSON string
portal_appearance_dto_instance = PortalAppearanceDTO.from_json(json)
# print the JSON string representation of the object
print(PortalAppearanceDTO.to_json())

# convert the object into a dict
portal_appearance_dto_dict = portal_appearance_dto_instance.to_dict()
# create an instance of PortalAppearanceDTO from a dict
portal_appearance_dto_from_dict = PortalAppearanceDTO.from_dict(portal_appearance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


