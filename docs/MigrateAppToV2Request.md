# MigrateAppToV2Request

Request to migrate an existing V1 app to platform V2 (shared container runtime)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime** | **str** | Required when functions disagree or none set: nodejs22 or python312 | [optional] 

## Example

```python
from caraer_client.models.migrate_app_to_v2_request import MigrateAppToV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateAppToV2Request from a JSON string
migrate_app_to_v2_request_instance = MigrateAppToV2Request.from_json(json)
# print the JSON string representation of the object
print(MigrateAppToV2Request.to_json())

# convert the object into a dict
migrate_app_to_v2_request_dict = migrate_app_to_v2_request_instance.to_dict()
# create an instance of MigrateAppToV2Request from a dict
migrate_app_to_v2_request_from_dict = MigrateAppToV2Request.from_dict(migrate_app_to_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


