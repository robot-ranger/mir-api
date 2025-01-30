# mir.LasersApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_setup_serial_devices_lasers_get**](LasersApi.md#system_setup_serial_devices_lasers_get) | **GET** /system/setup/serial_devices/lasers | GET /system/setup/serial_devices/lasers
[**system_setup_serial_devices_lasers_put**](LasersApi.md#system_setup_serial_devices_lasers_put) | **PUT** /system/setup/serial_devices/lasers | PUT /system/setup/serial_devices/lasers


# **system_setup_serial_devices_lasers_get**
> list[GetSetupLaserSerials] system_setup_serial_devices_lasers_get(authorization, accept_language)

GET /system/setup/serial_devices/lasers

Retrieve the setup information about FTDI adapters of laser scanners.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.LasersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/lasers
    api_response = api_instance.system_setup_serial_devices_lasers_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LasersApi->system_setup_serial_devices_lasers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSetupLaserSerials]**](GetSetupLaserSerials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_setup_serial_devices_lasers_put**
> GetSetupLaserSerials system_setup_serial_devices_lasers_put(authorization, accept_language, setup_laser_serials)

PUT /system/setup/serial_devices/lasers

Modify laser serials

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.LasersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_laser_serials = mir.PutSetupLaserSerials() # PutSetupLaserSerials | The new values of the setup_laser_serials

try:
    # PUT /system/setup/serial_devices/lasers
    api_response = api_instance.system_setup_serial_devices_lasers_put(authorization, accept_language, setup_laser_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LasersApi->system_setup_serial_devices_lasers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **setup_laser_serials** | [**PutSetupLaserSerials**](PutSetupLaserSerials.md)| The new values of the setup_laser_serials | 

### Return type

[**GetSetupLaserSerials**](GetSetupLaserSerials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

