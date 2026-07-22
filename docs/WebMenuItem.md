# WebMenuItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**image** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.web_menu_item import WebMenuItem

# TODO update the JSON string below
json = "{}"
# create an instance of WebMenuItem from a JSON string
web_menu_item_instance = WebMenuItem.from_json(json)
# print the JSON string representation of the object
print(WebMenuItem.to_json())

# convert the object into a dict
web_menu_item_dict = web_menu_item_instance.to_dict()
# create an instance of WebMenuItem from a dict
web_menu_item_from_dict = WebMenuItem.from_dict(web_menu_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


