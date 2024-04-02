# basecamp4_python_sdk.DefaultApi

All URIs are relative to *https://3.basecampapi.com/9999999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorization_json_get**](DefaultApi.md#authorization_json_get) | **GET** /authorization.json | Get authorization
[**projects_json_get**](DefaultApi.md#projects_json_get) | **GET** /projects.json | Get projects


# **authorization_json_get**
> Authorization authorization_json_get()

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
        api_response = api_instance.authorization_json_get()
        print("The response of DefaultApi->authorization_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authorization_json_get: %s\n" % e)
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

# **projects_json_get**
> List[Project] projects_json_get()

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
        api_response = api_instance.projects_json_get()
        print("The response of DefaultApi->projects_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->projects_json_get: %s\n" % e)
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

