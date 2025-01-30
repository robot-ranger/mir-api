# mir.SwaggerApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**swagger_get**](SwaggerApi.md#swagger_get) | **GET** /swagger | GET /swagger


# **swagger_get**
> GetSwaggerDoc swagger_get(authorization, accept_language)

GET /swagger

Retrieve the swagger definition of the API

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SwaggerApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /swagger
    api_response = api_instance.swagger_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwaggerApi->swagger_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSwaggerDoc**](GetSwaggerDoc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

