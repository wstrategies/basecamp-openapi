# CardTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | [optional] 
**visible_to_clients** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**inherits_status** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**app_url** | **str** |  | [optional] 
**bookmark_url** | **str** |  | [optional] 
**subscription_url** | **str** |  | [optional] 
**bucket** | [**Bucket**](Bucket.md) |  | [optional] 
**creator** | [**Person**](Person.md) |  | [optional] 
**subscribers** | [**List[Person]**](Person.md) |  | [optional] 
**lists** | [**List[CardTableColumn]**](CardTableColumn.md) |  | [optional] 

## Example

```python
from basecamp4_python_sdk.models.card_table import CardTable

# TODO update the JSON string below
json = "{}"
# create an instance of CardTable from a JSON string
card_table_instance = CardTable.from_json(json)
# print the JSON string representation of the object
print CardTable.to_json()

# convert the object into a dict
card_table_dict = card_table_instance.to_dict()
# create an instance of CardTable from a dict
card_table_form_dict = card_table.from_dict(card_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


