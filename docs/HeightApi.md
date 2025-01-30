# mir.HeightApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hook_height_get**](HeightApi.md#hook_height_get) | **GET** /hook/height | GET /hook/height
[**hook_height_put**](HeightApi.md#hook_height_put) | **PUT** /hook/height | PUT /hook/height


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
api_instance = mir.HeightApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hook/height
    api_response = api_instance.hook_height_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeightApi->hook_height_get: %s\n" % e)
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
api_instance = mir.HeightApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_height = mir.PutHookHeight() # PutHookHeight | The new values of the hook_height

try:
    # PUT /hook/height
    api_response = api_instance.hook_height_put(authorization, accept_language, hook_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeightApi->hook_height_put: %s\n" % e)
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

