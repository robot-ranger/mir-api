# mir.SoftwareApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_backups_get**](SoftwareApi.md#software_backups_get) | **GET** /software/backups | GET /software/backups
[**software_backups_guid_delete**](SoftwareApi.md#software_backups_guid_delete) | **DELETE** /software/backups/{guid} | DELETE /software/backups/{guid}
[**software_backups_guid_get**](SoftwareApi.md#software_backups_guid_get) | **GET** /software/backups/{guid} | GET /software/backups/{guid}
[**software_backups_guid_post**](SoftwareApi.md#software_backups_guid_post) | **POST** /software/backups/{guid} | POST /software/backups/{guid}
[**software_backups_post**](SoftwareApi.md#software_backups_post) | **POST** /software/backups | POST /software/backups
[**software_hook_interface_get**](SoftwareApi.md#software_hook_interface_get) | **GET** /software/hook_interface | GET /software/hook_interface
[**software_hook_interface_post**](SoftwareApi.md#software_hook_interface_post) | **POST** /software/hook_interface | POST /software/hook_interface
[**software_logs_get**](SoftwareApi.md#software_logs_get) | **GET** /software/logs | GET /software/logs
[**software_logs_guid_get**](SoftwareApi.md#software_logs_guid_get) | **GET** /software/logs/{guid} | GET /software/logs/{guid}
[**software_robot_peripherals_status_get**](SoftwareApi.md#software_robot_peripherals_status_get) | **GET** /software/robot_peripherals_status | GET /software/robot_peripherals_status
[**software_system_status_get**](SoftwareApi.md#software_system_status_get) | **GET** /software/system_status | GET /software/system_status
[**software_upgrades_get**](SoftwareApi.md#software_upgrades_get) | **GET** /software/upgrades | GET /software/upgrades
[**software_upgrades_guid_delete**](SoftwareApi.md#software_upgrades_guid_delete) | **DELETE** /software/upgrades/{guid} | DELETE /software/upgrades/{guid}
[**software_upgrades_guid_get**](SoftwareApi.md#software_upgrades_guid_get) | **GET** /software/upgrades/{guid} | GET /software/upgrades/{guid}
[**software_upgrades_guid_post**](SoftwareApi.md#software_upgrades_guid_post) | **POST** /software/upgrades/{guid} | POST /software/upgrades/{guid}
[**software_upgrades_post**](SoftwareApi.md#software_upgrades_post) | **POST** /software/upgrades | POST /software/upgrades


# **software_backups_get**
> list[GetSoftwareBackups] software_backups_get(authorization, accept_language)

GET /software/backups

Retrieve the list with all the software backups

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/backups
    api_response = api_instance.software_backups_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_backups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareBackups]**](GetSoftwareBackups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_delete**
> software_backups_guid_delete(authorization, accept_language, guid)

DELETE /software/backups/{guid}

Erase the software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /software/backups/{guid}
    api_instance.software_backups_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_backups_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_get**
> GetSoftwareBackup software_backups_guid_get(authorization, accept_language, guid)

GET /software/backups/{guid}

Retrieve the details about the software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /software/backups/{guid}
    api_response = api_instance.software_backups_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_backups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoftwareBackup**](GetSoftwareBackup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_post**
> GetSoftwareBackup software_backups_guid_post(authorization, accept_language, guid)

POST /software/backups/{guid}

If it exists a software backup with the specified GUID it will restore that backup. Otherwise, it will create a software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to

try:
    # POST /software/backups/{guid}
    api_response = api_instance.software_backups_guid_post(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_backups_guid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to add the new resource to | 

### Return type

[**GetSoftwareBackup**](GetSoftwareBackup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_post**
> GetSoftwareBackups software_backups_post(authorization, accept_language)

POST /software/backups

Create a new software backup

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # POST /software/backups
    api_response = api_instance.software_backups_post(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_backups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSoftwareBackups**](GetSoftwareBackups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_hook_interface_get**
> GetHookSoftwareInterface software_hook_interface_get(authorization, accept_language)

GET /software/hook_interface

Retrieve the information about the hook software interface

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/hook_interface
    api_response = api_instance.software_hook_interface_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_hook_interface_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetHookSoftwareInterface**](GetHookSoftwareInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_hook_interface_post**
> GetHookSoftwareInterface software_hook_interface_post(authorization, accept_language, hook_software_interface)

POST /software/hook_interface

Proceed with hook upgrade

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
hook_software_interface = mir.PostHookSoftwareInterface() # PostHookSoftwareInterface | The details of the hook_software_interface

try:
    # POST /software/hook_interface
    api_response = api_instance.software_hook_interface_post(authorization, accept_language, hook_software_interface)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_hook_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **hook_software_interface** | [**PostHookSoftwareInterface**](PostHookSoftwareInterface.md)| The details of the hook_software_interface | 

### Return type

[**GetHookSoftwareInterface**](GetHookSoftwareInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_logs_get**
> list[GetSoftwareLogs] software_logs_get(authorization, accept_language)

GET /software/logs

Retrieve the list of software upgrade logs

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/logs
    api_response = api_instance.software_logs_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareLogs]**](GetSoftwareLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_logs_guid_get**
> GetSoftwareLog software_logs_guid_get(authorization, accept_language, guid)

GET /software/logs/{guid}

Retrieve the details about the software upgrade log with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /software/logs/{guid}
    api_response = api_instance.software_logs_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_logs_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoftwareLog**](GetSoftwareLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_robot_peripherals_status_get**
> list[GetSoftwareRobotPeripheralsStatus] software_robot_peripherals_status_get(authorization, accept_language)

GET /software/robot_peripherals_status

Retrieve information related to the peripherals running upgrade routines in the robot..

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/robot_peripherals_status
    api_response = api_instance.software_robot_peripherals_status_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_robot_peripherals_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareRobotPeripheralsStatus]**](GetSoftwareRobotPeripheralsStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_status_get**
> list[GetSoftwareSystemStatus] software_system_status_get(authorization, accept_language)

GET /software/system_status

Retrieve information related to the upgrading system in the robot.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/system_status
    api_response = api_instance.software_system_status_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_system_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareSystemStatus]**](GetSoftwareSystemStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_get**
> list[GetSoftwareUpgrades] software_upgrades_get(authorization, accept_language)

GET /software/upgrades

Retrieve a list of the software upgrade performed

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/upgrades
    api_response = api_instance.software_upgrades_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_upgrades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareUpgrades]**](GetSoftwareUpgrades.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_delete**
> software_upgrades_guid_delete(authorization, accept_language, guid)

DELETE /software/upgrades/{guid}

Erase the upgrade file with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /software/upgrades/{guid}
    api_instance.software_upgrades_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_upgrades_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_get**
> GetSoftwareUpgrade software_upgrades_guid_get(authorization, accept_language, guid)

GET /software/upgrades/{guid}

Retrieve the details of the software upgrade with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /software/upgrades/{guid}
    api_response = api_instance.software_upgrades_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_upgrades_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoftwareUpgrade**](GetSoftwareUpgrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_post**
> GetSoftwareUpgrade software_upgrades_guid_post(authorization, accept_language, guid)

POST /software/upgrades/{guid}

Upgrade to the version of the upgrade file with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to

try:
    # POST /software/upgrades/{guid}
    api_response = api_instance.software_upgrades_guid_post(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_upgrades_guid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to add the new resource to | 

### Return type

[**GetSoftwareUpgrade**](GetSoftwareUpgrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_post**
> GetSoftwareUpgrades software_upgrades_post(authorization, accept_language)

POST /software/upgrades

Upgrade with the provided upgrade file

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoftwareApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # POST /software/upgrades
    api_response = api_instance.software_upgrades_post(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_upgrades_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSoftwareUpgrades**](GetSoftwareUpgrades.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

