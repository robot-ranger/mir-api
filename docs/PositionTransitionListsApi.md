# mir.PositionTransitionListsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**position_transition_lists_get**](PositionTransitionListsApi.md#position_transition_lists_get) | **GET** /position_transition_lists | GET /position_transition_lists
[**position_transition_lists_guid_delete**](PositionTransitionListsApi.md#position_transition_lists_guid_delete) | **DELETE** /position_transition_lists/{guid} | DELETE /position_transition_lists/{guid}
[**position_transition_lists_guid_get**](PositionTransitionListsApi.md#position_transition_lists_guid_get) | **GET** /position_transition_lists/{guid} | GET /position_transition_lists/{guid}
[**position_transition_lists_guid_put**](PositionTransitionListsApi.md#position_transition_lists_guid_put) | **PUT** /position_transition_lists/{guid} | PUT /position_transition_lists/{guid}
[**position_transition_lists_post**](PositionTransitionListsApi.md#position_transition_lists_post) | **POST** /position_transition_lists | POST /position_transition_lists
[**sessions_session_id_position_transition_lists_get**](PositionTransitionListsApi.md#sessions_session_id_position_transition_lists_get) | **GET** /sessions/{session_id}/position_transition_lists | GET /sessions/{session_id}/position_transition_lists


# **position_transition_lists_get**
> GetPositionTransitionLists position_transition_lists_get(authorization, accept_language)

GET /position_transition_lists

Retrieve the list of position transition lists

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionTransitionListsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /position_transition_lists
    api_response = api_instance.position_transition_lists_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTransitionListsApi->position_transition_lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetPositionTransitionLists**](GetPositionTransitionLists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_guid_delete**
> position_transition_lists_guid_delete(authorization, accept_language, guid)

DELETE /position_transition_lists/{guid}

Erase the position transition list with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionTransitionListsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /position_transition_lists/{guid}
    api_instance.position_transition_lists_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling PositionTransitionListsApi->position_transition_lists_guid_delete: %s\n" % e)
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

# **position_transition_lists_guid_get**
> GetPositionTransitionList position_transition_lists_guid_get(authorization, accept_language, guid)

GET /position_transition_lists/{guid}

Retrieve the details about the position transition list with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionTransitionListsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /position_transition_lists/{guid}
    api_response = api_instance.position_transition_lists_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTransitionListsApi->position_transition_lists_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetPositionTransitionList**](GetPositionTransitionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_guid_put**
> GetPositionTransitionList position_transition_lists_guid_put(authorization, accept_language, guid, position_transition_list)

PUT /position_transition_lists/{guid}

Modify the values of the position transition list with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionTransitionListsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
position_transition_list = mir.PutPositionTransitionList() # PutPositionTransitionList | The new values of the position_transition_list

try:
    # PUT /position_transition_lists/{guid}
    api_response = api_instance.position_transition_lists_guid_put(authorization, accept_language, guid, position_transition_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTransitionListsApi->position_transition_lists_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **position_transition_list** | [**PutPositionTransitionList**](PutPositionTransitionList.md)| The new values of the position_transition_list | 

### Return type

[**GetPositionTransitionList**](GetPositionTransitionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_post**
> GetPositionTransitionLists position_transition_lists_post(authorization, accept_language, position_transition_lists)

POST /position_transition_lists

Add a new position transition list

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionTransitionListsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
position_transition_lists = mir.PostPositionTransitionLists() # PostPositionTransitionLists | The details of the position_transition_lists

try:
    # POST /position_transition_lists
    api_response = api_instance.position_transition_lists_post(authorization, accept_language, position_transition_lists)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTransitionListsApi->position_transition_lists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **position_transition_lists** | [**PostPositionTransitionLists**](PostPositionTransitionLists.md)| The details of the position_transition_lists | 

### Return type

[**GetPositionTransitionLists**](GetPositionTransitionLists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_position_transition_lists_get**
> GetPositionTransitionListFromSession sessions_session_id_position_transition_lists_get(authorization, accept_language, session_id)

GET /sessions/{session_id}/position_transition_lists

Retrieve the list of position transition lists that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PositionTransitionListsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/position_transition_lists
    api_response = api_instance.sessions_session_id_position_transition_lists_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTransitionListsApi->sessions_session_id_position_transition_lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **session_id** | **str**| The session_id to search for | 

### Return type

[**GetPositionTransitionListFromSession**](GetPositionTransitionListFromSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

