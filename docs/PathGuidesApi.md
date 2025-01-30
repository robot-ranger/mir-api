# mir.PathGuidesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maps_map_id_path_guides_get**](PathGuidesApi.md#maps_map_id_path_guides_get) | **GET** /maps/{map_id}/path_guides | GET /maps/{map_id}/path_guides
[**path_guides_get**](PathGuidesApi.md#path_guides_get) | **GET** /path_guides | GET /path_guides
[**path_guides_guid_delete**](PathGuidesApi.md#path_guides_guid_delete) | **DELETE** /path_guides/{guid} | DELETE /path_guides/{guid}
[**path_guides_guid_get**](PathGuidesApi.md#path_guides_guid_get) | **GET** /path_guides/{guid} | GET /path_guides/{guid}
[**path_guides_guid_put**](PathGuidesApi.md#path_guides_guid_put) | **PUT** /path_guides/{guid} | PUT /path_guides/{guid}
[**path_guides_path_guide_guid_options_get**](PathGuidesApi.md#path_guides_path_guide_guid_options_get) | **GET** /path_guides/{path_guide_guid}/options | GET /path_guides/{path_guide_guid}/options
[**path_guides_path_guide_guid_positions_get**](PathGuidesApi.md#path_guides_path_guide_guid_positions_get) | **GET** /path_guides/{path_guide_guid}/positions | GET /path_guides/{path_guide_guid}/positions
[**path_guides_path_guide_guid_positions_guid_delete**](PathGuidesApi.md#path_guides_path_guide_guid_positions_guid_delete) | **DELETE** /path_guides/{path_guide_guid}/positions/{guid} | DELETE /path_guides/{path_guide_guid}/positions/{guid}
[**path_guides_path_guide_guid_positions_guid_get**](PathGuidesApi.md#path_guides_path_guide_guid_positions_guid_get) | **GET** /path_guides/{path_guide_guid}/positions/{guid} | GET /path_guides/{path_guide_guid}/positions/{guid}
[**path_guides_path_guide_guid_positions_guid_put**](PathGuidesApi.md#path_guides_path_guide_guid_positions_guid_put) | **PUT** /path_guides/{path_guide_guid}/positions/{guid} | PUT /path_guides/{path_guide_guid}/positions/{guid}
[**path_guides_path_guide_guid_positions_post**](PathGuidesApi.md#path_guides_path_guide_guid_positions_post) | **POST** /path_guides/{path_guide_guid}/positions | POST /path_guides/{path_guide_guid}/positions
[**path_guides_post**](PathGuidesApi.md#path_guides_post) | **POST** /path_guides | POST /path_guides


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
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/path_guides
    api_response = api_instance.maps_map_id_path_guides_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->maps_map_id_path_guides_get: %s\n" % e)
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

# **path_guides_get**
> list[GetPathGuides] path_guides_get(authorization, accept_language)

GET /path_guides

Retrieve the list of path guides

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /path_guides
    api_response = api_instance.path_guides_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetPathGuides]**](GetPathGuides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_guid_delete**
> path_guides_guid_delete(authorization, accept_language, guid)

DELETE /path_guides/{guid}

Erase the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /path_guides/{guid}
    api_instance.path_guides_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_guid_delete: %s\n" % e)
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

# **path_guides_guid_get**
> GetPathGuide path_guides_guid_get(authorization, accept_language, guid)

GET /path_guides/{guid}

Retrieve the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /path_guides/{guid}
    api_response = api_instance.path_guides_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetPathGuide**](GetPathGuide.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_guid_put**
> GetPathGuide path_guides_guid_put(authorization, accept_language, guid, path_guide)

PUT /path_guides/{guid}

Modify the values of the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
path_guide = mir.PutPathGuide() # PutPathGuide | The new values of the path_guide

try:
    # PUT /path_guides/{guid}
    api_response = api_instance.path_guides_guid_put(authorization, accept_language, guid, path_guide)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **path_guide** | [**PutPathGuide**](PutPathGuide.md)| The new values of the path_guide | 

### Return type

[**GetPathGuide**](GetPathGuide.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_options_get**
> GetPathGuideOptions path_guides_path_guide_guid_options_get(authorization, accept_language, path_guide_guid)

GET /path_guides/{path_guide_guid}/options

Retrieve the list of allowed start/via/goal options for the selected path guide

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for

try:
    # GET /path_guides/{path_guide_guid}/options
    api_response = api_instance.path_guides_path_guide_guid_options_get(authorization, accept_language, path_guide_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_path_guide_guid_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guide_guid** | **str**| The path_guide_guid to search for | 

### Return type

[**GetPathGuideOptions**](GetPathGuideOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_get**
> list[GetPathGuidePositions] path_guides_path_guide_guid_positions_get(authorization, accept_language, path_guide_guid)

GET /path_guides/{path_guide_guid}/positions

Retrieve the list of positions for the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for

try:
    # GET /path_guides/{path_guide_guid}/positions
    api_response = api_instance.path_guides_path_guide_guid_positions_get(authorization, accept_language, path_guide_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_path_guide_guid_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guide_guid** | **str**| The path_guide_guid to search for | 

### Return type

[**list[GetPathGuidePositions]**](GetPathGuidePositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_guid_delete**
> path_guides_path_guide_guid_positions_guid_delete(authorization, accept_language, path_guide_guid, guid)

DELETE /path_guides/{path_guide_guid}/positions/{guid}

Erase the position with the specified GUID from the path guide with the specified path guide GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to delete
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /path_guides/{path_guide_guid}/positions/{guid}
    api_instance.path_guides_path_guide_guid_positions_guid_delete(authorization, accept_language, path_guide_guid, guid)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_path_guide_guid_positions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guide_guid** | **str**| The path_guide_guid to delete | 
 **guid** | **str**| The guid to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_guid_get**
> GetPathGuidePosition path_guides_path_guide_guid_positions_guid_get(authorization, accept_language, path_guide_guid, guid)

GET /path_guides/{path_guide_guid}/positions/{guid}

Retrieve the position with the specified GUID from the path guide with the specified path guide GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for
guid = 'guid_example' # str | The guid to search for

try:
    # GET /path_guides/{path_guide_guid}/positions/{guid}
    api_response = api_instance.path_guides_path_guide_guid_positions_guid_get(authorization, accept_language, path_guide_guid, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_path_guide_guid_positions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guide_guid** | **str**| The path_guide_guid to search for | 
 **guid** | **str**| The guid to search for | 

### Return type

[**GetPathGuidePosition**](GetPathGuidePosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_guid_put**
> GetPathGuidePosition path_guides_path_guide_guid_positions_guid_put(authorization, accept_language, path_guide_guid, guid, path_guide_position)

PUT /path_guides/{path_guide_guid}/positions/{guid}

Modify the values of the position with the specified GUID from the path guide with the specified path guide GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to modify
guid = 'guid_example' # str | The guid to modify
path_guide_position = mir.PutPathGuidePosition() # PutPathGuidePosition | The new values of the path_guide_position

try:
    # PUT /path_guides/{path_guide_guid}/positions/{guid}
    api_response = api_instance.path_guides_path_guide_guid_positions_guid_put(authorization, accept_language, path_guide_guid, guid, path_guide_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_path_guide_guid_positions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guide_guid** | **str**| The path_guide_guid to modify | 
 **guid** | **str**| The guid to modify | 
 **path_guide_position** | [**PutPathGuidePosition**](PutPathGuidePosition.md)| The new values of the path_guide_position | 

### Return type

[**GetPathGuidePosition**](GetPathGuidePosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_post**
> GetPathGuidePositions path_guides_path_guide_guid_positions_post(authorization, accept_language, path_guide_guid, path_guide_positions)

POST /path_guides/{path_guide_guid}/positions

Add a new position to the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to add the new resource to
path_guide_positions = mir.PostPathGuidePositions() # PostPathGuidePositions | The details of the path_guide_positions

try:
    # POST /path_guides/{path_guide_guid}/positions
    api_response = api_instance.path_guides_path_guide_guid_positions_post(authorization, accept_language, path_guide_guid, path_guide_positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_path_guide_guid_positions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guide_guid** | **str**| The path_guide_guid to add the new resource to | 
 **path_guide_positions** | [**PostPathGuidePositions**](PostPathGuidePositions.md)| The details of the path_guide_positions | 

### Return type

[**GetPathGuidePositions**](GetPathGuidePositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_post**
> GetPathGuides path_guides_post(authorization, accept_language, path_guides)

POST /path_guides

Add a new path guide

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guides = mir.PostPathGuides() # PostPathGuides | The details of the path_guides

try:
    # POST /path_guides
    api_response = api_instance.path_guides_post(authorization, accept_language, path_guides)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesApi->path_guides_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guides** | [**PostPathGuides**](PostPathGuides.md)| The details of the path_guides | 

### Return type

[**GetPathGuides**](GetPathGuides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

