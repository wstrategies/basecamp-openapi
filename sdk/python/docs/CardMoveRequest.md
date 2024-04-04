# CardMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | **int** | The column ID of the destination column. | 

## Example

```python
from basecamp4_python_sdk.models.card_move_request import CardMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CardMoveRequest from a JSON string
card_move_request_instance = CardMoveRequest.from_json(json)
# print the JSON string representation of the object
print CardMoveRequest.to_json()

# convert the object into a dict
card_move_request_dict = card_move_request_instance.to_dict()
# create an instance of CardMoveRequest from a dict
card_move_request_form_dict = card_move_request.from_dict(card_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


