# ViewShareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[Record]**](Record.md) |  | [optional] 
**teams** | [**List[Record]**](Record.md) |  | [optional] 
**is_internally_public** | **bool** |  | [optional] 

## Example

```python
from caraer_client.models.view_share_request import ViewShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ViewShareRequest from a JSON string
view_share_request_instance = ViewShareRequest.from_json(json)
# print the JSON string representation of the object
print(ViewShareRequest.to_json())

# convert the object into a dict
view_share_request_dict = view_share_request_instance.to_dict()
# create an instance of ViewShareRequest from a dict
view_share_request_from_dict = ViewShareRequest.from_dict(view_share_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


