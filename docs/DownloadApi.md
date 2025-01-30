# mir.DownloadApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_error_reports_id_download_get**](DownloadApi.md#log_error_reports_id_download_get) | **GET** /log/error_reports/{id}/download | GET /log/error_reports/{id}/download
[**system_setup_sick_configs_guid_download_get**](DownloadApi.md#system_setup_sick_configs_guid_download_get) | **GET** /system/setup/sick_configs/{guid}/download | GET /system/setup/sick_configs/{guid}/download


# **log_error_reports_id_download_get**
> GetErrorReportDownload log_error_reports_id_download_get(authorization, accept_language, id)

GET /log/error_reports/{id}/download

Download the file containing the error report with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DownloadApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /log/error_reports/{id}/download
    api_response = api_instance.log_error_reports_id_download_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->log_error_reports_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to search for | 

### Return type

[**GetErrorReportDownload**](GetErrorReportDownload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_setup_sick_configs_guid_download_get**
> GetSickConfigDownload system_setup_sick_configs_guid_download_get(authorization, accept_language, guid)

GET /system/setup/sick_configs/{guid}/download

Download sick configuration file.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DownloadApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /system/setup/sick_configs/{guid}/download
    api_response = api_instance.system_setup_sick_configs_guid_download_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->system_setup_sick_configs_guid_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSickConfigDownload**](GetSickConfigDownload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

