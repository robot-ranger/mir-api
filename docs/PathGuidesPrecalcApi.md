# mir.PathGuidesPrecalcApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**path_guides_precalc_get**](PathGuidesPrecalcApi.md#path_guides_precalc_get) | **GET** /path_guides_precalc | GET /path_guides_precalc
[**path_guides_precalc_post**](PathGuidesPrecalcApi.md#path_guides_precalc_post) | **POST** /path_guides_precalc | POST /path_guides_precalc


# **path_guides_precalc_get**
> GetPathGuidesPrecalc path_guides_precalc_get(authorization, accept_language)

GET /path_guides_precalc

Retrieve the status of path guides precalculation

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesPrecalcApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /path_guides_precalc
    api_response = api_instance.path_guides_precalc_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesPrecalcApi->path_guides_precalc_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetPathGuidesPrecalc**](GetPathGuidesPrecalc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_precalc_post**
> GetPathGuidesPrecalc path_guides_precalc_post(authorization, accept_language, path_guides_precalc)

POST /path_guides_precalc

Start/stop precalculation of the specified path guide

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesPrecalcApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guides_precalc = mir.PostPathGuidesPrecalc() # PostPathGuidesPrecalc | The details of the path_guides_precalc

try:
    # POST /path_guides_precalc
    api_response = api_instance.path_guides_precalc_post(authorization, accept_language, path_guides_precalc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesPrecalcApi->path_guides_precalc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guides_precalc** | [**PostPathGuidesPrecalc**](PostPathGuidesPrecalc.md)| The details of the path_guides_precalc | 

### Return type

[**GetPathGuidesPrecalc**](GetPathGuidesPrecalc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

