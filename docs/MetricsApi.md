# mir.MetricsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_get**](MetricsApi.md#metrics_get) | **GET** /metrics | GET /metrics


# **metrics_get**
> GetMetrics metrics_get(authorization, accept_language, accept=accept)

GET /metrics

Retrieve the latests MiR metrics related to the given MiR product in the Prometheus or OpenMetrics text format. Default: OpenMetrics.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MetricsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
accept = ['accept_example'] # list[str] | The response content types accepted by the client (optional)

try:
    # GET /metrics
    api_response = api_instance.metrics_get(authorization, accept_language, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **accept** | [**list[str]**](str.md)| The response content types accepted by the client | [optional] 

### Return type

[**GetMetrics**](GetMetrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/openmetrics-text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

