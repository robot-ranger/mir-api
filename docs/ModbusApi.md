# mir.ModbusApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modbus_get**](ModbusApi.md#modbus_get) | **GET** /modbus | GET /modbus
[**modbus_id_get**](ModbusApi.md#modbus_id_get) | **GET** /modbus/{id} | GET /modbus/{id}
[**modbus_missions_get**](ModbusApi.md#modbus_missions_get) | **GET** /modbus/missions | GET /modbus/missions
[**modbus_missions_guid_delete**](ModbusApi.md#modbus_missions_guid_delete) | **DELETE** /modbus/missions/{guid} | DELETE /modbus/missions/{guid}
[**modbus_missions_guid_get**](ModbusApi.md#modbus_missions_guid_get) | **GET** /modbus/missions/{guid} | GET /modbus/missions/{guid}
[**modbus_missions_guid_put**](ModbusApi.md#modbus_missions_guid_put) | **PUT** /modbus/missions/{guid} | PUT /modbus/missions/{guid}
[**modbus_missions_post**](ModbusApi.md#modbus_missions_post) | **POST** /modbus/missions | POST /modbus/missions


# **modbus_get**
> GetModbus modbus_get(authorization, accept_language)

GET /modbus

Retrieve the modbus registers linked to actions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ModbusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /modbus
    api_response = api_instance.modbus_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModbusApi->modbus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetModbus**](GetModbus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_id_get**
> GetModbu modbus_id_get(authorization, accept_language, id)

GET /modbus/{id}

Retrieve the modbus registers linked to an action

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ModbusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 'id_example' # str | The id to search for

try:
    # GET /modbus/{id}
    api_response = api_instance.modbus_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModbusApi->modbus_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **str**| The id to search for | 

### Return type

[**GetModbu**](GetModbu.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_get**
> list[GetModbusMissions] modbus_missions_get(authorization, accept_language)

GET /modbus/missions

Retrieve the list of coils that can trigger a mission

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ModbusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /modbus/missions
    api_response = api_instance.modbus_missions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModbusApi->modbus_missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetModbusMissions]**](GetModbusMissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_guid_delete**
> modbus_missions_guid_delete(authorization, accept_language, guid)

DELETE /modbus/missions/{guid}

Delete the specified ID on the the modbus mission table

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ModbusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /modbus/missions/{guid}
    api_instance.modbus_missions_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling ModbusApi->modbus_missions_guid_delete: %s\n" % e)
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

# **modbus_missions_guid_get**
> GetModbusMission modbus_missions_guid_get(authorization, accept_language, guid)

GET /modbus/missions/{guid}

Retrieve the details about the mission linked with the coil

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ModbusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /modbus/missions/{guid}
    api_response = api_instance.modbus_missions_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModbusApi->modbus_missions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetModbusMission**](GetModbusMission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_guid_put**
> GetModbusMission modbus_missions_guid_put(authorization, accept_language, guid, modbus_mission)

PUT /modbus/missions/{guid}

Modify the values of the modbus mission with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ModbusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
modbus_mission = mir.PutModbusMission() # PutModbusMission | The new values of the modbus_mission

try:
    # PUT /modbus/missions/{guid}
    api_response = api_instance.modbus_missions_guid_put(authorization, accept_language, guid, modbus_mission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModbusApi->modbus_missions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **modbus_mission** | [**PutModbusMission**](PutModbusMission.md)| The new values of the modbus_mission | 

### Return type

[**GetModbusMission**](GetModbusMission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_post**
> GetModbusMissions modbus_missions_post(authorization, accept_language, modbus_missions)

POST /modbus/missions

Create a new link between a coil and a mission

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ModbusApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
modbus_missions = mir.PostModbusMissions() # PostModbusMissions | The details of the modbus_missions

try:
    # POST /modbus/missions
    api_response = api_instance.modbus_missions_post(authorization, accept_language, modbus_missions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModbusApi->modbus_missions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **modbus_missions** | [**PostModbusMissions**](PostModbusMissions.md)| The details of the modbus_missions | 

### Return type

[**GetModbusMissions**](GetModbusMissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

