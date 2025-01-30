# mir.RecordApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maps_record_get**](RecordApi.md#maps_record_get) | **GET** /maps/record | GET /maps/record
[**maps_record_put**](RecordApi.md#maps_record_put) | **PUT** /maps/record | PUT /maps/record


# **maps_record_get**
> GetMapRecord maps_record_get(authorization, accept_language)

GET /maps/record

Retrive the latest recording of a map

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RecordApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /maps/record
    api_response = api_instance.maps_record_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->maps_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetMapRecord**](GetMapRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_record_put**
> GetMapRecord maps_record_put(authorization, accept_language, map_record)

PUT /maps/record

Start and stop the recording of a map

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RecordApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_record = mir.PutMapRecord() # PutMapRecord | The new values of the map_record

try:
    # PUT /maps/record
    api_response = api_instance.maps_record_put(authorization, accept_language, map_record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->maps_record_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **map_record** | [**PutMapRecord**](PutMapRecord.md)| The new values of the map_record | 

### Return type

[**GetMapRecord**](GetMapRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

