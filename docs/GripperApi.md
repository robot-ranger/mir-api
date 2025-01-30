# mir.GripperApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hook_gripper_get**](GripperApi.md#hook_gripper_get) | **GET** /hook/gripper | GET /hook/gripper
[**hook_gripper_put**](GripperApi.md#hook_gripper_put) | **PUT** /hook/gripper | PUT /hook/gripper


# **hook_gripper_get**
> GetHookGripper hook_gripper_get(authorization, accept_language)

GET /hook/gripper

Retrieve the state of the Hook gripper

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.GripperApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/gripper
    api_response = api_instance.hook_gripper_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GripperApi->hook_gripper_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHookGripper**](GetHookGripper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_gripper_put**
> GetHookGripper hook_gripper_put(authorization, accept_language, hook_gripper)

PUT /hook/gripper

Open or close the Hook gripper

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.GripperApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_gripper = mir.PutHookGripper() # PutHookGripper | The new values of the hook_gripper

try:
    # PUT /hook/gripper
    api_response = api_instance.hook_gripper_put(authorization, accept_language, hook_gripper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GripperApi->hook_gripper_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **hook_gripper** | [**PutHookGripper**](PutHookGripper.md)| The new values of the hook_gripper | 

### Return type

[**GetHookGripper**](GetHookGripper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

