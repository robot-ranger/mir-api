# mir.OptionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**path_guides_path_guide_guid_options_get**](OptionsApi.md#path_guides_path_guide_guid_options_get) | **GET** /path_guides/{path_guide_guid}/options | GET /path_guides/{path_guide_guid}/options


# **path_guides_path_guide_guid_options_get**
> GetPathGuideOptions path_guides_path_guide_guid_options_get(authorization, accept_language, path_guide_guid)

GET /path_guides/{path_guide_guid}/options

Retrieve the list of allowed start/via/goal options for the selected path guide

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.OptionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for

try:
    # GET /path_guides/{path_guide_guid}/options
    api_response = api_instance.path_guides_path_guide_guid_options_get(authorization, accept_language, path_guide_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->path_guides_path_guide_guid_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guide_guid** | **str**| The path_guide_guid to search for | 

### Return type

[**GetPathGuideOptions**](GetPathGuideOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

