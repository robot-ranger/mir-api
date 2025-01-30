# mir.ImportApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hw_import_post**](ImportApi.md#hw_import_post) | **POST** /hw/import | POST /hw/import
[**sessions_import_delete**](ImportApi.md#sessions_import_delete) | **DELETE** /sessions/import | DELETE /sessions/import
[**sessions_import_get**](ImportApi.md#sessions_import_get) | **GET** /sessions/import | GET /sessions/import
[**sessions_import_post**](ImportApi.md#sessions_import_post) | **POST** /sessions/import | POST /sessions/import


# **hw_import_post**
> GetHwConfigImport hw_import_post(authorization, accept_language, hw_config_import)

POST /hw/import

Import the hardware configuration contained in the file into the robot

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ImportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hw_config_import = mir.PostHwConfigImport() # PostHwConfigImport | The details of the hw_config_import

try:
    # POST /hw/import
    api_response = api_instance.hw_import_post(authorization, accept_language, hw_config_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->hw_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **hw_config_import** | [**PostHwConfigImport**](PostHwConfigImport.md)| The details of the hw_config_import | 

### Return type

[**GetHwConfigImport**](GetHwConfigImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_delete**
> sessions_import_delete(authorization, accept_language)

DELETE /sessions/import

Cancel currently running import

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ImportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # DELETE /sessions/import
    api_instance.sessions_import_delete(authorization, accept_language)
except ApiException as e:
    print("Exception when calling ImportApi->sessions_import_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_get**
> GetSessionImport sessions_import_get(authorization, accept_language)

GET /sessions/import

Get progress of the running import

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ImportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /sessions/import
    api_response = api_instance.sessions_import_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->sessions_import_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSessionImport**](GetSessionImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_post**
> GetSessionImport sessions_import_post(authorization, accept_language, session_import)

POST /sessions/import

Import the session contained in the file

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ImportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_import = mir.PostSessionImport() # PostSessionImport | The details of the session_import

try:
    # POST /sessions/import
    api_response = api_instance.sessions_import_post(authorization, accept_language, session_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->sessions_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **session_import** | [**PostSessionImport**](PostSessionImport.md)| The details of the session_import | 

### Return type

[**GetSessionImport**](GetSessionImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

