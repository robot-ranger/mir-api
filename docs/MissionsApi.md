# mir.MissionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mission_groups_group_id_missions_get**](MissionsApi.md#mission_groups_group_id_missions_get) | **GET** /mission_groups/{group_id}/missions | GET /mission_groups/{group_id}/missions
[**missions_get**](MissionsApi.md#missions_get) | **GET** /missions | GET /missions
[**missions_guid_definition_get**](MissionsApi.md#missions_guid_definition_get) | **GET** /missions/{guid}/definition | GET /missions/{guid}/definition
[**missions_guid_delete**](MissionsApi.md#missions_guid_delete) | **DELETE** /missions/{guid} | DELETE /missions/{guid}
[**missions_guid_get**](MissionsApi.md#missions_guid_get) | **GET** /missions/{guid} | GET /missions/{guid}
[**missions_guid_put**](MissionsApi.md#missions_guid_put) | **PUT** /missions/{guid} | PUT /missions/{guid}
[**missions_mission_id_actions_get**](MissionsApi.md#missions_mission_id_actions_get) | **GET** /missions/{mission_id}/actions | GET /missions/{mission_id}/actions
[**missions_mission_id_actions_guid_delete**](MissionsApi.md#missions_mission_id_actions_guid_delete) | **DELETE** /missions/{mission_id}/actions/{guid} | DELETE /missions/{mission_id}/actions/{guid}
[**missions_mission_id_actions_guid_get**](MissionsApi.md#missions_mission_id_actions_guid_get) | **GET** /missions/{mission_id}/actions/{guid} | GET /missions/{mission_id}/actions/{guid}
[**missions_mission_id_actions_guid_put**](MissionsApi.md#missions_mission_id_actions_guid_put) | **PUT** /missions/{mission_id}/actions/{guid} | PUT /missions/{mission_id}/actions/{guid}
[**missions_mission_id_actions_post**](MissionsApi.md#missions_mission_id_actions_post) | **POST** /missions/{mission_id}/actions | POST /missions/{mission_id}/actions
[**missions_post**](MissionsApi.md#missions_post) | **POST** /missions | POST /missions
[**modbus_missions_get**](MissionsApi.md#modbus_missions_get) | **GET** /modbus/missions | GET /modbus/missions
[**modbus_missions_guid_delete**](MissionsApi.md#modbus_missions_guid_delete) | **DELETE** /modbus/missions/{guid} | DELETE /modbus/missions/{guid}
[**modbus_missions_guid_get**](MissionsApi.md#modbus_missions_guid_get) | **GET** /modbus/missions/{guid} | GET /modbus/missions/{guid}
[**modbus_missions_guid_put**](MissionsApi.md#modbus_missions_guid_put) | **PUT** /modbus/missions/{guid} | PUT /modbus/missions/{guid}
[**modbus_missions_post**](MissionsApi.md#modbus_missions_post) | **POST** /modbus/missions | POST /modbus/missions
[**sessions_session_id_missions_get**](MissionsApi.md#sessions_session_id_missions_get) | **GET** /sessions/{session_id}/missions | GET /sessions/{session_id}/missions


# **mission_groups_group_id_missions_get**
> list[GetGroupMissions] mission_groups_group_id_missions_get(authorization, accept_language, group_id)

GET /mission_groups/{group_id}/missions

Retrieve the list of missions that belong to the group with the specified group ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
group_id = 'group_id_example' # str | The group_id to search for

try:
    # GET /mission_groups/{group_id}/missions
    api_response = api_instance.mission_groups_group_id_missions_get(authorization, accept_language, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->mission_groups_group_id_missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **group_id** | **str**| The group_id to search for | 

### Return type

[**list[GetGroupMissions]**](GetGroupMissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_get**
> list[GetMissions] missions_get(authorization, accept_language)

GET /missions

Retrieve the list of missions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /missions
    api_response = api_instance.missions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetMissions]**](GetMissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_guid_definition_get**
> list[GetMissionDefinition] missions_guid_definition_get(authorization, accept_language, guid)

GET /missions/{guid}/definition

Retrieve the mission with the specified GUID as an action definition that can be inserted in another mission

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /missions/{guid}/definition
    api_response = api_instance.missions_guid_definition_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_guid_definition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**list[GetMissionDefinition]**](GetMissionDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_guid_delete**
> missions_guid_delete(authorization, accept_language, guid)

DELETE /missions/{guid}

Erase the mission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /missions/{guid}
    api_instance.missions_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_guid_delete: %s\n" % e)
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

# **missions_guid_get**
> GetMission missions_guid_get(authorization, accept_language, guid)

GET /missions/{guid}

Retrieve the details about the mission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /missions/{guid}
    api_response = api_instance.missions_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetMission**](GetMission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_guid_put**
> GetMission missions_guid_put(authorization, accept_language, guid, mission)

PUT /missions/{guid}

Modify the values of the mission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
mission = mir.PutMission() # PutMission | The new values of the mission

try:
    # PUT /missions/{guid}
    api_response = api_instance.missions_guid_put(authorization, accept_language, guid, mission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **mission** | [**PutMission**](PutMission.md)| The new values of the mission | 

### Return type

[**GetMission**](GetMission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_get**
> list[GetMissionActions] missions_mission_id_actions_get(authorization, accept_language, mission_id)

GET /missions/{mission_id}/actions

Retrieve the list of actions that belong to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to search for

try:
    # GET /missions/{mission_id}/actions
    api_response = api_instance.missions_mission_id_actions_get(authorization, accept_language, mission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_mission_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_id** | **str**| The mission_id to search for | 

### Return type

[**list[GetMissionActions]**](GetMissionActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_guid_delete**
> missions_mission_id_actions_guid_delete(authorization, accept_language, mission_id, guid)

DELETE /missions/{mission_id}/actions/{guid}

Erase the action with the specified GUID from the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to delete
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /missions/{mission_id}/actions/{guid}
    api_instance.missions_mission_id_actions_guid_delete(authorization, accept_language, mission_id, guid)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_mission_id_actions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_id** | **str**| The mission_id to delete | 
 **guid** | **str**| The guid to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_guid_get**
> GetMissionAction missions_mission_id_actions_guid_get(authorization, accept_language, mission_id, guid)

GET /missions/{mission_id}/actions/{guid}

Retrieve the details about the action with the specified GUID that belongs to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to search for
guid = 'guid_example' # str | The guid to search for

try:
    # GET /missions/{mission_id}/actions/{guid}
    api_response = api_instance.missions_mission_id_actions_guid_get(authorization, accept_language, mission_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_mission_id_actions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_id** | **str**| The mission_id to search for | 
 **guid** | **str**| The guid to search for | 

### Return type

[**GetMissionAction**](GetMissionAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_guid_put**
> GetMissionAction missions_mission_id_actions_guid_put(authorization, accept_language, mission_id, guid, mission_action)

PUT /missions/{mission_id}/actions/{guid}

Modify the values of the action with the specified GUID that belongs to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to modify
guid = 'guid_example' # str | The guid to modify
mission_action = mir.PutMissionAction() # PutMissionAction | The new values of the mission_action

try:
    # PUT /missions/{mission_id}/actions/{guid}
    api_response = api_instance.missions_mission_id_actions_guid_put(authorization, accept_language, mission_id, guid, mission_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_mission_id_actions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_id** | **str**| The mission_id to modify | 
 **guid** | **str**| The guid to modify | 
 **mission_action** | [**PutMissionAction**](PutMissionAction.md)| The new values of the mission_action | 

### Return type

[**GetMissionAction**](GetMissionAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_post**
> GetMissionActions missions_mission_id_actions_post(authorization, accept_language, mission_id, mission_actions)

POST /missions/{mission_id}/actions

Add a new action to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to add the new resource to
mission_actions = mir.PostMissionActions() # PostMissionActions | The details of the mission_actions

try:
    # POST /missions/{mission_id}/actions
    api_response = api_instance.missions_mission_id_actions_post(authorization, accept_language, mission_id, mission_actions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_mission_id_actions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_id** | **str**| The mission_id to add the new resource to | 
 **mission_actions** | [**PostMissionActions**](PostMissionActions.md)| The details of the mission_actions | 

### Return type

[**GetMissionActions**](GetMissionActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_post**
> GetMissions missions_post(authorization, accept_language, missions)

POST /missions

Add a new mission

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
missions = mir.PostMissions() # PostMissions | The details of the missions

try:
    # POST /missions
    api_response = api_instance.missions_post(authorization, accept_language, missions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->missions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **missions** | [**PostMissions**](PostMissions.md)| The details of the missions | 

### Return type

[**GetMissions**](GetMissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_get**
> list[GetModbusMissions] modbus_missions_get(authorization, accept_language)

GET /modbus/missions

Retrieve the list of coils that can trigger a mission

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /modbus/missions
    api_response = api_instance.modbus_missions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->modbus_missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetModbusMissions]**](GetModbusMissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_guid_delete**
> modbus_missions_guid_delete(authorization, accept_language, guid)

DELETE /modbus/missions/{guid}

Delete the specified ID on the the modbus mission table

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /modbus/missions/{guid}
    api_instance.modbus_missions_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling MissionsApi->modbus_missions_guid_delete: %s\n" % e)
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

# **modbus_missions_guid_get**
> GetModbusMission modbus_missions_guid_get(authorization, accept_language, guid)

GET /modbus/missions/{guid}

Retrieve the details about the mission linked with the coil

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /modbus/missions/{guid}
    api_response = api_instance.modbus_missions_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->modbus_missions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetModbusMission**](GetModbusMission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_guid_put**
> GetModbusMission modbus_missions_guid_put(authorization, accept_language, guid, modbus_mission)

PUT /modbus/missions/{guid}

Modify the values of the modbus mission with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
modbus_mission = mir.PutModbusMission() # PutModbusMission | The new values of the modbus_mission

try:
    # PUT /modbus/missions/{guid}
    api_response = api_instance.modbus_missions_guid_put(authorization, accept_language, guid, modbus_mission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->modbus_missions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **modbus_mission** | [**PutModbusMission**](PutModbusMission.md)| The new values of the modbus_mission | 

### Return type

[**GetModbusMission**](GetModbusMission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_post**
> GetModbusMissions modbus_missions_post(authorization, accept_language, modbus_missions)

POST /modbus/missions

Create a new link between a coil and a mission

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
modbus_missions = mir.PostModbusMissions() # PostModbusMissions | The details of the modbus_missions

try:
    # POST /modbus/missions
    api_response = api_instance.modbus_missions_post(authorization, accept_language, modbus_missions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->modbus_missions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **modbus_missions** | [**PostModbusMissions**](PostModbusMissions.md)| The details of the modbus_missions | 

### Return type

[**GetModbusMissions**](GetModbusMissions.md)

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
api_instance = mir.MissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/missions
    api_response = api_instance.sessions_session_id_missions_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionsApi->sessions_session_id_missions_get: %s\n" % e)
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

