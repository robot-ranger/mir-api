# mir.RemoteSupportApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_support_get**](RemoteSupportApi.md#remote_support_get) | **GET** /remote_support | GET /remote_support
[**remote_support_log_get**](RemoteSupportApi.md#remote_support_log_get) | **GET** /remote_support/log | GET /remote_support/log
[**remote_support_put**](RemoteSupportApi.md#remote_support_put) | **PUT** /remote_support | PUT /remote_support


# **remote_support_get**
> GetRemoteSupport remote_support_get(authorization, accept_language)

GET /remote_support

Retrieve the status of the remote support connection

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RemoteSupportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /remote_support
    api_response = api_instance.remote_support_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSupportApi->remote_support_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetRemoteSupport**](GetRemoteSupport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_support_log_get**
> GetRemoteSupportLog remote_support_log_get(authorization, accept_language)

GET /remote_support/log

Retrieve the list with the actions performed by the remote support controller

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RemoteSupportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /remote_support/log
    api_response = api_instance.remote_support_log_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSupportApi->remote_support_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetRemoteSupportLog**](GetRemoteSupportLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_support_put**
> GetRemoteSupport remote_support_put(authorization, accept_language, remote_support)

PUT /remote_support

Modify the remote support connection timeout

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RemoteSupportApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
remote_support = mir.PutRemoteSupport() # PutRemoteSupport | The new values of the remote_support

try:
    # PUT /remote_support
    api_response = api_instance.remote_support_put(authorization, accept_language, remote_support)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSupportApi->remote_support_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **remote_support** | [**PutRemoteSupport**](PutRemoteSupport.md)| The new values of the remote_support | 

### Return type

[**GetRemoteSupport**](GetRemoteSupport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

