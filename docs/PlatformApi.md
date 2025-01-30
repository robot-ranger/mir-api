# mir.PlatformApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_timezone_get**](PlatformApi.md#platform_timezone_get) | **GET** /platform/timezone | GET /platform/timezone
[**platform_timezone_post**](PlatformApi.md#platform_timezone_post) | **POST** /platform/timezone | POST /platform/timezone


# **platform_timezone_get**
> GetTimezone platform_timezone_get(authorization, accept_language)

GET /platform/timezone

Gets the user set timezone

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PlatformApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /platform/timezone
    api_response = api_instance.platform_timezone_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_timezone_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetTimezone**](GetTimezone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_timezone_post**
> GetTimezone platform_timezone_post(authorization, accept_language, timezone)

POST /platform/timezone

Sets the user timezone

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PlatformApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
timezone = mir.PostTimezone() # PostTimezone | The details of the timezone

try:
    # POST /platform/timezone
    api_response = api_instance.platform_timezone_post(authorization, accept_language, timezone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_timezone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **timezone** | [**PostTimezone**](PostTimezone.md)| The details of the timezone | 

### Return type

[**GetTimezone**](GetTimezone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

