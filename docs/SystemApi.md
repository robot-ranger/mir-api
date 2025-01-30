# mir.SystemApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_info_get**](SystemApi.md#system_info_get) | **GET** /system/info | GET /system/info
[**system_protective_scan_get**](SystemApi.md#system_protective_scan_get) | **GET** /system/protective_scan | GET /system/protective_scan
[**system_setup_cameras_get**](SystemApi.md#system_setup_cameras_get) | **GET** /system/setup/cameras | GET /system/setup/cameras
[**system_setup_cameras_put**](SystemApi.md#system_setup_cameras_put) | **PUT** /system/setup/cameras | PUT /system/setup/cameras
[**system_setup_serial_devices_external_interfaces_get**](SystemApi.md#system_setup_serial_devices_external_interfaces_get) | **GET** /system/setup/serial_devices/external_interfaces | GET /system/setup/serial_devices/external_interfaces
[**system_setup_serial_devices_external_interfaces_put**](SystemApi.md#system_setup_serial_devices_external_interfaces_put) | **PUT** /system/setup/serial_devices/external_interfaces | PUT /system/setup/serial_devices/external_interfaces
[**system_setup_serial_devices_get**](SystemApi.md#system_setup_serial_devices_get) | **GET** /system/setup/serial_devices | GET /system/setup/serial_devices
[**system_setup_serial_devices_id_get**](SystemApi.md#system_setup_serial_devices_id_get) | **GET** /system/setup/serial_devices/{id} | GET /system/setup/serial_devices/{id}
[**system_setup_serial_devices_lasers_get**](SystemApi.md#system_setup_serial_devices_lasers_get) | **GET** /system/setup/serial_devices/lasers | GET /system/setup/serial_devices/lasers
[**system_setup_serial_devices_lasers_put**](SystemApi.md#system_setup_serial_devices_lasers_put) | **PUT** /system/setup/serial_devices/lasers | PUT /system/setup/serial_devices/lasers
[**system_setup_serial_devices_motor_controllers_get**](SystemApi.md#system_setup_serial_devices_motor_controllers_get) | **GET** /system/setup/serial_devices/motor_controllers | GET /system/setup/serial_devices/motor_controllers
[**system_setup_serial_devices_motor_controllers_put**](SystemApi.md#system_setup_serial_devices_motor_controllers_put) | **PUT** /system/setup/serial_devices/motor_controllers | PUT /system/setup/serial_devices/motor_controllers
[**system_setup_sick_configs_get**](SystemApi.md#system_setup_sick_configs_get) | **GET** /system/setup/sick_configs | GET /system/setup/sick_configs
[**system_setup_sick_configs_guid_download_get**](SystemApi.md#system_setup_sick_configs_guid_download_get) | **GET** /system/setup/sick_configs/{guid}/download | GET /system/setup/sick_configs/{guid}/download
[**system_setup_sick_configs_guid_get**](SystemApi.md#system_setup_sick_configs_guid_get) | **GET** /system/setup/sick_configs/{guid} | GET /system/setup/sick_configs/{guid}


# **system_info_get**
> GetSystemInfo system_info_get(authorization, accept_language)

GET /system/info

Retrieve the information about the system. It contains different information like serial numbers of hardware components, MAC addresses of network cards, etc...

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/info
    api_response = api_instance.system_info_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSystemInfo**](GetSystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_protective_scan_get**
> GetProtectiveScan system_protective_scan_get(authorization, accept_language)

GET /system/protective_scan

Retrieve PNG image visualizing the laser scans near the robot, including visualization of points in protective fields if supported.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/protective_scan
    api_response = api_instance.system_protective_scan_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_protective_scan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetProtectiveScan**](GetProtectiveScan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/cameras
    api_response = api_instance.system_setup_cameras_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_cameras_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_cameras = mir.PutSetupCameras() # PutSetupCameras | The new values of the setup_cameras

try:
    # PUT /system/setup/cameras
    api_response = api_instance.system_setup_cameras_put(authorization, accept_language, setup_cameras)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_cameras_put: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/external_interfaces
    api_response = api_instance.system_setup_serial_devices_external_interfaces_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_external_interfaces_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_external_interface_serials = mir.PutSetupExternalInterfaceSerials() # PutSetupExternalInterfaceSerials | The new values of the setup_external_interface_serials

try:
    # PUT /system/setup/serial_devices/external_interfaces
    api_response = api_instance.system_setup_serial_devices_external_interfaces_put(authorization, accept_language, setup_external_interface_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_external_interfaces_put: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices
    api_response = api_instance.system_setup_serial_devices_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /system/setup/serial_devices/{id}
    api_response = api_instance.system_setup_serial_devices_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_id_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/lasers
    api_response = api_instance.system_setup_serial_devices_lasers_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_lasers_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_laser_serials = mir.PutSetupLaserSerials() # PutSetupLaserSerials | The new values of the setup_laser_serials

try:
    # PUT /system/setup/serial_devices/lasers
    api_response = api_instance.system_setup_serial_devices_lasers_put(authorization, accept_language, setup_laser_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_lasers_put: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/motor_controllers
    api_response = api_instance.system_setup_serial_devices_motor_controllers_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_motor_controllers_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_mc_serials = mir.PutSetupMcSerials() # PutSetupMcSerials | The new values of the setup_mc_serials

try:
    # PUT /system/setup/serial_devices/motor_controllers
    api_response = api_instance.system_setup_serial_devices_motor_controllers_put(authorization, accept_language, setup_mc_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_serial_devices_motor_controllers_put: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/sick_configs
    api_response = api_instance.system_setup_sick_configs_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_sick_configs_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /system/setup/sick_configs/{guid}/download
    api_response = api_instance.system_setup_sick_configs_guid_download_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_sick_configs_guid_download_get: %s\n" % e)
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
api_instance = mir.SystemApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /system/setup/sick_configs/{guid}
    api_response = api_instance.system_setup_sick_configs_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_setup_sick_configs_guid_get: %s\n" % e)
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

