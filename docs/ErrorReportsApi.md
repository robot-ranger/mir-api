# mir.ErrorReportsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_error_reports_delete**](ErrorReportsApi.md#log_error_reports_delete) | **DELETE** /log/error_reports | DELETE /log/error_reports
[**log_error_reports_get**](ErrorReportsApi.md#log_error_reports_get) | **GET** /log/error_reports | GET /log/error_reports
[**log_error_reports_id_delete**](ErrorReportsApi.md#log_error_reports_id_delete) | **DELETE** /log/error_reports/{id} | DELETE /log/error_reports/{id}
[**log_error_reports_id_download_get**](ErrorReportsApi.md#log_error_reports_id_download_get) | **GET** /log/error_reports/{id}/download | GET /log/error_reports/{id}/download
[**log_error_reports_id_get**](ErrorReportsApi.md#log_error_reports_id_get) | **GET** /log/error_reports/{id} | GET /log/error_reports/{id}
[**log_error_reports_post**](ErrorReportsApi.md#log_error_reports_post) | **POST** /log/error_reports | POST /log/error_reports


# **log_error_reports_delete**
> log_error_reports_delete(authorization, accept_language)

DELETE /log/error_reports

Erase ALL the error reports

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ErrorReportsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # DELETE /log/error_reports
    api_instance.log_error_reports_delete(authorization, accept_language)
except ApiException as e:
    print("Exception when calling ErrorReportsApi->log_error_reports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_get**
> GetErrorReports log_error_reports_get(authorization, accept_language)

GET /log/error_reports

Retrieve the list of error reports

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ErrorReportsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /log/error_reports
    api_response = api_instance.log_error_reports_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorReportsApi->log_error_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetErrorReports**](GetErrorReports.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_id_delete**
> log_error_reports_id_delete(authorization, accept_language, id)

DELETE /log/error_reports/{id}

Erase the error report with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ErrorReportsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to delete

try:
    # DELETE /log/error_reports/{id}
    api_instance.log_error_reports_id_delete(authorization, accept_language, id)
except ApiException as e:
    print("Exception when calling ErrorReportsApi->log_error_reports_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mir.ErrorReportsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /log/error_reports/{id}/download
    api_response = api_instance.log_error_reports_id_download_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorReportsApi->log_error_reports_id_download_get: %s\n" % e)
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

# **log_error_reports_id_get**
> GetErrorReport log_error_reports_id_get(authorization, accept_language, id)

GET /log/error_reports/{id}

Retrieve the details about the error report with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ErrorReportsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /log/error_reports/{id}
    api_response = api_instance.log_error_reports_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorReportsApi->log_error_reports_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to search for | 

### Return type

[**GetErrorReport**](GetErrorReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_post**
> GetErrorReports log_error_reports_post(authorization, accept_language, error_reports)

POST /log/error_reports

Generate a new error report. This will record the 30s previous to this call in a file.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ErrorReportsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
error_reports = mir.PostErrorReports() # PostErrorReports | The details of the error_reports

try:
    # POST /log/error_reports
    api_response = api_instance.log_error_reports_post(authorization, accept_language, error_reports)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorReportsApi->log_error_reports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **error_reports** | [**PostErrorReports**](PostErrorReports.md)| The details of the error_reports | 

### Return type

[**GetErrorReports**](GetErrorReports.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

