# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**attachable_sgid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**personable_type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**admin** | **bool** |  | [optional] 
**owner** | **bool** |  | [optional] 
**client** | **bool** |  | [optional] 
**employee** | **bool** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**can_manage_projects** | **bool** |  | [optional] 
**can_manage_people** | **bool** |  | [optional] 

## Example

```python
from basecamp4_python_sdk.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print Person.to_json()

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_form_dict = person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


