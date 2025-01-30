# mir.LogsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_logs_get**](LogsApi.md#software_logs_get) | **GET** /software/logs | GET /software/logs
[**software_logs_guid_get**](LogsApi.md#software_logs_guid_get) | **GET** /software/logs/{guid} | GET /software/logs/{guid}


# **software_logs_get**
> list[GetSoftwareLogs] software_logs_get(authorization, accept_language)

GET /software/logs

Retrieve the list of software upgrade logs

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.LogsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/logs
    api_response = api_instance.software_logs_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->software_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareLogs]**](GetSoftwareLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_logs_guid_get**
> GetSoftwareLog software_logs_guid_get(authorization, accept_language, guid)

GET /software/logs/{guid}

Retrieve the details about the software upgrade log with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.LogsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /software/logs/{guid}
    api_response = api_instance.software_logs_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->software_logs_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoftwareLog**](GetSoftwareLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

