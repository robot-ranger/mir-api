# mir.PositionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maps_map_id_positions_get**](PositionsApi.md#maps_map_id_positions_get) | **GET** /maps/{map_id}/positions | GET /maps/{map_id}/positions
[**path_guides_path_guide_guid_positions_get**](PositionsApi.md#path_guides_path_guide_guid_positions_get) | **GET** /path_guides/{path_guide_guid}/positions | GET /path_guides/{path_guide_guid}/positions
[**path_guides_path_guide_guid_positions_guid_delete**](PositionsApi.md#path_guides_path_guide_guid_positions_guid_delete) | **DELETE** /path_guides/{path_guide_guid}/positions/{guid} | DELETE /path_guides/{path_guide_guid}/positions/{guid}
[**path_guides_path_guide_guid_positions_guid_get**](PositionsApi.md#path_guides_path_guide_guid_positions_guid_get) | **GET** /path_guides/{path_guide_guid}/positions/{guid} | GET /path_guides/{path_guide_guid}/positions/{guid}
[**path_guides_path_guide_guid_positions_guid_put**](PositionsApi.md#path_guides_path_guide_guid_positions_guid_put) | **PUT** /path_guides/{path_guide_guid}/positions/{guid} | PUT /path_guides/{path_guide_guid}/positions/{guid}
[**path_guides_path_guide_guid_positions_post**](PositionsApi.md#path_guides_path_guide_guid_positions_post) | **POST** /path_guides/{path_guide_guid}/positions | POST /path_guides/{path_guide_guid}/positions
[**positions_get**](PositionsApi.md#positions_get) | **GET** /positions | GET /positions
[**positions_guid_delete**](PositionsApi.md#positions_guid_delete) | **DELETE** /positions/{guid} | DELETE /positions/{guid}
[**positions_guid_get**](PositionsApi.md#positions_guid_get) | **GET** /positions/{guid} | GET /positions/{guid}
[**positions_guid_put**](PositionsApi.md#positions_guid_put) | **PUT** /positions/{guid} | PUT /positions/{guid}
[**positions_parent_guid_helper_positions_get**](PositionsApi.md#positions_parent_guid_helper_positions_get) | **GET** /positions/{parent_guid}/helper_positions | GET /positions/{parent_guid}/helper_positions
[**positions_pos_id_docking_offsets_get**](PositionsApi.md#positions_pos_id_docking_offsets_get) | **GET** /positions/{pos_id}/docking_offsets | GET /positions/{pos_id}/docking_offsets
[**positions_post**](PositionsApi.md#positions_post) | **POST** /positions | POST /positions


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
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_id = 'map_id_example' # str | The map_id to search for

try:
    # GET /maps/{map_id}/positions
    api_response = api_instance.maps_map_id_positions_get(authorization, accept_language, map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->maps_map_id_positions_get: %s\n" % e)
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
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for

try:
    # GET /path_guides/{path_guide_guid}/positions
    api_response = api_instance.path_guides_path_guide_guid_positions_get(authorization, accept_language, path_guide_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->path_guides_path_guide_guid_positions_get: %s\n" % e)
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
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to delete
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /path_guides/{path_guide_guid}/positions/{guid}
    api_instance.path_guides_path_guide_guid_positions_guid_delete(authorization, accept_language, path_guide_guid, guid)
except ApiException as e:
    print("Exception when calling PositionsApi->path_guides_path_guide_guid_positions_guid_delete: %s\n" % e)
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
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for
guid = 'guid_example' # str | The guid to search for

try:
    # GET /path_guides/{path_guide_guid}/positions/{guid}
    api_response = api_instance.path_guides_path_guide_guid_positions_guid_get(authorization, accept_language, path_guide_guid, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->path_guides_path_guide_guid_positions_guid_get: %s\n" % e)
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
api_instance = mir.PositionsApi()
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
    print("Exception when calling PositionsApi->path_guides_path_guide_guid_positions_guid_put: %s\n" % e)
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
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to add the new resource to
path_guide_positions = mir.PostPathGuidePositions() # PostPathGuidePositions | The details of the path_guide_positions

try:
    # POST /path_guides/{path_guide_guid}/positions
    api_response = api_instance.path_guides_path_guide_guid_positions_post(authorization, accept_language, path_guide_guid, path_guide_positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->path_guides_path_guide_guid_positions_post: %s\n" % e)
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

# **positions_get**
> list[GetPositions] positions_get(authorization, accept_language)

GET /positions

Retrieve the list of positions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /positions
    api_response = api_instance.positions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetPositions]**](GetPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_guid_delete**
> positions_guid_delete(authorization, accept_language, guid)

DELETE /positions/{guid}

Erase the position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /positions/{guid}
    api_instance.positions_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_guid_delete: %s\n" % e)
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

# **positions_guid_get**
> GetPosition positions_guid_get(authorization, accept_language, guid)

GET /positions/{guid}

Retrieve the details about the position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /positions/{guid}
    api_response = api_instance.positions_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetPosition**](GetPosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_guid_put**
> GetPosition positions_guid_put(authorization, accept_language, guid, position)

PUT /positions/{guid}

Modify the values of the position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
position = mir.PutPosition() # PutPosition | The new values of the position

try:
    # PUT /positions/{guid}
    api_response = api_instance.positions_guid_put(authorization, accept_language, guid, position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **position** | [**PutPosition**](PutPosition.md)| The new values of the position | 

### Return type

[**GetPosition**](GetPosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_parent_guid_helper_positions_get**
> list[GetHelperPositions] positions_parent_guid_helper_positions_get(authorization, accept_language, parent_guid)

GET /positions/{parent_guid}/helper_positions

Retrieve the list of helper positions for the position with the specified parent GUID. Only Charging Stations, V markers, VL markers, Shelf and Trolley positions have helper positions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
parent_guid = 'parent_guid_example' # str | The parent_guid to search for

try:
    # GET /positions/{parent_guid}/helper_positions
    api_response = api_instance.positions_parent_guid_helper_positions_get(authorization, accept_language, parent_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_parent_guid_helper_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **parent_guid** | **str**| The parent_guid to search for | 

### Return type

[**list[GetHelperPositions]**](GetHelperPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_pos_id_docking_offsets_get**
> list[GetPosDockingOffsets] positions_pos_id_docking_offsets_get(authorization, accept_language, pos_id)

GET /positions/{pos_id}/docking_offsets

Retrieve the details of the docking offset of the position with the specified position ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
pos_id = 'pos_id_example' # str | The pos_id to search for

try:
    # GET /positions/{pos_id}/docking_offsets
    api_response = api_instance.positions_pos_id_docking_offsets_get(authorization, accept_language, pos_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_pos_id_docking_offsets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **pos_id** | **str**| The pos_id to search for | 

### Return type

[**list[GetPosDockingOffsets]**](GetPosDockingOffsets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_post**
> GetPositions positions_post(authorization, accept_language, positions)

POST /positions

Add a new position

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
positions = mir.PostPositions() # PostPositions | The details of the positions

try:
    # POST /positions
    api_response = api_instance.positions_post(authorization, accept_language, positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->positions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **positions** | [**PostPositions**](PostPositions.md)| The details of the positions | 

### Return type

[**GetPositions**](GetPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

