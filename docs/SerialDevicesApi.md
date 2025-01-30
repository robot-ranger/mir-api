# mir.SerialDevicesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_setup_serial_devices_external_interfaces_get**](SerialDevicesApi.md#system_setup_serial_devices_external_interfaces_get) | **GET** /system/setup/serial_devices/external_interfaces | GET /system/setup/serial_devices/external_interfaces
[**system_setup_serial_devices_external_interfaces_put**](SerialDevicesApi.md#system_setup_serial_devices_external_interfaces_put) | **PUT** /system/setup/serial_devices/external_interfaces | PUT /system/setup/serial_devices/external_interfaces
[**system_setup_serial_devices_get**](SerialDevicesApi.md#system_setup_serial_devices_get) | **GET** /system/setup/serial_devices | GET /system/setup/serial_devices
[**system_setup_serial_devices_id_get**](SerialDevicesApi.md#system_setup_serial_devices_id_get) | **GET** /system/setup/serial_devices/{id} | GET /system/setup/serial_devices/{id}
[**system_setup_serial_devices_lasers_get**](SerialDevicesApi.md#system_setup_serial_devices_lasers_get) | **GET** /system/setup/serial_devices/lasers | GET /system/setup/serial_devices/lasers
[**system_setup_serial_devices_lasers_put**](SerialDevicesApi.md#system_setup_serial_devices_lasers_put) | **PUT** /system/setup/serial_devices/lasers | PUT /system/setup/serial_devices/lasers
[**system_setup_serial_devices_motor_controllers_get**](SerialDevicesApi.md#system_setup_serial_devices_motor_controllers_get) | **GET** /system/setup/serial_devices/motor_controllers | GET /system/setup/serial_devices/motor_controllers
[**system_setup_serial_devices_motor_controllers_put**](SerialDevicesApi.md#system_setup_serial_devices_motor_controllers_put) | **PUT** /system/setup/serial_devices/motor_controllers | PUT /system/setup/serial_devices/motor_controllers


# **system_setup_serial_devices_external_interfaces_get**
> list[GetSetupExternalInterfaceSerials] system_setup_serial_devices_external_interfaces_get(authorization, accept_language)

GET /system/setup/serial_devices/external_interfaces

Retrieve the setup information about FTDI adapters of external_interfaces.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/external_interfaces
    api_response = api_instance.system_setup_serial_devices_external_interfaces_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_external_interfaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSetupExternalInterfaceSerials]**](GetSetupExternalInterfaceSerials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_setup_serial_devices_external_interfaces_put**
> GetSetupExternalInterfaceSerials system_setup_serial_devices_external_interfaces_put(authorization, accept_language, setup_external_interface_serials)

PUT /system/setup/serial_devices/external_interfaces

Modify external interface serials

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_external_interface_serials = mir.PutSetupExternalInterfaceSerials() # PutSetupExternalInterfaceSerials | The new values of the setup_external_interface_serials

try:
    # PUT /system/setup/serial_devices/external_interfaces
    api_response = api_instance.system_setup_serial_devices_external_interfaces_put(authorization, accept_language, setup_external_interface_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_external_interfaces_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **setup_external_interface_serials** | [**PutSetupExternalInterfaceSerials**](PutSetupExternalInterfaceSerials.md)| The new values of the setup_external_interface_serials | 

### Return type

[**GetSetupExternalInterfaceSerials**](GetSetupExternalInterfaceSerials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_setup_serial_devices_get**
> list[GetSetupSerialDevices] system_setup_serial_devices_get(authorization, accept_language)

GET /system/setup/serial_devices

Retrieve the information about serial devices setup.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices
    api_response = api_instance.system_setup_serial_devices_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSetupSerialDevices]**](GetSetupSerialDevices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_setup_serial_devices_id_get**
> GetSetupSerialDevice system_setup_serial_devices_id_get(authorization, accept_language, id)

GET /system/setup/serial_devices/{id}

Retrieve the information about serial devices setup.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /system/setup/serial_devices/{id}
    api_response = api_instance.system_setup_serial_devices_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to search for | 

### Return type

[**GetSetupSerialDevice**](GetSetupSerialDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/lasers
    api_response = api_instance.system_setup_serial_devices_lasers_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_lasers_get: %s\n" % e)
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
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_laser_serials = mir.PutSetupLaserSerials() # PutSetupLaserSerials | The new values of the setup_laser_serials

try:
    # PUT /system/setup/serial_devices/lasers
    api_response = api_instance.system_setup_serial_devices_lasers_put(authorization, accept_language, setup_laser_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_lasers_put: %s\n" % e)
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
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/motor_controllers
    api_response = api_instance.system_setup_serial_devices_motor_controllers_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_motor_controllers_get: %s\n" % e)
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
api_instance = mir.SerialDevicesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_mc_serials = mir.PutSetupMcSerials() # PutSetupMcSerials | The new values of the setup_mc_serials

try:
    # PUT /system/setup/serial_devices/motor_controllers
    api_response = api_instance.system_setup_serial_devices_motor_controllers_put(authorization, accept_language, setup_mc_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerialDevicesApi->system_setup_serial_devices_motor_controllers_put: %s\n" % e)
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

