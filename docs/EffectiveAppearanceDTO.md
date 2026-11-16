# EffectiveAppearanceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appearance** | [**PortalAppearanceDTO**](PortalAppearanceDTO.md) |  | [optional] 
**can_manage** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.effective_appearance_dto import EffectiveAppearanceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveAppearanceDTO from a JSON string
effective_appearance_dto_instance = EffectiveAppearanceDTO.from_json(json)
# print the JSON string representation of the object
print(EffectiveAppearanceDTO.to_json())

# convert the object into a dict
effective_appearance_dto_dict = effective_appearance_dto_instance.to_dict()
# create an instance of EffectiveAppearanceDTO from a dict
effective_appearance_dto_from_dict = EffectiveAppearanceDTO.from_dict(effective_appearance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


