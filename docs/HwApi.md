# mir.HwApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hw_export_get**](HwApi.md#hw_export_get) | **GET** /hw/export | GET /hw/export
[**hw_import_post**](HwApi.md#hw_import_post) | **POST** /hw/import | POST /hw/import


# **hw_export_get**
> GetHwConfigExport hw_export_get(authorization, accept_language)

GET /hw/export

Download a file containing the hardware configuration of the robot

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.HwApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /hw/export
    api_response = api_instance.hw_export_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HwApi->hw_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHwConfigExport**](GetHwConfigExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hw_import_post**
> GetHwConfigImport hw_import_post(authorization, accept_language, hw_config_import)

POST /hw/import

Import the hardware configuration contained in the file into the robot

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.HwApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hw_config_import = mir.PostHwConfigImport() # PostHwConfigImport | The details of the hw_config_import

try:
    # POST /hw/import
    api_response = api_instance.hw_import_post(authorization, accept_language, hw_config_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HwApi->hw_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **hw_config_import** | [**PostHwConfigImport**](PostHwConfigImport.md)| The details of the hw_config_import | 

### Return type

[**GetHwConfigImport**](GetHwConfigImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

