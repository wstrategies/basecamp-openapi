# DockItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the dock item | 
**title** | **str** | Display title of the dock item | 
**name** | **str** | System name of the dock item | 
**enabled** | **bool** | Indicates if the dock item is enabled | 
**position** | **int** | Position of the dock item in the UI, null if not applicable | [optional] 
**url** | **str** | API URL for the dock item | 
**app_url** | **str** | Web application URL for the dock item | 

## Example

```python
from basecamp4_python_sdk.models.dock_item import DockItem

# TODO update the JSON string below
json = "{}"
# create an instance of DockItem from a JSON string
dock_item_instance = DockItem.from_json(json)
# print the JSON string representation of the object
print DockItem.to_json()

# convert the object into a dict
dock_item_dict = dock_item_instance.to_dict()
# create an instance of DockItem from a dict
dock_item_form_dict = dock_item.from_dict(dock_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


