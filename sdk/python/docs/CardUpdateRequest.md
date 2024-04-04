# CardUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the card. | [optional] 
**content** | **str** | Content containing information about the card. See Basecamp Rich text guide for what HTML tags are allowed. | [optional] 
**due_on** | **date** | Due date (ISO 8601) of the card. | [optional] 
**assignee_ids** | **List[int]** | An array of people that will be assigned to this card. Please see the Get people endpoints to retrieve them. | [optional] 

## Example

```python
from basecamp4_python_sdk.models.card_update_request import CardUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CardUpdateRequest from a JSON string
card_update_request_instance = CardUpdateRequest.from_json(json)
# print the JSON string representation of the object
print CardUpdateRequest.to_json()

# convert the object into a dict
card_update_request_dict = card_update_request_instance.to_dict()
# create an instance of CardUpdateRequest from a dict
card_update_request_form_dict = card_update_request.from_dict(card_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


