# mir.FactoryResetApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factory_reset_post**](FactoryResetApi.md#factory_reset_post) | **POST** /factory_reset | POST /factory_reset


# **factory_reset_post**
> GetFactoryReset factory_reset_post(authorization, accept_language, factory_reset)

POST /factory_reset

Clean and migrate the database. Keep hardware configurations

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.FactoryResetApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
factory_reset = mir.PostFactoryReset() # PostFactoryReset | The details of the factory_reset

try:
    # POST /factory_reset
    api_response = api_instance.factory_reset_post(authorization, accept_language, factory_reset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactoryResetApi->factory_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **factory_reset** | [**PostFactoryReset**](PostFactoryReset.md)| The details of the factory_reset | 

### Return type

[**GetFactoryReset**](GetFactoryReset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

