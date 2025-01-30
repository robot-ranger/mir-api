# mir.ActionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_action_type_get**](ActionsApi.md#actions_action_type_get) | **GET** /actions/{action_type} | GET /actions/{action_type}
[**actions_action_type_post**](ActionsApi.md#actions_action_type_post) | **POST** /actions/{action_type} | POST /actions/{action_type}
[**actions_get**](ActionsApi.md#actions_get) | **GET** /actions | GET /actions
[**mission_groups_mission_group_id_actions_get**](ActionsApi.md#mission_groups_mission_group_id_actions_get) | **GET** /mission_groups/{mission_group_id}/actions | GET /mission_groups/{mission_group_id}/actions
[**mission_queue_mission_queue_id_actions_get**](ActionsApi.md#mission_queue_mission_queue_id_actions_get) | **GET** /mission_queue/{mission_queue_id}/actions | GET /mission_queue/{mission_queue_id}/actions
[**mission_queue_mission_queue_id_actions_id_get**](ActionsApi.md#mission_queue_mission_queue_id_actions_id_get) | **GET** /mission_queue/{mission_queue_id}/actions/{id} | GET /mission_queue/{mission_queue_id}/actions/{id}
[**missions_mission_id_actions_get**](ActionsApi.md#missions_mission_id_actions_get) | **GET** /missions/{mission_id}/actions | GET /missions/{mission_id}/actions
[**missions_mission_id_actions_guid_delete**](ActionsApi.md#missions_mission_id_actions_guid_delete) | **DELETE** /missions/{mission_id}/actions/{guid} | DELETE /missions/{mission_id}/actions/{guid}
[**missions_mission_id_actions_guid_get**](ActionsApi.md#missions_mission_id_actions_guid_get) | **GET** /missions/{mission_id}/actions/{guid} | GET /missions/{mission_id}/actions/{guid}
[**missions_mission_id_actions_guid_put**](ActionsApi.md#missions_mission_id_actions_guid_put) | **PUT** /missions/{mission_id}/actions/{guid} | PUT /missions/{mission_id}/actions/{guid}
[**missions_mission_id_actions_post**](ActionsApi.md#missions_mission_id_actions_post) | **POST** /missions/{mission_id}/actions | POST /missions/{mission_id}/actions


# **actions_action_type_get**
> GetActionDefinition actions_action_type_get(authorization, accept_language, action_type)

GET /actions/{action_type}

Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
action_type = 'action_type_example' # str | The action_type to search for

try:
    # GET /actions/{action_type}
    api_response = api_instance.actions_action_type_get(authorization, accept_language, action_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->actions_action_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **action_type** | **str**| The action_type to search for | 

### Return type

[**GetActionDefinition**](GetActionDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_action_type_post**
> GetActionDefinition actions_action_type_post(authorization, accept_language, action_type, action_definition)

POST /actions/{action_type}

Add a new action definition with the specified action_type

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
action_type = 'action_type_example' # str | The action_type to add the new resource to
action_definition = mir.PostActionDefinition() # PostActionDefinition | The details of the action_definition

try:
    # POST /actions/{action_type}
    api_response = api_instance.actions_action_type_post(authorization, accept_language, action_type, action_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->actions_action_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **action_type** | **str**| The action_type to add the new resource to | 
 **action_definition** | [**PostActionDefinition**](PostActionDefinition.md)| The details of the action_definition | 

### Return type

[**GetActionDefinition**](GetActionDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_get**
> GetActionDefinitions actions_get(authorization, accept_language)

GET /actions

Retrieve the list of action definitions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /actions
    api_response = api_instance.actions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetActionDefinitions**](GetActionDefinitions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_mission_group_id_actions_get**
> GetGroupActionDefinition mission_groups_mission_group_id_actions_get(authorization, accept_language, mission_group_id)

GET /mission_groups/{mission_group_id}/actions

Retrieve the list of action definitions from the mission group with the specified mission group ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_group_id = 'mission_group_id_example' # str | The mission_group_id to search for

try:
    # GET /mission_groups/{mission_group_id}/actions
    api_response = api_instance.mission_groups_mission_group_id_actions_get(authorization, accept_language, mission_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->mission_groups_mission_group_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_group_id** | **str**| The mission_group_id to search for | 

### Return type

[**GetGroupActionDefinition**](GetGroupActionDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_mission_queue_id_actions_get**
> GetMissionQueueActions mission_queue_mission_queue_id_actions_get(authorization, accept_language, mission_queue_id)

GET /mission_queue/{mission_queue_id}/actions

Retrieve the list of actions from the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_queue_id = 56 # int | The mission_queue_id to search for

try:
    # GET /mission_queue/{mission_queue_id}/actions
    api_response = api_instance.mission_queue_mission_queue_id_actions_get(authorization, accept_language, mission_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->mission_queue_mission_queue_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_queue_id** | **int**| The mission_queue_id to search for | 

### Return type

[**GetMissionQueueActions**](GetMissionQueueActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_mission_queue_id_actions_id_get**
> GetMissionQueueAction mission_queue_mission_queue_id_actions_id_get(authorization, accept_language, mission_queue_id, id)

GET /mission_queue/{mission_queue_id}/actions/{id}

Retrieve the details about the action with the specified ID from the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_queue_id = 56 # int | The mission_queue_id to search for
id = 56 # int | The id to search for

try:
    # GET /mission_queue/{mission_queue_id}/actions/{id}
    api_response = api_instance.mission_queue_mission_queue_id_actions_id_get(authorization, accept_language, mission_queue_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->mission_queue_mission_queue_id_actions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_queue_id** | **int**| The mission_queue_id to search for | 
 **id** | **int**| The id to search for | 

### Return type

[**GetMissionQueueAction**](GetMissionQueueAction.md)

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
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to search for

try:
    # GET /missions/{mission_id}/actions
    api_response = api_instance.missions_mission_id_actions_get(authorization, accept_language, mission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->missions_mission_id_actions_get: %s\n" % e)
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
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to delete
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /missions/{mission_id}/actions/{guid}
    api_instance.missions_mission_id_actions_guid_delete(authorization, accept_language, mission_id, guid)
except ApiException as e:
    print("Exception when calling ActionsApi->missions_mission_id_actions_guid_delete: %s\n" % e)
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
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to search for
guid = 'guid_example' # str | The guid to search for

try:
    # GET /missions/{mission_id}/actions/{guid}
    api_response = api_instance.missions_mission_id_actions_guid_get(authorization, accept_language, mission_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->missions_mission_id_actions_guid_get: %s\n" % e)
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
api_instance = mir.ActionsApi()
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
    print("Exception when calling ActionsApi->missions_mission_id_actions_guid_put: %s\n" % e)
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
api_instance = mir.ActionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_id = 'mission_id_example' # str | The mission_id to add the new resource to
mission_actions = mir.PostMissionActions() # PostMissionActions | The details of the mission_actions

try:
    # POST /missions/{mission_id}/actions
    api_response = api_instance.missions_mission_id_actions_post(authorization, accept_language, mission_id, mission_actions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->missions_mission_id_actions_post: %s\n" % e)
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

