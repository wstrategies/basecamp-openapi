# CardTableColumn


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
**parent** | [**CardTable**](CardTable.md) |  | [optional] 
**bucket** | [**Bucket**](Bucket.md) |  | [optional] 
**creator** | [**Person**](Person.md) |  | [optional] 
**description** | **str** |  | [optional] 
**subscribers** | [**List[Person]**](Person.md) |  | [optional] 
**color** | **str** |  | [optional] 
**cards_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**cards_url** | **str** |  | [optional] 

## Example

```python
from basecamp4_python_sdk.models.card_table_column import CardTableColumn

# TODO update the JSON string below
json = "{}"
# create an instance of CardTableColumn from a JSON string
card_table_column_instance = CardTableColumn.from_json(json)
# print the JSON string representation of the object
print CardTableColumn.to_json()

# convert the object into a dict
card_table_column_dict = card_table_column_instance.to_dict()
# create an instance of CardTableColumn from a dict
card_table_column_form_dict = card_table_column.from_dict(card_table_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


