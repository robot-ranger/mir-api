# mir.StatusApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hook_status_get**](StatusApi.md#hook_status_get) | **GET** /hook/status | GET /hook/status
[**io_modules_guid_status_delete**](StatusApi.md#io_modules_guid_status_delete) | **DELETE** /io_modules/{guid}/status | DELETE /io_modules/{guid}/status
[**io_modules_guid_status_get**](StatusApi.md#io_modules_guid_status_get) | **GET** /io_modules/{guid}/status | GET /io_modules/{guid}/status
[**io_modules_guid_status_post**](StatusApi.md#io_modules_guid_status_post) | **POST** /io_modules/{guid}/status | POST /io_modules/{guid}/status
[**io_modules_guid_status_put**](StatusApi.md#io_modules_guid_status_put) | **PUT** /io_modules/{guid}/status | PUT /io_modules/{guid}/status
[**status_get**](StatusApi.md#status_get) | **GET** /status | GET /status
[**status_put**](StatusApi.md#status_put) | **PUT** /status | PUT /status


# **hook_status_get**
> GetHook hook_status_get(authorization, accept_language)

GET /hook/status

Retrieve the extended status of the Hook

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/status
    api_response = api_instance.hook_status_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->hook_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHook**](GetHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_delete**
> io_modules_guid_status_delete(authorization, accept_language, guid)

DELETE /io_modules/{guid}/status

Disconnect from the IO module with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /io_modules/{guid}/status
    api_instance.io_modules_guid_status_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling StatusApi->io_modules_guid_status_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_get**
> GetIoModuleStatus io_modules_guid_status_get(authorization, accept_language, guid)

GET /io_modules/{guid}/status

Retrieve the status of the connection to the IO module with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /io_modules/{guid}/status
    api_response = api_instance.io_modules_guid_status_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->io_modules_guid_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetIoModuleStatus**](GetIoModuleStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_post**
> GetIoModuleStatus io_modules_guid_status_post(authorization, accept_language, guid, io_module_status)

POST /io_modules/{guid}/status

Connect to theIO module with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to
io_module_status = mir.PostIoModuleStatus() # PostIoModuleStatus | The details of the io_module_status

try:
    # POST /io_modules/{guid}/status
    api_response = api_instance.io_modules_guid_status_post(authorization, accept_language, guid, io_module_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->io_modules_guid_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to add the new resource to | 
 **io_module_status** | [**PostIoModuleStatus**](PostIoModuleStatus.md)| The details of the io_module_status | 

### Return type

[**GetIoModuleStatus**](GetIoModuleStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_put**
> GetIoModuleStatus io_modules_guid_status_put(authorization, accept_language, guid, io_module_status)

PUT /io_modules/{guid}/status

Modify the outputs of the connected IO module with specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
io_module_status = mir.PutIoModuleStatus() # PutIoModuleStatus | The new values of the io_module_status

try:
    # PUT /io_modules/{guid}/status
    api_response = api_instance.io_modules_guid_status_put(authorization, accept_language, guid, io_module_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->io_modules_guid_status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **io_module_status** | [**PutIoModuleStatus**](PutIoModuleStatus.md)| The new values of the io_module_status | 

### Return type

[**GetIoModuleStatus**](GetIoModuleStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> GetStatus status_get(authorization, accept_language)

GET /status

Retrieve the status

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /status
    api_response = api_instance.status_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetStatus**](GetStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_put**
> GetStatus status_put(authorization, accept_language, status)

PUT /status

Modify the status

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
status = mir.PutStatus() # PutStatus | The new values of the status

try:
    # PUT /status
    api_response = api_instance.status_put(authorization, accept_language, status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **status** | [**PutStatus**](PutStatus.md)| The new values of the status | 

### Return type

[**GetStatus**](GetStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

