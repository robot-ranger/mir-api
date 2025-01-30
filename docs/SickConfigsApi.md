# mir.SickConfigsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_setup_sick_configs_get**](SickConfigsApi.md#system_setup_sick_configs_get) | **GET** /system/setup/sick_configs | GET /system/setup/sick_configs
[**system_setup_sick_configs_guid_download_get**](SickConfigsApi.md#system_setup_sick_configs_guid_download_get) | **GET** /system/setup/sick_configs/{guid}/download | GET /system/setup/sick_configs/{guid}/download
[**system_setup_sick_configs_guid_get**](SickConfigsApi.md#system_setup_sick_configs_guid_get) | **GET** /system/setup/sick_configs/{guid} | GET /system/setup/sick_configs/{guid}


# **system_setup_sick_configs_get**
> list[GetSickConfigs] system_setup_sick_configs_get(authorization, accept_language)

GET /system/setup/sick_configs

Get configuration description of sick configuration file.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SickConfigsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/sick_configs
    api_response = api_instance.system_setup_sick_configs_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SickConfigsApi->system_setup_sick_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSickConfigs]**](GetSickConfigs.md)

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
api_instance = mir.SickConfigsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /system/setup/sick_configs/{guid}/download
    api_response = api_instance.system_setup_sick_configs_guid_download_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SickConfigsApi->system_setup_sick_configs_guid_download_get: %s\n" % e)
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

# **system_setup_sick_configs_guid_get**
> GetSickConfig system_setup_sick_configs_guid_get(authorization, accept_language, guid)

GET /system/setup/sick_configs/{guid}

Get configuration description of sick configuration file.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SickConfigsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /system/setup/sick_configs/{guid}
    api_response = api_instance.system_setup_sick_configs_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SickConfigsApi->system_setup_sick_configs_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSickConfig**](GetSickConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

