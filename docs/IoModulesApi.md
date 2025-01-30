# mir.IoModulesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**io_modules_get**](IoModulesApi.md#io_modules_get) | **GET** /io_modules | GET /io_modules
[**io_modules_guid_delete**](IoModulesApi.md#io_modules_guid_delete) | **DELETE** /io_modules/{guid} | DELETE /io_modules/{guid}
[**io_modules_guid_get**](IoModulesApi.md#io_modules_guid_get) | **GET** /io_modules/{guid} | GET /io_modules/{guid}
[**io_modules_guid_put**](IoModulesApi.md#io_modules_guid_put) | **PUT** /io_modules/{guid} | PUT /io_modules/{guid}
[**io_modules_guid_status_delete**](IoModulesApi.md#io_modules_guid_status_delete) | **DELETE** /io_modules/{guid}/status | DELETE /io_modules/{guid}/status
[**io_modules_guid_status_get**](IoModulesApi.md#io_modules_guid_status_get) | **GET** /io_modules/{guid}/status | GET /io_modules/{guid}/status
[**io_modules_guid_status_post**](IoModulesApi.md#io_modules_guid_status_post) | **POST** /io_modules/{guid}/status | POST /io_modules/{guid}/status
[**io_modules_guid_status_put**](IoModulesApi.md#io_modules_guid_status_put) | **PUT** /io_modules/{guid}/status | PUT /io_modules/{guid}/status
[**io_modules_post**](IoModulesApi.md#io_modules_post) | **POST** /io_modules | POST /io_modules


# **io_modules_get**
> list[GetIoModules] io_modules_get(authorization, accept_language)

GET /io_modules

Retrieve the list of configured IO modules

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /io_modules
    api_response = api_instance.io_modules_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetIoModules]**](GetIoModules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_delete**
> io_modules_guid_delete(authorization, accept_language, guid)

DELETE /io_modules/{guid}

Erase the IO device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /io_modules/{guid}
    api_instance.io_modules_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_guid_delete: %s\n" % e)
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

# **io_modules_guid_get**
> GetIoModule io_modules_guid_get(authorization, accept_language, guid)

GET /io_modules/{guid}

Retrieve the details about a IO device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /io_modules/{guid}
    api_response = api_instance.io_modules_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetIoModule**](GetIoModule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_put**
> GetIoModule io_modules_guid_put(authorization, accept_language, guid, io_module)

PUT /io_modules/{guid}

Modify the values of the IO device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
io_module = mir.PutIoModule() # PutIoModule | The new values of the io_module

try:
    # PUT /io_modules/{guid}
    api_response = api_instance.io_modules_guid_put(authorization, accept_language, guid, io_module)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **io_module** | [**PutIoModule**](PutIoModule.md)| The new values of the io_module | 

### Return type

[**GetIoModule**](GetIoModule.md)

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
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /io_modules/{guid}/status
    api_instance.io_modules_guid_status_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_guid_status_delete: %s\n" % e)
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
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /io_modules/{guid}/status
    api_response = api_instance.io_modules_guid_status_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_guid_status_get: %s\n" % e)
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
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to
io_module_status = mir.PostIoModuleStatus() # PostIoModuleStatus | The details of the io_module_status

try:
    # POST /io_modules/{guid}/status
    api_response = api_instance.io_modules_guid_status_post(authorization, accept_language, guid, io_module_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_guid_status_post: %s\n" % e)
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
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
io_module_status = mir.PutIoModuleStatus() # PutIoModuleStatus | The new values of the io_module_status

try:
    # PUT /io_modules/{guid}/status
    api_response = api_instance.io_modules_guid_status_put(authorization, accept_language, guid, io_module_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_guid_status_put: %s\n" % e)
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

# **io_modules_post**
> GetIoModules io_modules_post(authorization, accept_language, io_modules)

POST /io_modules

Add a new IO module

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.IoModulesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
io_modules = mir.PostIoModules() # PostIoModules | The details of the io_modules

try:
    # POST /io_modules
    api_response = api_instance.io_modules_post(authorization, accept_language, io_modules)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IoModulesApi->io_modules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **io_modules** | [**PostIoModules**](PostIoModules.md)| The details of the io_modules | 

### Return type

[**GetIoModules**](GetIoModules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

