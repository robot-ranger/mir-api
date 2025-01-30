# mir.TypesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docking_offsets_types_get**](TypesApi.md#docking_offsets_types_get) | **GET** /docking_offsets/types | GET /docking_offsets/types
[**docking_offsets_types_id_get**](TypesApi.md#docking_offsets_types_id_get) | **GET** /docking_offsets/types/{id} | GET /docking_offsets/types/{id}


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
api_instance = mir.TypesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /docking_offsets/types
    api_response = api_instance.docking_offsets_types_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TypesApi->docking_offsets_types_get: %s\n" % e)
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
api_instance = mir.TypesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /docking_offsets/types/{id}
    api_response = api_instance.docking_offsets_types_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TypesApi->docking_offsets_types_id_get: %s\n" % e)
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

