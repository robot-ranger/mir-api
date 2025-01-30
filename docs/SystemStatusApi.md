# mir.SystemStatusApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_system_status_get**](SystemStatusApi.md#software_system_status_get) | **GET** /software/system_status | GET /software/system_status


# **software_system_status_get**
> list[GetSoftwareSystemStatus] software_system_status_get(authorization, accept_language)

GET /software/system_status

Retrieve information related to the upgrading system in the robot.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SystemStatusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/system_status
    api_response = api_instance.software_system_status_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStatusApi->software_system_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareSystemStatus]**](GetSoftwareSystemStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

