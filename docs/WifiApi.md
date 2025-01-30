# mir.WifiApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wifi_connections_get**](WifiApi.md#wifi_connections_get) | **GET** /wifi/connections | GET /wifi/connections
[**wifi_connections_post**](WifiApi.md#wifi_connections_post) | **POST** /wifi/connections | POST /wifi/connections
[**wifi_connections_uuid_delete**](WifiApi.md#wifi_connections_uuid_delete) | **DELETE** /wifi/connections/{uuid} | DELETE /wifi/connections/{uuid}
[**wifi_connections_uuid_get**](WifiApi.md#wifi_connections_uuid_get) | **GET** /wifi/connections/{uuid} | GET /wifi/connections/{uuid}
[**wifi_connections_uuid_post**](WifiApi.md#wifi_connections_uuid_post) | **POST** /wifi/connections/{uuid} | POST /wifi/connections/{uuid}
[**wifi_get**](WifiApi.md#wifi_get) | **GET** /wifi | GET /wifi
[**wifi_networks_get**](WifiApi.md#wifi_networks_get) | **GET** /wifi/networks | GET /wifi/networks
[**wifi_networks_guid_get**](WifiApi.md#wifi_networks_guid_get) | **GET** /wifi/networks/{guid} | GET /wifi/networks/{guid}


# **wifi_connections_get**
> list[GetWifiConnections] wifi_connections_get(authorization, accept_language)

GET /wifi/connections

Retrieve the list of WiFi networks already configured

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /wifi/connections
    api_response = api_instance.wifi_connections_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_connections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetWifiConnections]**](GetWifiConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_post**
> GetWifiConnections wifi_connections_post(authorization, accept_language, wifi_connections)

POST /wifi/connections

Add a new WiFi network configuration

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
wifi_connections = mir.PostWifiConnections() # PostWifiConnections | The details of the wifi_connections

try:
    # POST /wifi/connections
    api_response = api_instance.wifi_connections_post(authorization, accept_language, wifi_connections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_connections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **wifi_connections** | [**PostWifiConnections**](PostWifiConnections.md)| The details of the wifi_connections | 

### Return type

[**GetWifiConnections**](GetWifiConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_uuid_delete**
> wifi_connections_uuid_delete(authorization, accept_language, uuid)

DELETE /wifi/connections/{uuid}

Erase the WiFi network configuration with the specified UUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
uuid = 'uuid_example' # str | The uuid to delete

try:
    # DELETE /wifi/connections/{uuid}
    api_instance.wifi_connections_uuid_delete(authorization, accept_language, uuid)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_connections_uuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **uuid** | **str**| The uuid to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_uuid_get**
> GetWifiConnection wifi_connections_uuid_get(authorization, accept_language, uuid)

GET /wifi/connections/{uuid}

Retrieve the details about the WiFi network configuration with the specified UUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
uuid = 'uuid_example' # str | The uuid to search for

try:
    # GET /wifi/connections/{uuid}
    api_response = api_instance.wifi_connections_uuid_get(authorization, accept_language, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_connections_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **uuid** | **str**| The uuid to search for | 

### Return type

[**GetWifiConnection**](GetWifiConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_uuid_post**
> GetWifiConnection wifi_connections_uuid_post(authorization, accept_language, uuid, wifi_connection)

POST /wifi/connections/{uuid}

Connect to the network with the specified UUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
uuid = 'uuid_example' # str | The uuid to add the new resource to
wifi_connection = mir.PostWifiConnection() # PostWifiConnection | The details of the wifi_connection

try:
    # POST /wifi/connections/{uuid}
    api_response = api_instance.wifi_connections_uuid_post(authorization, accept_language, uuid, wifi_connection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_connections_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **uuid** | **str**| The uuid to add the new resource to | 
 **wifi_connection** | [**PostWifiConnection**](PostWifiConnection.md)| The details of the wifi_connection | 

### Return type

[**GetWifiConnection**](GetWifiConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_get**
> GetWifiApi wifi_get(authorization, accept_language)

GET /wifi

Retrive the list of WIFI API endpoints.

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /wifi
    api_response = api_instance.wifi_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetWifiApi**](GetWifiApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_networks_get**
> list[GetWifiNetworks] wifi_networks_get(authorization, accept_language)

GET /wifi/networks

Retrieve the list of WiFi networks available for the robot to connect

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /wifi/networks
    api_response = api_instance.wifi_networks_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetWifiNetworks]**](GetWifiNetworks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_networks_guid_get**
> GetWifiNetwork wifi_networks_guid_get(authorization, accept_language, guid)

GET /wifi/networks/{guid}

Retrieve the details about the WiFi network with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WifiApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /wifi/networks/{guid}
    api_response = api_instance.wifi_networks_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WifiApi->wifi_networks_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetWifiNetwork**](GetWifiNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

