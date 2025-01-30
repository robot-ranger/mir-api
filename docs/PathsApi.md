# mir.PathsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maps_map_id_paths_get**](PathsApi.md#maps_map_id_paths_get) | **GET** /maps/{map_id}/paths | GET /maps/{map_id}/paths
[**paths_get**](PathsApi.md#paths_get) | **GET** /paths | GET /paths
[**paths_guid_delete**](PathsApi.md#paths_guid_delete) | **DELETE** /paths/{guid} | DELETE /paths/{guid}
[**paths_guid_get**](PathsApi.md#paths_guid_get) | **GET** /paths/{guid} | GET /paths/{guid}
[**paths_guid_put**](PathsApi.md#paths_guid_put) | **PUT** /paths/{guid} | PUT /paths/{guid}
[**paths_post**](PathsApi.md#paths_post) | **POST** /paths | POST /paths


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
api_instance = mir.PathsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/paths
    api_response = api_instance.maps_map_id_paths_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathsApi->maps_map_id_paths_get: %s\n" % e)
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

# **paths_get**
> list[GetPaths] paths_get(authorization, accept_language)

GET /paths

Retrieve the list of paths

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /paths
    api_response = api_instance.paths_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathsApi->paths_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetPaths]**](GetPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_guid_delete**
> paths_guid_delete(authorization, accept_language, guid)

DELETE /paths/{guid}

Erase the path with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /paths/{guid}
    api_instance.paths_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling PathsApi->paths_guid_delete: %s\n" % e)
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

# **paths_guid_get**
> GetPath paths_guid_get(authorization, accept_language, guid)

GET /paths/{guid}

Retrieve the path with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /paths/{guid}
    api_response = api_instance.paths_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathsApi->paths_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetPath**](GetPath.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_guid_put**
> GetPath paths_guid_put(authorization, accept_language, guid, path)

PUT /paths/{guid}

Modify the values of the path with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
path = mir.PutPath() # PutPath | The new values of the path

try:
    # PUT /paths/{guid}
    api_response = api_instance.paths_guid_put(authorization, accept_language, guid, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathsApi->paths_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **path** | [**PutPath**](PutPath.md)| The new values of the path | 

### Return type

[**GetPath**](GetPath.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_post**
> GetPaths paths_post(authorization, accept_language, paths)

POST /paths

Add a new path

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
paths = mir.PostPaths() # PostPaths | The details of the paths

try:
    # POST /paths
    api_response = api_instance.paths_post(authorization, accept_language, paths)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathsApi->paths_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **paths** | [**PostPaths**](PostPaths.md)| The details of the paths | 

### Return type

[**GetPaths**](GetPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

