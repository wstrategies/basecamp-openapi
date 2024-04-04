# basecamp4_python_sdk.DefaultApi

All URIs are relative to *https://3.basecampapi.com/9999999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_card_table_card**](DefaultApi.md#create_card_table_card) | **POST** /buckets/{project_id}/card_tables/lists/{column_id}/cards.json | Create a card
[**get_authorization**](DefaultApi.md#get_authorization) | **GET** /authorization.json | Get authorization
[**get_card_table**](DefaultApi.md#get_card_table) | **GET** /buckets/{project_id}/card_tables/{card_table_id}.json | Get card table
[**get_card_table_cards**](DefaultApi.md#get_card_table_cards) | **GET** /buckets/{project_id}/card_tables/lists/{column_id}/cards.json | Get card table cards
[**get_card_table_column**](DefaultApi.md#get_card_table_column) | **GET** /buckets/{project_id}/card_tables/columns/{column_id}.json | Get card table column
[**get_projects**](DefaultApi.md#get_projects) | **GET** /projects.json | Get projects
[**move_card_table_card**](DefaultApi.md#move_card_table_card) | **POST** /buckets/{project_id}/card_tables/cards/{card_id}/moves.json | Move a card
[**update_card_table_card**](DefaultApi.md#update_card_table_card) | **PUT** /buckets/{project_id}/card_tables/cards/{card_id}.json | Update a card


# **create_card_table_card**
> CardTableCard create_card_table_card(project_id, column_id, card_create_request)

Create a card

Creates a new card in the specified card table.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.card_create_request import CardCreateRequest
from basecamp4_python_sdk.models.card_table_card import CardTableCard
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)
    project_id = 56 # int | The project ID.
    column_id = 56 # int | The column ID.
    card_create_request = basecamp4_python_sdk.CardCreateRequest() # CardCreateRequest | 

    try:
        # Create a card
        api_response = api_instance.create_card_table_card(project_id, column_id, card_create_request)
        print("The response of DefaultApi->create_card_table_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_card_table_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID. | 
 **column_id** | **int**| The column ID. | 
 **card_create_request** | [**CardCreateRequest**](CardCreateRequest.md)|  | 

### Return type

[**CardTableCard**](CardTableCard.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization**
> Authorization get_authorization()

Get authorization

Get the authorization for the Basecamp4 API

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.authorization import Authorization
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)

    try:
        # Get authorization
        api_response = api_instance.get_authorization()
        print("The response of DefaultApi->get_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_authorization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Authorization**](Authorization.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_table**
> CardTable get_card_table(project_id, card_table_id)

Get card table

Get the card table for the Basecamp4 API

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.card_table import CardTable
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)
    project_id = 56 # int | The project ID
    card_table_id = 56 # int | The card table ID

    try:
        # Get card table
        api_response = api_instance.get_card_table(project_id, card_table_id)
        print("The response of DefaultApi->get_card_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_card_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **card_table_id** | **int**| The card table ID | 

### Return type

[**CardTable**](CardTable.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_table_cards**
> List[CardTableCard] get_card_table_cards(project_id, column_id)

Get card table cards

Get the card table cards for the Basecamp4 API

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.card_table_card import CardTableCard
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)
    project_id = 56 # int | The project ID
    column_id = 56 # int | The card table column ID

    try:
        # Get card table cards
        api_response = api_instance.get_card_table_cards(project_id, column_id)
        print("The response of DefaultApi->get_card_table_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_card_table_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **column_id** | **int**| The card table column ID | 

### Return type

[**List[CardTableCard]**](CardTableCard.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_table_column**
> CardTableColumn get_card_table_column(project_id, column_id)

Get card table column

Get the card table column for the Basecamp4 API

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.card_table_column import CardTableColumn
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)
    project_id = 56 # int | The project ID
    column_id = 56 # int | The card table column ID

    try:
        # Get card table column
        api_response = api_instance.get_card_table_column(project_id, column_id)
        print("The response of DefaultApi->get_card_table_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_card_table_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **column_id** | **int**| The card table column ID | 

### Return type

[**CardTableColumn**](CardTableColumn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> List[Project] get_projects()

Get projects

Get the projects for the Basecamp4 API

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.project import Project
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)

    try:
        # Get projects
        api_response = api_instance.get_projects()
        print("The response of DefaultApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Project]**](Project.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_card_table_card**
> move_card_table_card(project_id, card_id, card_move_request)

Move a card

Allows moving of a card to a different column within the same card table.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.card_move_request import CardMoveRequest
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)
    project_id = 56 # int | The project ID.
    card_id = 56 # int | The card ID to move.
    card_move_request = basecamp4_python_sdk.CardMoveRequest() # CardMoveRequest | 

    try:
        # Move a card
        api_instance.move_card_table_card(project_id, card_id, card_move_request)
    except Exception as e:
        print("Exception when calling DefaultApi->move_card_table_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID. | 
 **card_id** | **int**| The card ID to move. | 
 **card_move_request** | [**CardMoveRequest**](CardMoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_card_table_card**
> CardTableCard update_card_table_card(project_id, card_id, card_update_request=card_update_request)

Update a card

Allows changing of the card with a specified ID in the project with a specified ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import os
import basecamp4_python_sdk
from basecamp4_python_sdk.models.card_table_card import CardTableCard
from basecamp4_python_sdk.models.card_update_request import CardUpdateRequest
from basecamp4_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://3.basecampapi.com/9999999
# See configuration.py for a list of all supported configuration parameters.
configuration = basecamp4_python_sdk.Configuration(
    host = "https://3.basecampapi.com/9999999"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = basecamp4_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with basecamp4_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = basecamp4_python_sdk.DefaultApi(api_client)
    project_id = 56 # int | The project ID.
    card_id = 56 # int | The card ID.
    card_update_request = basecamp4_python_sdk.CardUpdateRequest() # CardUpdateRequest |  (optional)

    try:
        # Update a card
        api_response = api_instance.update_card_table_card(project_id, card_id, card_update_request=card_update_request)
        print("The response of DefaultApi->update_card_table_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_card_table_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID. | 
 **card_id** | **int**| The card ID. | 
 **card_update_request** | [**CardUpdateRequest**](CardUpdateRequest.md)|  | [optional] 

### Return type

[**CardTableCard**](CardTableCard.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

