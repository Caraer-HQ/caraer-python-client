# WebpageAccessGrantDTO

Signed URL access grant for a protected webpage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the entity | 
**name** | **str** | The name of the entity | 
**label** | **str** | Display label for the entity, can be different from name | [optional] 
**created_at** | **int** | Unix timestamp when the entity was created | [optional] 
**created_by** | [**Record**](Record.md) | Identifier of the user who created the entity | [optional] 
**updated_at** | **int** | Unix timestamp when the entity was last updated | [optional] 
**updated_by** | [**Record**](Record.md) | Identifier of the user who last updated the entity | [optional] 
**deleted_at** | **int** | Unix timestamp when the entity was deleted (null if not deleted) | [optional] 
**deleted_by** | [**Record**](Record.md) | Identifier of the user who deleted the entity | [optional] 
**index** | **int** | Index number for ordering entities | [optional] 
**record_uuid** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**revoked_at** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 
**token_hash** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from caraer_client.models.webpage_access_grant_dto import WebpageAccessGrantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageAccessGrantDTO from a JSON string
webpage_access_grant_dto_instance = WebpageAccessGrantDTO.from_json(json)
# print the JSON string representation of the object
print(WebpageAccessGrantDTO.to_json())

# convert the object into a dict
webpage_access_grant_dto_dict = webpage_access_grant_dto_instance.to_dict()
# create an instance of WebpageAccessGrantDTO from a dict
webpage_access_grant_dto_from_dict = WebpageAccessGrantDTO.from_dict(webpage_access_grant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


