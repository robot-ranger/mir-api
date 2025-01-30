# mir.ExportApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hw_export_get**](ExportApi.md#hw_export_get) | **GET** /hw/export | GET /hw/export
[**sessions_guid_export_get**](ExportApi.md#sessions_guid_export_get) | **GET** /sessions/{guid}/export | GET /sessions/{guid}/export


# **hw_export_get**
> GetHwConfigExport hw_export_get(authorization, accept_language)

GET /hw/export

Download a file containing the hardware configuration of the robot

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ExportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hw/export
    api_response = api_instance.hw_export_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->hw_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHwConfigExport**](GetHwConfigExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_export_get**
> GetSessionExport sessions_guid_export_get(authorization, accept_language, guid)

GET /sessions/{guid}/export

Download a file containing the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ExportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /sessions/{guid}/export
    api_response = api_instance.sessions_guid_export_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->sessions_guid_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSessionExport**](GetSessionExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

