# mir.CamerasApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_setup_cameras_get**](CamerasApi.md#system_setup_cameras_get) | **GET** /system/setup/cameras | GET /system/setup/cameras
[**system_setup_cameras_put**](CamerasApi.md#system_setup_cameras_put) | **PUT** /system/setup/cameras | PUT /system/setup/cameras


# **system_setup_cameras_get**
> list[GetSetupCameras] system_setup_cameras_get(authorization, accept_language)

GET /system/setup/cameras

Retrieve the setup information about Cameras.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CamerasApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/cameras
    api_response = api_instance.system_setup_cameras_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CamerasApi->system_setup_cameras_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSetupCameras]**](GetSetupCameras.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_setup_cameras_put**
> GetSetupCameras system_setup_cameras_put(authorization, accept_language, setup_cameras)

PUT /system/setup/cameras

Modify camera settings

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CamerasApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_cameras = mir.PutSetupCameras() # PutSetupCameras | The new values of the setup_cameras

try:
    # PUT /system/setup/cameras
    api_response = api_instance.system_setup_cameras_put(authorization, accept_language, setup_cameras)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CamerasApi->system_setup_cameras_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **setup_cameras** | [**PutSetupCameras**](PutSetupCameras.md)| The new values of the setup_cameras | 

### Return type

[**GetSetupCameras**](GetSetupCameras.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

