# PropertyOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**completed** | **bool** |  | [optional] 
**used_in** | [**UsedInResult**](UsedInResult.md) |  | [optional] 

## Example

```python
from caraer_client.models.property_option import PropertyOption

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyOption from a JSON string
property_option_instance = PropertyOption.from_json(json)
# print the JSON string representation of the object
print(PropertyOption.to_json())

# convert the object into a dict
property_option_dict = property_option_instance.to_dict()
# create an instance of PropertyOption from a dict
property_option_from_dict = PropertyOption.from_dict(property_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


