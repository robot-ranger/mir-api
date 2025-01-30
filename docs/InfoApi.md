# mir.InfoApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_info_get**](InfoApi.md#system_info_get) | **GET** /system/info | GET /system/info


# **system_info_get**
> GetSystemInfo system_info_get(authorization, accept_language)

GET /system/info

Retrieve the information about the system. It contains different information like serial numbers of hardware components, MAC addresses of network cards, etc...

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.InfoApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/info
    api_response = api_instance.system_info_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->system_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSystemInfo**](GetSystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

