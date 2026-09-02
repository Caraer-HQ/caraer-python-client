# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**action_title** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**data** | **Dict[str, Optional[object]]** |  | [optional] 
**sender** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**target_user_uuid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**read_at** | **str** |  | [optional] 
**source_app_uuid** | **str** |  | [optional] 
**app_logo** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


