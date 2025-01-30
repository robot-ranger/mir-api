# mir.DistanceApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_distance_get**](DistanceApi.md#statistics_distance_get) | **GET** /statistics/distance | GET /statistics/distance


# **statistics_distance_get**
> GetDistanceStatistics statistics_distance_get(authorization, accept_language)

GET /statistics/distance

Retrieve the list with the distance driven by the robot at different dates and times

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DistanceApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /statistics/distance
    api_response = api_instance.statistics_distance_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistanceApi->statistics_distance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetDistanceStatistics**](GetDistanceStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

