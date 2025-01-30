# mir.StreamApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sounds_guid_stream_get**](StreamApi.md#sounds_guid_stream_get) | **GET** /sounds/{guid}/stream | GET /sounds/{guid}/stream


# **sounds_guid_stream_get**
> GetSoundStream sounds_guid_stream_get(authorization, accept_language, guid)

GET /sounds/{guid}/stream

Download the sound file of the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.StreamApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /sounds/{guid}/stream
    api_response = api_instance.sounds_guid_stream_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamApi->sounds_guid_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoundStream**](GetSoundStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

