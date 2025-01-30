# mir.ShelfsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docking_offsets_shelfs_get**](ShelfsApi.md#docking_offsets_shelfs_get) | **GET** /docking_offsets/shelfs | GET /docking_offsets/shelfs


# **docking_offsets_shelfs_get**
> list[GetDockingOffsetsNoPos] docking_offsets_shelfs_get(authorization, accept_language)

GET /docking_offsets/shelfs

Retrieve the list of docking offsets

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ShelfsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /docking_offsets/shelfs
    api_response = api_instance.docking_offsets_shelfs_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShelfsApi->docking_offsets_shelfs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetDockingOffsetsNoPos]**](GetDockingOffsetsNoPos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

