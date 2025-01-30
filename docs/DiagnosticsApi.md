# mir.DiagnosticsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experimental_diagnostics_get**](DiagnosticsApi.md#experimental_diagnostics_get) | **GET** /experimental/diagnostics | GET /experimental/diagnostics


# **experimental_diagnostics_get**
> GetDiagnostics experimental_diagnostics_get(authorization, accept_language)

GET /experimental/diagnostics

Retrieve diagnostics status

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DiagnosticsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /experimental/diagnostics
    api_response = api_instance.experimental_diagnostics_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->experimental_diagnostics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetDiagnostics**](GetDiagnostics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

