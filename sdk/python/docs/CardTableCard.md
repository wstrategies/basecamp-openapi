# CardTableCard


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
**comments_count** | **int** |  | [optional] 
**comments_url** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**parent** | [**CardTableColumn**](CardTableColumn.md) |  | [optional] 
**bucket** | [**Bucket**](Bucket.md) |  | [optional] 
**creator** | [**Person**](Person.md) |  | [optional] 
**description** | **str** |  | [optional] 
**completed** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 
**due_on** | **date** |  | [optional] 
**assignees** | [**List[Person]**](Person.md) |  | [optional] 
**completion_subscribers** | [**List[Person]**](Person.md) |  | [optional] 
**completion_url** | **str** |  | [optional] 
**comment_count** | **int** |  | [optional] 

## Example

```python
from basecamp4_python_sdk.models.card_table_card import CardTableCard

# TODO update the JSON string below
json = "{}"
# create an instance of CardTableCard from a JSON string
card_table_card_instance = CardTableCard.from_json(json)
# print the JSON string representation of the object
print CardTableCard.to_json()

# convert the object into a dict
card_table_card_dict = card_table_card_instance.to_dict()
# create an instance of CardTableCard from a dict
card_table_card_form_dict = card_table_card.from_dict(card_table_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


