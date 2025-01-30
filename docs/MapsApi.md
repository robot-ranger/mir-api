# mir.MapsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maps_get**](MapsApi.md#maps_get) | **GET** /maps | GET /maps
[**maps_guid_delete**](MapsApi.md#maps_guid_delete) | **DELETE** /maps/{guid} | DELETE /maps/{guid}
[**maps_guid_get**](MapsApi.md#maps_guid_get) | **GET** /maps/{guid} | GET /maps/{guid}
[**maps_guid_put**](MapsApi.md#maps_guid_put) | **PUT** /maps/{guid} | PUT /maps/{guid}
[**maps_map_id_path_guides_get**](MapsApi.md#maps_map_id_path_guides_get) | **GET** /maps/{map_id}/path_guides | GET /maps/{map_id}/path_guides
[**maps_map_id_paths_get**](MapsApi.md#maps_map_id_paths_get) | **GET** /maps/{map_id}/paths | GET /maps/{map_id}/paths
[**maps_map_id_positions_get**](MapsApi.md#maps_map_id_positions_get) | **GET** /maps/{map_id}/positions | GET /maps/{map_id}/positions
[**maps_map_id_zones_get**](MapsApi.md#maps_map_id_zones_get) | **GET** /maps/{map_id}/zones | GET /maps/{map_id}/zones
[**maps_post**](MapsApi.md#maps_post) | **POST** /maps | POST /maps
[**maps_record_get**](MapsApi.md#maps_record_get) | **GET** /maps/record | GET /maps/record
[**maps_record_put**](MapsApi.md#maps_record_put) | **PUT** /maps/record | PUT /maps/record
[**maps_uploads_get**](MapsApi.md#maps_uploads_get) | **GET** /maps/uploads | GET /maps/uploads
[**maps_uploads_guid_delete**](MapsApi.md#maps_uploads_guid_delete) | **DELETE** /maps/uploads/{guid} | DELETE /maps/uploads/{guid}
[**maps_uploads_guid_get**](MapsApi.md#maps_uploads_guid_get) | **GET** /maps/uploads/{guid} | GET /maps/uploads/{guid}
[**maps_uploads_guid_post**](MapsApi.md#maps_uploads_guid_post) | **POST** /maps/uploads/{guid} | POST /maps/uploads/{guid}
[**maps_uploads_post**](MapsApi.md#maps_uploads_post) | **POST** /maps/uploads | POST /maps/uploads
[**sessions_session_id_maps_get**](MapsApi.md#sessions_session_id_maps_get) | **GET** /sessions/{session_id}/maps | GET /sessions/{session_id}/maps


# **maps_get**
> list[GetMaps] maps_get(authorization, accept_language)

GET /maps

Retrieve the list of maps

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /maps
    api_response = api_instance.maps_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetMaps]**](GetMaps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_guid_delete**
> maps_guid_delete(authorization, accept_language, guid)

DELETE /maps/{guid}

Erase the map with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /maps/{guid}
    api_instance.maps_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling MapsApi->maps_guid_delete: %s\n" % e)
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

# **maps_guid_get**
> GetMap maps_guid_get(authorization, accept_language, guid)

GET /maps/{guid}

Retrieve the details about the map with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /maps/{guid}
    api_response = api_instance.maps_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetMap**](GetMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_guid_put**
> GetMap maps_guid_put(authorization, accept_language, guid, map)

PUT /maps/{guid}

Modify the values of the map with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
map = mir.PutMap() # PutMap | The new values of the map

try:
    # PUT /maps/{guid}
    api_response = api_instance.maps_guid_put(authorization, accept_language, guid, map)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **map** | [**PutMap**](PutMap.md)| The new values of the map | 

### Return type

[**GetMap**](GetMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_map_id_path_guides_get**
> list[GetMapPathGuides] maps_map_id_path_guides_get(authorization, accept_language, map_id)

GET /maps/{map_id}/path_guides

Retrieve the list of path guides that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/path_guides
    api_response = api_instance.maps_map_id_path_guides_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_map_id_path_guides_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **map_id** | **str**| The map_id to search for | 

### Return type

[**list[GetMapPathGuides]**](GetMapPathGuides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_map_id_paths_get**
> list[GetMapPaths] maps_map_id_paths_get(authorization, accept_language, map_id)

GET /maps/{map_id}/paths

Retrieve the list of paths that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/paths
    api_response = api_instance.maps_map_id_paths_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_map_id_paths_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **map_id** | **str**| The map_id to search for | 

### Return type

[**list[GetMapPaths]**](GetMapPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_map_id_positions_get**
> list[GetMapPositions] maps_map_id_positions_get(authorization, accept_language, map_id)

GET /maps/{map_id}/positions

Retrieve the list of positions that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/positions
    api_response = api_instance.maps_map_id_positions_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_map_id_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **map_id** | **str**| The map_id to search for | 

### Return type

[**list[GetMapPositions]**](GetMapPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/zones
    api_response = api_instance.maps_map_id_zones_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_map_id_zones_get: %s\n" % e)
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

# **maps_post**
> GetMaps maps_post(authorization, accept_language, maps)

POST /maps

Add a new map

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
maps = mir.PostMaps() # PostMaps | The details of the maps

try:
    # POST /maps
    api_response = api_instance.maps_post(authorization, accept_language, maps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **maps** | [**PostMaps**](PostMaps.md)| The details of the maps | 

### Return type

[**GetMaps**](GetMaps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_record_get**
> GetMapRecord maps_record_get(authorization, accept_language)

GET /maps/record

Retrive the latest recording of a map

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /maps/record
    api_response = api_instance.maps_record_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetMapRecord**](GetMapRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_record_put**
> GetMapRecord maps_record_put(authorization, accept_language, map_record)

PUT /maps/record

Start and stop the recording of a map

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_record = mir.PutMapRecord() # PutMapRecord | The new values of the map_record

try:
    # PUT /maps/record
    api_response = api_instance.maps_record_put(authorization, accept_language, map_record)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_record_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **map_record** | [**PutMapRecord**](PutMapRecord.md)| The new values of the map_record | 

### Return type

[**GetMapRecord**](GetMapRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_uploads_get**
> list[GetMapUploads] maps_uploads_get(authorization, accept_language)

GET /maps/uploads

Retrieve the list of map uploads

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /maps/uploads
    api_response = api_instance.maps_uploads_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_uploads_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetMapUploads]**](GetMapUploads.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_uploads_guid_delete**
> maps_uploads_guid_delete(authorization, accept_language, guid)

DELETE /maps/uploads/{guid}

Delete map upload

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /maps/uploads/{guid}
    api_instance.maps_uploads_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling MapsApi->maps_uploads_guid_delete: %s\n" % e)
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

# **maps_uploads_guid_get**
> GetMapUpload maps_uploads_guid_get(authorization, accept_language, guid)

GET /maps/uploads/{guid}

Fetch map upload

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /maps/uploads/{guid}
    api_response = api_instance.maps_uploads_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_uploads_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetMapUpload**](GetMapUpload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_uploads_guid_post**
> GetMapUpload maps_uploads_guid_post(authorization, accept_language, guid, map_upload)

POST /maps/uploads/{guid}

Apply map upload

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to
map_upload = mir.PostMapUpload() # PostMapUpload | The details of the map_upload

try:
    # POST /maps/uploads/{guid}
    api_response = api_instance.maps_uploads_guid_post(authorization, accept_language, guid, map_upload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_uploads_guid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to add the new resource to | 
 **map_upload** | [**PostMapUpload**](PostMapUpload.md)| The details of the map_upload | 

### Return type

[**GetMapUpload**](GetMapUpload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_uploads_post**
> GetMapUploads maps_uploads_post(authorization, accept_language, map_uploads)

POST /maps/uploads

Upload a new map

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_uploads = mir.PostMapUploads() # PostMapUploads | The details of the map_uploads

try:
    # POST /maps/uploads
    api_response = api_instance.maps_uploads_post(authorization, accept_language, map_uploads)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->maps_uploads_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **map_uploads** | [**PostMapUploads**](PostMapUploads.md)| The details of the map_uploads | 

### Return type

[**GetMapUploads**](GetMapUploads.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_maps_get**
> list[GetSessionMaps] sessions_session_id_maps_get(authorization, accept_language, session_id)

GET /sessions/{session_id}/maps

Retrieve the list of maps that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MapsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/maps
    api_response = api_instance.sessions_session_id_maps_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->sessions_session_id_maps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **session_id** | **str**| The session_id to search for | 

### Return type

[**list[GetSessionMaps]**](GetSessionMaps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

