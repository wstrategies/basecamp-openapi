# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project | 
**status** | **str** | Current status of the project | [optional] 
**created_at** | **datetime** | Timestamp of project creation | [optional] 
**updated_at** | **datetime** | Timestamp of last project update | [optional] 
**name** | **str** | Name of the project | [optional] 
**description** | **str** | Detailed description of the project | [optional] 
**purpose** | **str** | Purpose of the project | [optional] 
**clients_enabled** | **bool** | Indicates if clients are enabled for the project | [optional] 
**bookmark_url** | **str** | URL for bookmarking the project | [optional] 
**url** | **str** | API URL for the project | [optional] 
**app_url** | **str** | Web application URL for the project | [optional] 
**dock** | [**List[DockItem]**](DockItem.md) | Collection of dock items associated with the project | [optional] 
**bookmarked** | **bool** | Indicates if the project is bookmarked | [optional] 

## Example

```python
from basecamp4_python_sdk.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


