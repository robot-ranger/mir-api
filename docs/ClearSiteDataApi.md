# mir.ClearSiteDataApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_site_data_post**](ClearSiteDataApi.md#clear_site_data_post) | **POST** /clear_site_data | POST /clear_site_data


# **clear_site_data_post**
> GetClearSiteData clear_site_data_post(authorization, accept_language)

POST /clear_site_data

Clear site data

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ClearSiteDataApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # POST /clear_site_data
    api_response = api_instance.clear_site_data_post(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClearSiteDataApi->clear_site_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetClearSiteData**](GetClearSiteData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

