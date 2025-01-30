# mir.HookInterfaceApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_hook_interface_get**](HookInterfaceApi.md#software_hook_interface_get) | **GET** /software/hook_interface | GET /software/hook_interface
[**software_hook_interface_post**](HookInterfaceApi.md#software_hook_interface_post) | **POST** /software/hook_interface | POST /software/hook_interface


# **software_hook_interface_get**
> GetHookSoftwareInterface software_hook_interface_get(authorization, accept_language)

GET /software/hook_interface

Retrieve the information about the hook software interface

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.HookInterfaceApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/hook_interface
    api_response = api_instance.software_hook_interface_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookInterfaceApi->software_hook_interface_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHookSoftwareInterface**](GetHookSoftwareInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_hook_interface_post**
> GetHookSoftwareInterface software_hook_interface_post(authorization, accept_language, hook_software_interface)

POST /software/hook_interface

Proceed with hook upgrade

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.HookInterfaceApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_software_interface = mir.PostHookSoftwareInterface() # PostHookSoftwareInterface | The details of the hook_software_interface

try:
    # POST /software/hook_interface
    api_response = api_instance.software_hook_interface_post(authorization, accept_language, hook_software_interface)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookInterfaceApi->software_hook_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **hook_software_interface** | [**PostHookSoftwareInterface**](PostHookSoftwareInterface.md)| The details of the hook_software_interface | 

### Return type

[**GetHookSoftwareInterface**](GetHookSoftwareInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

