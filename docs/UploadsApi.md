# mir.UploadsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maps_uploads_get**](UploadsApi.md#maps_uploads_get) | **GET** /maps/uploads | GET /maps/uploads
[**maps_uploads_guid_delete**](UploadsApi.md#maps_uploads_guid_delete) | **DELETE** /maps/uploads/{guid} | DELETE /maps/uploads/{guid}
[**maps_uploads_guid_get**](UploadsApi.md#maps_uploads_guid_get) | **GET** /maps/uploads/{guid} | GET /maps/uploads/{guid}
[**maps_uploads_guid_post**](UploadsApi.md#maps_uploads_guid_post) | **POST** /maps/uploads/{guid} | POST /maps/uploads/{guid}
[**maps_uploads_post**](UploadsApi.md#maps_uploads_post) | **POST** /maps/uploads | POST /maps/uploads


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
api_instance = mir.UploadsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /maps/uploads
    api_response = api_instance.maps_uploads_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->maps_uploads_get: %s\n" % e)
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
api_instance = mir.UploadsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /maps/uploads/{guid}
    api_instance.maps_uploads_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling UploadsApi->maps_uploads_guid_delete: %s\n" % e)
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
api_instance = mir.UploadsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /maps/uploads/{guid}
    api_response = api_instance.maps_uploads_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->maps_uploads_guid_get: %s\n" % e)
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
api_instance = mir.UploadsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to
map_upload = mir.PostMapUpload() # PostMapUpload | The details of the map_upload

try:
    # POST /maps/uploads/{guid}
    api_response = api_instance.maps_uploads_guid_post(authorization, accept_language, guid, map_upload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->maps_uploads_guid_post: %s\n" % e)
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
api_instance = mir.UploadsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
map_uploads = mir.PostMapUploads() # PostMapUploads | The details of the map_uploads

try:
    # POST /maps/uploads
    api_response = api_instance.maps_uploads_post(authorization, accept_language, map_uploads)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadsApi->maps_uploads_post: %s\n" % e)
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

