# RecordSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**properties** | **Dict[str, Optional[object]]** |  | [optional] 
**parsed_properties** | **Dict[str, Optional[object]]** |  | [optional] 

## Example

```python
from caraer_client.models.record_summary import RecordSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RecordSummary from a JSON string
record_summary_instance = RecordSummary.from_json(json)
# print the JSON string representation of the object
print(RecordSummary.to_json())

# convert the object into a dict
record_summary_dict = record_summary_instance.to_dict()
# create an instance of RecordSummary from a dict
record_summary_from_dict = RecordSummary.from_dict(record_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


