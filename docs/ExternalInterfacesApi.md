# mir.ExternalInterfacesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_setup_serial_devices_external_interfaces_get**](ExternalInterfacesApi.md#system_setup_serial_devices_external_interfaces_get) | **GET** /system/setup/serial_devices/external_interfaces | GET /system/setup/serial_devices/external_interfaces
[**system_setup_serial_devices_external_interfaces_put**](ExternalInterfacesApi.md#system_setup_serial_devices_external_interfaces_put) | **PUT** /system/setup/serial_devices/external_interfaces | PUT /system/setup/serial_devices/external_interfaces


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
api_instance = mir.ExternalInterfacesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /system/setup/serial_devices/external_interfaces
    api_response = api_instance.system_setup_serial_devices_external_interfaces_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalInterfacesApi->system_setup_serial_devices_external_interfaces_get: %s\n" % e)
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
api_instance = mir.ExternalInterfacesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
setup_external_interface_serials = mir.PutSetupExternalInterfaceSerials() # PutSetupExternalInterfaceSerials | The new values of the setup_external_interface_serials

try:
    # PUT /system/setup/serial_devices/external_interfaces
    api_response = api_instance.system_setup_serial_devices_external_interfaces_put(authorization, accept_language, setup_external_interface_serials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalInterfacesApi->system_setup_serial_devices_external_interfaces_put: %s\n" % e)
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

