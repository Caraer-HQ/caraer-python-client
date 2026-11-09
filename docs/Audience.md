# Audience


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **object** |  | [optional] 
**principal** | **object** |  | [optional] 
**authenticated** | **bool** |  | [optional] 
**database** | **str** |  | [optional] 
**principal_database** | **str** |  | [optional] 
**company_uuid** | **str** |  | [optional] 
**principal_uuid** | **str** |  | [optional] 
**authorities** | **List[str]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from caraer_client.models.audience import Audience

# TODO update the JSON string below
json = "{}"
# create an instance of Audience from a JSON string
audience_instance = Audience.from_json(json)
# print the JSON string representation of the object
print(Audience.to_json())

# convert the object into a dict
audience_dict = audience_instance.to_dict()
# create an instance of Audience from a dict
audience_from_dict = Audience.from_dict(audience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


