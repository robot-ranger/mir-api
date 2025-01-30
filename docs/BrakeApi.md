# mir.BrakeApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hook_brake_get**](BrakeApi.md#hook_brake_get) | **GET** /hook/brake | GET /hook/brake
[**hook_brake_put**](BrakeApi.md#hook_brake_put) | **PUT** /hook/brake | PUT /hook/brake


# **hook_brake_get**
> GetHookBrake hook_brake_get(authorization, accept_language)

GET /hook/brake

Retrieve the state of the Hook brake

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.BrakeApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/brake
    api_response = api_instance.hook_brake_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrakeApi->hook_brake_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHookBrake**](GetHookBrake.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_brake_put**
> GetHookBrake hook_brake_put(authorization, accept_language, hook_brake)

PUT /hook/brake

Activate or release the Hook brake

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.BrakeApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_brake = mir.PutHookBrake() # PutHookBrake | The new values of the hook_brake

try:
    # PUT /hook/brake
    api_response = api_instance.hook_brake_put(authorization, accept_language, hook_brake)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrakeApi->hook_brake_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **hook_brake** | [**PutHookBrake**](PutHookBrake.md)| The new values of the hook_brake | 

### Return type

[**GetHookBrake**](GetHookBrake.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

