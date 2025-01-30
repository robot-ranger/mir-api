# mir.DefinitionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_definitions_get**](DefinitionsApi.md#zones_definitions_get) | **GET** /zones/definitions | GET /zones/definitions


# **zones_definitions_get**
> GetZonesDefinitions zones_definitions_get(authorization, accept_language)

GET /zones/definitions

Retrieve definitions of zones and their actions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DefinitionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /zones/definitions
    api_response = api_instance.zones_definitions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionsApi->zones_definitions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetZonesDefinitions**](GetZonesDefinitions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

