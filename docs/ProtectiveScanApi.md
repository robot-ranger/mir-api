# mir.ProtectiveScanApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_protective_scan_get**](ProtectiveScanApi.md#system_protective_scan_get) | **GET** /system/protective_scan | GET /system/protective_scan


# **system_protective_scan_get**
> GetProtectiveScan system_protective_scan_get(authorization, accept_language)

GET /system/protective_scan

Retrieve PNG image visualizing the laser scans near the robot, including visualization of points in protective fields if supported.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ProtectiveScanApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/protective_scan
    api_response = api_instance.system_protective_scan_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectiveScanApi->system_protective_scan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetProtectiveScan**](GetProtectiveScan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

