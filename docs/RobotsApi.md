# mir.RobotsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**robots_post**](RobotsApi.md#robots_post) | **POST** /robots | POST /robots


# **robots_post**
> GetRobots robots_post(authorization, accept_language, robots)

POST /robots

Add information about other robots in the world. This is used by the Fleet manager to avoid robot collisions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RobotsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
robots = mir.PostRobots() # PostRobots | The details of the robots

try:
    # POST /robots
    api_response = api_instance.robots_post(authorization, accept_language, robots)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotsApi->robots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **robots** | [**PostRobots**](PostRobots.md)| The details of the robots | 

### Return type

[**GetRobots**](GetRobots.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

