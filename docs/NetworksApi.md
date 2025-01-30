# mir.NetworksApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wifi_networks_get**](NetworksApi.md#wifi_networks_get) | **GET** /wifi/networks | GET /wifi/networks
[**wifi_networks_guid_get**](NetworksApi.md#wifi_networks_guid_get) | **GET** /wifi/networks/{guid} | GET /wifi/networks/{guid}


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
api_instance = mir.NetworksApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /wifi/networks
    api_response = api_instance.wifi_networks_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->wifi_networks_get: %s\n" % e)
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
api_instance = mir.NetworksApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /wifi/networks/{guid}
    api_response = api_instance.wifi_networks_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->wifi_networks_guid_get: %s\n" % e)
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

