# CardCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the card. | 
**content** | **str** | Content containing information about the card. See Basecamp Rich text guide for what HTML tags are allowed. | [optional] 
**due_on** | **date** | Due date (ISO 8601) of the card. | [optional] 
**notify** | **bool** | Whether to notify assignees, value true or false. Defaults to false. | [optional] [default to False]

## Example

```python
from basecamp4_python_sdk.models.card_create_request import CardCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CardCreateRequest from a JSON string
card_create_request_instance = CardCreateRequest.from_json(json)
# print the JSON string representation of the object
print CardCreateRequest.to_json()

# convert the object into a dict
card_create_request_dict = card_create_request_instance.to_dict()
# create an instance of CardCreateRequest from a dict
card_create_request_form_dict = card_create_request.from_dict(card_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


