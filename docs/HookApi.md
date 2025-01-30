# mir.HookApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hook_brake_get**](HookApi.md#hook_brake_get) | **GET** /hook/brake | GET /hook/brake
[**hook_brake_put**](HookApi.md#hook_brake_put) | **PUT** /hook/brake | PUT /hook/brake
[**hook_gripper_get**](HookApi.md#hook_gripper_get) | **GET** /hook/gripper | GET /hook/gripper
[**hook_gripper_put**](HookApi.md#hook_gripper_put) | **PUT** /hook/gripper | PUT /hook/gripper
[**hook_height_get**](HookApi.md#hook_height_get) | **GET** /hook/height | GET /hook/height
[**hook_height_put**](HookApi.md#hook_height_put) | **PUT** /hook/height | PUT /hook/height
[**hook_status_get**](HookApi.md#hook_status_get) | **GET** /hook/status | GET /hook/status


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
api_instance = mir.HookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/brake
    api_response = api_instance.hook_brake_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->hook_brake_get: %s\n" % e)
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
api_instance = mir.HookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_brake = mir.PutHookBrake() # PutHookBrake | The new values of the hook_brake

try:
    # PUT /hook/brake
    api_response = api_instance.hook_brake_put(authorization, accept_language, hook_brake)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->hook_brake_put: %s\n" % e)
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
api_instance = mir.HookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/gripper
    api_response = api_instance.hook_gripper_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->hook_gripper_get: %s\n" % e)
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
api_instance = mir.HookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_gripper = mir.PutHookGripper() # PutHookGripper | The new values of the hook_gripper

try:
    # PUT /hook/gripper
    api_response = api_instance.hook_gripper_put(authorization, accept_language, hook_gripper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->hook_gripper_put: %s\n" % e)
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

# **hook_height_get**
> GetHookHeight hook_height_get(authorization, accept_language)

GET /hook/height

Retrieve the height of the Hook

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.HookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/height
    api_response = api_instance.hook_height_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->hook_height_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHookHeight**](GetHookHeight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_height_put**
> GetHookHeight hook_height_put(authorization, accept_language, hook_height)

PUT /hook/height

Modify the height of the Hook

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.HookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_height = mir.PutHookHeight() # PutHookHeight | The new values of the hook_height

try:
    # PUT /hook/height
    api_response = api_instance.hook_height_put(authorization, accept_language, hook_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->hook_height_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **hook_height** | [**PutHookHeight**](PutHookHeight.md)| The new values of the hook_height | 

### Return type

[**GetHookHeight**](GetHookHeight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mir.HookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/status
    api_response = api_instance.hook_status_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HookApi->hook_status_get: %s\n" % e)
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

