# mir.ZonesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maps_map_id_zones_get**](ZonesApi.md#maps_map_id_zones_get) | **GET** /maps/{map_id}/zones | GET /maps/{map_id}/zones
[**zones_action_definitions_action_type_get**](ZonesApi.md#zones_action_definitions_action_type_get) | **GET** /zones/action_definitions/{action_type} | GET /zones/action_definitions/{action_type}
[**zones_action_definitions_get**](ZonesApi.md#zones_action_definitions_get) | **GET** /zones/action_definitions | GET /zones/action_definitions
[**zones_definitions_get**](ZonesApi.md#zones_definitions_get) | **GET** /zones/definitions | GET /zones/definitions
[**zones_get**](ZonesApi.md#zones_get) | **GET** /zones | GET /zones
[**zones_guid_delete**](ZonesApi.md#zones_guid_delete) | **DELETE** /zones/{guid} | DELETE /zones/{guid}
[**zones_guid_get**](ZonesApi.md#zones_guid_get) | **GET** /zones/{guid} | GET /zones/{guid}
[**zones_guid_put**](ZonesApi.md#zones_guid_put) | **PUT** /zones/{guid} | PUT /zones/{guid}
[**zones_post**](ZonesApi.md#zones_post) | **POST** /zones | POST /zones


# **maps_map_id_zones_get**
> list[GetMapZone] maps_map_id_zones_get(authorization, accept_language, map_id)

GET /maps/{map_id}/zones

Retrieve the list of zones that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/zones
    api_response = api_instance.maps_map_id_zones_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->maps_map_id_zones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **map_id** | **str**| The map_id to search for | 

### Return type

[**list[GetMapZone]**](GetMapZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_action_definitions_action_type_get**
> GetZoneActionDefinition zones_action_definitions_action_type_get(authorization, accept_language, action_type)

GET /zones/action_definitions/{action_type}

Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
action_type = 'action_type_example' # str | The action_type to search for

try:
    # GET /zones/action_definitions/{action_type}
    api_response = api_instance.zones_action_definitions_action_type_get(authorization, accept_language, action_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_action_definitions_action_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **action_type** | **str**| The action_type to search for | 

### Return type

[**GetZoneActionDefinition**](GetZoneActionDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_action_definitions_get**
> GetZoneActionDefinitions zones_action_definitions_get(authorization, accept_language)

GET /zones/action_definitions

Retrieve definitions of zone actions and their parameters

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /zones/action_definitions
    api_response = api_instance.zones_action_definitions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_action_definitions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetZoneActionDefinitions**](GetZoneActionDefinitions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_definitions_get**
> GetZonesDefinitions zones_definitions_get(authorization, accept_language)

GET /zones/definitions

Retrieve definitions of zones and their actions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /zones/definitions
    api_response = api_instance.zones_definitions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_definitions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetZonesDefinitions**](GetZonesDefinitions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_get**
> list[GetZones] zones_get(authorization, accept_language)

GET /zones

Retrieve the list of zones

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /zones
    api_response = api_instance.zones_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetZones]**](GetZones.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_guid_delete**
> zones_guid_delete(authorization, accept_language, guid)

DELETE /zones/{guid}

Erase the zone with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /zones/{guid}
    api_instance.zones_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_guid_delete: %s\n" % e)
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

# **zones_guid_get**
> GetZone zones_guid_get(authorization, accept_language, guid)

GET /zones/{guid}

Retrieve the details about the zone with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /zones/{guid}
    api_response = api_instance.zones_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetZone**](GetZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_guid_put**
> GetZone zones_guid_put(authorization, accept_language, guid, zone)

PUT /zones/{guid}

Modify the values of the zone with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
zone = mir.PutZone() # PutZone | The new values of the zone

try:
    # PUT /zones/{guid}
    api_response = api_instance.zones_guid_put(authorization, accept_language, guid, zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **zone** | [**PutZone**](PutZone.md)| The new values of the zone | 

### Return type

[**GetZone**](GetZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_post**
> GetZones zones_post(authorization, accept_language, zones)

POST /zones

Add a new zone

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ZonesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
zones = mir.PostZones() # PostZones | The details of the zones

try:
    # POST /zones
    api_response = api_instance.zones_post(authorization, accept_language, zones)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->zones_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **zones** | [**PostZones**](PostZones.md)| The details of the zones | 

### Return type

[**GetZones**](GetZones.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

