# mir.PathGuidesPositionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**path_guides_positions_get**](PathGuidesPositionsApi.md#path_guides_positions_get) | **GET** /path_guides_positions | GET /path_guides_positions
[**path_guides_positions_guid_delete**](PathGuidesPositionsApi.md#path_guides_positions_guid_delete) | **DELETE** /path_guides_positions/{guid} | DELETE /path_guides_positions/{guid}
[**path_guides_positions_guid_get**](PathGuidesPositionsApi.md#path_guides_positions_guid_get) | **GET** /path_guides_positions/{guid} | GET /path_guides_positions/{guid}
[**path_guides_positions_guid_put**](PathGuidesPositionsApi.md#path_guides_positions_guid_put) | **PUT** /path_guides_positions/{guid} | PUT /path_guides_positions/{guid}
[**path_guides_positions_post**](PathGuidesPositionsApi.md#path_guides_positions_post) | **POST** /path_guides_positions | POST /path_guides_positions


# **path_guides_positions_get**
> list[GetPathGuidesPositions] path_guides_positions_get(authorization, accept_language)

GET /path_guides_positions

Retrieve the list of positions used for path guides

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesPositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /path_guides_positions
    api_response = api_instance.path_guides_positions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesPositionsApi->path_guides_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetPathGuidesPositions]**](GetPathGuidesPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_guid_delete**
> path_guides_positions_guid_delete(authorization, accept_language, guid)

DELETE /path_guides_positions/{guid}

Erase the path guide position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesPositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /path_guides_positions/{guid}
    api_instance.path_guides_positions_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling PathGuidesPositionsApi->path_guides_positions_guid_delete: %s\n" % e)
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

# **path_guides_positions_guid_get**
> GetPathGuidesPosition path_guides_positions_guid_get(authorization, accept_language, guid)

GET /path_guides_positions/{guid}

Retrieve the position for path guides with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesPositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /path_guides_positions/{guid}
    api_response = api_instance.path_guides_positions_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesPositionsApi->path_guides_positions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetPathGuidesPosition**](GetPathGuidesPosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_guid_put**
> GetPathGuidesPosition path_guides_positions_guid_put(authorization, accept_language, guid, path_guides_position)

PUT /path_guides_positions/{guid}

Modify the values of the position for path guides with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesPositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
path_guides_position = mir.PutPathGuidesPosition() # PutPathGuidesPosition | The new values of the path_guides_position

try:
    # PUT /path_guides_positions/{guid}
    api_response = api_instance.path_guides_positions_guid_put(authorization, accept_language, guid, path_guides_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesPositionsApi->path_guides_positions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **path_guides_position** | [**PutPathGuidesPosition**](PutPathGuidesPosition.md)| The new values of the path_guides_position | 

### Return type

[**GetPathGuidesPosition**](GetPathGuidesPosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_post**
> GetPathGuidesPositions path_guides_positions_post(authorization, accept_language, path_guides_positions)

POST /path_guides_positions

Add a new position in a path guide

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PathGuidesPositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
path_guides_positions = mir.PostPathGuidesPositions() # PostPathGuidesPositions | The details of the path_guides_positions

try:
    # POST /path_guides_positions
    api_response = api_instance.path_guides_positions_post(authorization, accept_language, path_guides_positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathGuidesPositionsApi->path_guides_positions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **path_guides_positions** | [**PostPathGuidesPositions**](PostPathGuidesPositions.md)| The details of the path_guides_positions | 

### Return type

[**GetPathGuidesPositions**](GetPathGuidesPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

