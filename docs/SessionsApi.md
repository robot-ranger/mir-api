# mir.SessionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessions_get**](SessionsApi.md#sessions_get) | **GET** /sessions | GET /sessions
[**sessions_guid_delete**](SessionsApi.md#sessions_guid_delete) | **DELETE** /sessions/{guid} | DELETE /sessions/{guid}
[**sessions_guid_export_get**](SessionsApi.md#sessions_guid_export_get) | **GET** /sessions/{guid}/export | GET /sessions/{guid}/export
[**sessions_guid_get**](SessionsApi.md#sessions_guid_get) | **GET** /sessions/{guid} | GET /sessions/{guid}
[**sessions_guid_put**](SessionsApi.md#sessions_guid_put) | **PUT** /sessions/{guid} | PUT /sessions/{guid}
[**sessions_import_delete**](SessionsApi.md#sessions_import_delete) | **DELETE** /sessions/import | DELETE /sessions/import
[**sessions_import_get**](SessionsApi.md#sessions_import_get) | **GET** /sessions/import | GET /sessions/import
[**sessions_import_post**](SessionsApi.md#sessions_import_post) | **POST** /sessions/import | POST /sessions/import
[**sessions_post**](SessionsApi.md#sessions_post) | **POST** /sessions | POST /sessions
[**sessions_session_id_elevator_floors_get**](SessionsApi.md#sessions_session_id_elevator_floors_get) | **GET** /sessions/{session_id}/elevator_floors | GET /sessions/{session_id}/elevator_floors
[**sessions_session_id_elevators_get**](SessionsApi.md#sessions_session_id_elevators_get) | **GET** /sessions/{session_id}/elevators | GET /sessions/{session_id}/elevators
[**sessions_session_id_maps_get**](SessionsApi.md#sessions_session_id_maps_get) | **GET** /sessions/{session_id}/maps | GET /sessions/{session_id}/maps
[**sessions_session_id_missions_get**](SessionsApi.md#sessions_session_id_missions_get) | **GET** /sessions/{session_id}/missions | GET /sessions/{session_id}/missions
[**sessions_session_id_position_transition_lists_get**](SessionsApi.md#sessions_session_id_position_transition_lists_get) | **GET** /sessions/{session_id}/position_transition_lists | GET /sessions/{session_id}/position_transition_lists


# **sessions_get**
> list[GetSessions] sessions_get(authorization, accept_language)

GET /sessions

Retrieve the list of sessions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /sessions
    api_response = api_instance.sessions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSessions]**](GetSessions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_delete**
> sessions_guid_delete(authorization, accept_language, guid)

DELETE /sessions/{guid}

Erase the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /sessions/{guid}
    api_instance.sessions_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_guid_delete: %s\n" % e)
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

# **sessions_guid_export_get**
> GetSessionExport sessions_guid_export_get(authorization, accept_language, guid)

GET /sessions/{guid}/export

Download a file containing the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /sessions/{guid}/export
    api_response = api_instance.sessions_guid_export_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_guid_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSessionExport**](GetSessionExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_get**
> GetSession sessions_guid_get(authorization, accept_language, guid)

GET /sessions/{guid}

Retrieve the details about the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /sessions/{guid}
    api_response = api_instance.sessions_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSession**](GetSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_put**
> GetSession sessions_guid_put(authorization, accept_language, guid, session)

PUT /sessions/{guid}

Modify the values of the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
session = mir.PutSession() # PutSession | The new values of the session

try:
    # PUT /sessions/{guid}
    api_response = api_instance.sessions_guid_put(authorization, accept_language, guid, session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **session** | [**PutSession**](PutSession.md)| The new values of the session | 

### Return type

[**GetSession**](GetSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_delete**
> sessions_import_delete(authorization, accept_language)

DELETE /sessions/import

Cancel currently running import

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # DELETE /sessions/import
    api_instance.sessions_import_delete(authorization, accept_language)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_import_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_get**
> GetSessionImport sessions_import_get(authorization, accept_language)

GET /sessions/import

Get progress of the running import

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /sessions/import
    api_response = api_instance.sessions_import_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_import_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSessionImport**](GetSessionImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_post**
> GetSessionImport sessions_import_post(authorization, accept_language, session_import)

POST /sessions/import

Import the session contained in the file

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_import = mir.PostSessionImport() # PostSessionImport | The details of the session_import

try:
    # POST /sessions/import
    api_response = api_instance.sessions_import_post(authorization, accept_language, session_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **session_import** | [**PostSessionImport**](PostSessionImport.md)| The details of the session_import | 

### Return type

[**GetSessionImport**](GetSessionImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_post**
> GetSessions sessions_post(authorization, accept_language, sessions)

POST /sessions

Add a new session

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
sessions = mir.PostSessions() # PostSessions | The details of the sessions

try:
    # POST /sessions
    api_response = api_instance.sessions_post(authorization, accept_language, sessions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **sessions** | [**PostSessions**](PostSessions.md)| The details of the sessions | 

### Return type

[**GetSessions**](GetSessions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_elevator_floors_get**
> list[GetSessionElevatorFloors] sessions_session_id_elevator_floors_get(authorization, accept_language, session_id)

GET /sessions/{session_id}/elevator_floors

Retrieve the list of elevator floors that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/elevator_floors
    api_response = api_instance.sessions_session_id_elevator_floors_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_session_id_elevator_floors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **session_id** | **str**| The session_id to search for | 

### Return type

[**list[GetSessionElevatorFloors]**](GetSessionElevatorFloors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_elevators_get**
> list[GetSessionElevators] sessions_session_id_elevators_get(authorization, accept_language, session_id)

GET /sessions/{session_id}/elevators

Retrieve the list of elevators that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/elevators
    api_response = api_instance.sessions_session_id_elevators_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_session_id_elevators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **session_id** | **str**| The session_id to search for | 

### Return type

[**list[GetSessionElevators]**](GetSessionElevators.md)

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
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/maps
    api_response = api_instance.sessions_session_id_maps_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_session_id_maps_get: %s\n" % e)
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

# **sessions_session_id_missions_get**
> list[GetSessionMissions] sessions_session_id_missions_get(authorization, accept_language, session_id)

GET /sessions/{session_id}/missions

Retrieve the list of missions that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/missions
    api_response = api_instance.sessions_session_id_missions_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_session_id_missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **session_id** | **str**| The session_id to search for | 

### Return type

[**list[GetSessionMissions]**](GetSessionMissions.md)

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
api_instance = mir.SessionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/position_transition_lists
    api_response = api_instance.sessions_session_id_position_transition_lists_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_session_id_position_transition_lists_get: %s\n" % e)
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

