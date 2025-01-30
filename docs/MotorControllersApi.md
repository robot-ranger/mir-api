# mir.MotorControllersApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_setup_serial_devices_motor_controllers_get**](MotorControllersApi.md#system_setup_serial_devices_motor_controllers_get) | **GET** /system/setup/serial_devices/motor_controllers | GET /system/setup/serial_devices/motor_controllers
[**system_setup_serial_devices_motor_controllers_put**](MotorControllersApi.md#system_setup_serial_devices_motor_controllers_put) | **PUT** /system/setup/serial_devices/motor_controllers | PUT /system/setup/serial_devices/motor_controllers


# **system_setup_serial_devices_motor_controllers_get**
> list[GetSetupMcSerials] system_setup_serial_devices_motor_controllers_get(authorization, accept_language)

GET /system/setup/serial_devices/motor_controllers

Retrieve the setup information about FTDI adapters of motor controllers.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MotorControllersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/motor_controllers
    api_response = api_instance.system_setup_serial_devices_motor_controllers_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotorControllersApi->system_setup_serial_devices_motor_controllers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSetupMcSerials]**](GetSetupMcSerials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_setup_serial_devices_motor_controllers_put**
> GetSetupMcSerials system_setup_serial_devices_motor_controllers_put(authorization, accept_language, setup_mc_serials)

PUT /system/setup/serial_devices/motor_controllers

Modify motor controller serials

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MotorControllersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_mc_serials = mir.PutSetupMcSerials() # PutSetupMcSerials | The new values of the setup_mc_serials

try:
    # PUT /system/setup/serial_devices/motor_controllers
    api_response = api_instance.system_setup_serial_devices_motor_controllers_put(authorization, accept_language, setup_mc_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotorControllersApi->system_setup_serial_devices_motor_controllers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **setup_mc_serials** | [**PutSetupMcSerials**](PutSetupMcSerials.md)| The new values of the setup_mc_serials | 

### Return type

[**GetSetupMcSerials**](GetSetupMcSerials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

