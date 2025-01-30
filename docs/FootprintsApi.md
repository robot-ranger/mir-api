# mir.FootprintsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**footprints_get**](FootprintsApi.md#footprints_get) | **GET** /footprints | GET /footprints
[**footprints_guid_delete**](FootprintsApi.md#footprints_guid_delete) | **DELETE** /footprints/{guid} | DELETE /footprints/{guid}
[**footprints_guid_get**](FootprintsApi.md#footprints_guid_get) | **GET** /footprints/{guid} | GET /footprints/{guid}
[**footprints_guid_put**](FootprintsApi.md#footprints_guid_put) | **PUT** /footprints/{guid} | PUT /footprints/{guid}
[**footprints_post**](FootprintsApi.md#footprints_post) | **POST** /footprints | POST /footprints


# **footprints_get**
> list[GetFootprints] footprints_get(authorization, accept_language)

GET /footprints

Retrieve a list of footprints currently stored

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.FootprintsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /footprints
    api_response = api_instance.footprints_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintsApi->footprints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetFootprints]**](GetFootprints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **footprints_guid_delete**
> footprints_guid_delete(authorization, accept_language, guid)

DELETE /footprints/{guid}

Delete with a specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.FootprintsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /footprints/{guid}
    api_instance.footprints_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling FootprintsApi->footprints_guid_delete: %s\n" % e)
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

# **footprints_guid_get**
> GetFootprint footprints_guid_get(authorization, accept_language, guid)

GET /footprints/{guid}

Retrieve information about a footprint with specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.FootprintsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /footprints/{guid}
    api_response = api_instance.footprints_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintsApi->footprints_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetFootprint**](GetFootprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **footprints_guid_put**
> GetFootprint footprints_guid_put(authorization, accept_language, guid, footprint)

PUT /footprints/{guid}

Modify a footprint with a specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.FootprintsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
footprint = mir.PutFootprint() # PutFootprint | The new values of the footprint

try:
    # PUT /footprints/{guid}
    api_response = api_instance.footprints_guid_put(authorization, accept_language, guid, footprint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintsApi->footprints_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **footprint** | [**PutFootprint**](PutFootprint.md)| The new values of the footprint | 

### Return type

[**GetFootprint**](GetFootprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **footprints_post**
> GetFootprints footprints_post(authorization, accept_language, footprints)

POST /footprints

Add new footprint to the database

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.FootprintsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
footprints = mir.PostFootprints() # PostFootprints | The details of the footprints

try:
    # POST /footprints
    api_response = api_instance.footprints_post(authorization, accept_language, footprints)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintsApi->footprints_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **footprints** | [**PostFootprints**](PostFootprints.md)| The details of the footprints | 

### Return type

[**GetFootprints**](GetFootprints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

