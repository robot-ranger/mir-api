# mir.DockingOffsetsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docking_offsets_get**](DockingOffsetsApi.md#docking_offsets_get) | **GET** /docking_offsets | GET /docking_offsets
[**docking_offsets_guid_delete**](DockingOffsetsApi.md#docking_offsets_guid_delete) | **DELETE** /docking_offsets/{guid} | DELETE /docking_offsets/{guid}
[**docking_offsets_guid_get**](DockingOffsetsApi.md#docking_offsets_guid_get) | **GET** /docking_offsets/{guid} | GET /docking_offsets/{guid}
[**docking_offsets_guid_put**](DockingOffsetsApi.md#docking_offsets_guid_put) | **PUT** /docking_offsets/{guid} | PUT /docking_offsets/{guid}
[**docking_offsets_post**](DockingOffsetsApi.md#docking_offsets_post) | **POST** /docking_offsets | POST /docking_offsets
[**docking_offsets_shelfs_get**](DockingOffsetsApi.md#docking_offsets_shelfs_get) | **GET** /docking_offsets/shelfs | GET /docking_offsets/shelfs
[**docking_offsets_types_get**](DockingOffsetsApi.md#docking_offsets_types_get) | **GET** /docking_offsets/types | GET /docking_offsets/types
[**docking_offsets_types_id_get**](DockingOffsetsApi.md#docking_offsets_types_id_get) | **GET** /docking_offsets/types/{id} | GET /docking_offsets/types/{id}
[**positions_pos_id_docking_offsets_get**](DockingOffsetsApi.md#positions_pos_id_docking_offsets_get) | **GET** /positions/{pos_id}/docking_offsets | GET /positions/{pos_id}/docking_offsets


# **docking_offsets_get**
> list[GetDockingOffsets] docking_offsets_get(authorization, accept_language)

GET /docking_offsets

Retrieve the list of docking offsets

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /docking_offsets
    api_response = api_instance.docking_offsets_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetDockingOffsets]**](GetDockingOffsets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_guid_delete**
> docking_offsets_guid_delete(authorization, accept_language, guid)

DELETE /docking_offsets/{guid}

Erase the docking offset with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /docking_offsets/{guid}
    api_instance.docking_offsets_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_guid_delete: %s\n" % e)
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

# **docking_offsets_guid_get**
> GetDockingOffset docking_offsets_guid_get(authorization, accept_language, guid)

GET /docking_offsets/{guid}

Retrieve the details of the docking offset with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /docking_offsets/{guid}
    api_response = api_instance.docking_offsets_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetDockingOffset**](GetDockingOffset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_guid_put**
> GetDockingOffset docking_offsets_guid_put(authorization, accept_language, guid, docking_offset)

PUT /docking_offsets/{guid}

Modify the values of the docking offset with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
docking_offset = mir.PutDockingOffset() # PutDockingOffset | The new values of the docking_offset

try:
    # PUT /docking_offsets/{guid}
    api_response = api_instance.docking_offsets_guid_put(authorization, accept_language, guid, docking_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **docking_offset** | [**PutDockingOffset**](PutDockingOffset.md)| The new values of the docking_offset | 

### Return type

[**GetDockingOffset**](GetDockingOffset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_post**
> GetDockingOffsets docking_offsets_post(authorization, accept_language, docking_offsets)

POST /docking_offsets

Add a new docking offset. The only positions that can have docking offsets are Charging stations, V markers and VL markers

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
docking_offsets = mir.PostDockingOffsets() # PostDockingOffsets | The details of the docking_offsets

try:
    # POST /docking_offsets
    api_response = api_instance.docking_offsets_post(authorization, accept_language, docking_offsets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **docking_offsets** | [**PostDockingOffsets**](PostDockingOffsets.md)| The details of the docking_offsets | 

### Return type

[**GetDockingOffsets**](GetDockingOffsets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_shelfs_get**
> list[GetDockingOffsetsNoPos] docking_offsets_shelfs_get(authorization, accept_language)

GET /docking_offsets/shelfs

Retrieve the list of docking offsets

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /docking_offsets/shelfs
    api_response = api_instance.docking_offsets_shelfs_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_shelfs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetDockingOffsetsNoPos]**](GetDockingOffsetsNoPos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_types_get**
> list[GetDockingOffsetTypes] docking_offsets_types_get(authorization, accept_language)

GET /docking_offsets/types

Retrieve a list of possible position types

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /docking_offsets/types
    api_response = api_instance.docking_offsets_types_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetDockingOffsetTypes]**](GetDockingOffsetTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_types_id_get**
> GetDockingOffsetType docking_offsets_types_id_get(authorization, accept_language, id)

GET /docking_offsets/types/{id}

Retrieve the details about the position type with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /docking_offsets/types/{id}
    api_response = api_instance.docking_offsets_types_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->docking_offsets_types_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to search for | 

### Return type

[**GetDockingOffsetType**](GetDockingOffsetType.md)

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
api_instance = mir.DockingOffsetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
pos_id = 'pos_id_example' # str | The pos_id to search for

try:
    # GET /positions/{pos_id}/docking_offsets
    api_response = api_instance.positions_pos_id_docking_offsets_get(authorization, accept_language, pos_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockingOffsetsApi->positions_pos_id_docking_offsets_get: %s\n" % e)
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

