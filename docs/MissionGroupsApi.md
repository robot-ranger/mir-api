# mir.MissionGroupsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mission_groups_get**](MissionGroupsApi.md#mission_groups_get) | **GET** /mission_groups | GET /mission_groups
[**mission_groups_group_id_missions_get**](MissionGroupsApi.md#mission_groups_group_id_missions_get) | **GET** /mission_groups/{group_id}/missions | GET /mission_groups/{group_id}/missions
[**mission_groups_guid_delete**](MissionGroupsApi.md#mission_groups_guid_delete) | **DELETE** /mission_groups/{guid} | DELETE /mission_groups/{guid}
[**mission_groups_guid_get**](MissionGroupsApi.md#mission_groups_guid_get) | **GET** /mission_groups/{guid} | GET /mission_groups/{guid}
[**mission_groups_guid_put**](MissionGroupsApi.md#mission_groups_guid_put) | **PUT** /mission_groups/{guid} | PUT /mission_groups/{guid}
[**mission_groups_mission_group_id_actions_get**](MissionGroupsApi.md#mission_groups_mission_group_id_actions_get) | **GET** /mission_groups/{mission_group_id}/actions | GET /mission_groups/{mission_group_id}/actions
[**mission_groups_post**](MissionGroupsApi.md#mission_groups_post) | **POST** /mission_groups | POST /mission_groups


# **mission_groups_get**
> list[GetMissionGroups] mission_groups_get(authorization, accept_language)

GET /mission_groups

Retrieve the list of mission groups

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /mission_groups
    api_response = api_instance.mission_groups_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionGroupsApi->mission_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetMissionGroups]**](GetMissionGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mir.MissionGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
group_id = 'group_id_example' # str | The group_id to search for

try:
    # GET /mission_groups/{group_id}/missions
    api_response = api_instance.mission_groups_group_id_missions_get(authorization, accept_language, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionGroupsApi->mission_groups_group_id_missions_get: %s\n" % e)
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

# **mission_groups_guid_delete**
> mission_groups_guid_delete(authorization, accept_language, guid)

DELETE /mission_groups/{guid}

Erase the mission group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /mission_groups/{guid}
    api_instance.mission_groups_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling MissionGroupsApi->mission_groups_guid_delete: %s\n" % e)
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

# **mission_groups_guid_get**
> GetMissionGroup mission_groups_guid_get(authorization, accept_language, guid)

GET /mission_groups/{guid}

Retrieve the details about the mission group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /mission_groups/{guid}
    api_response = api_instance.mission_groups_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionGroupsApi->mission_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetMissionGroup**](GetMissionGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_guid_put**
> GetMissionGroup mission_groups_guid_put(authorization, accept_language, guid, mission_group)

PUT /mission_groups/{guid}

Modify the values of the mission group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
mission_group = mir.PutMissionGroup() # PutMissionGroup | The new values of the mission_group

try:
    # PUT /mission_groups/{guid}
    api_response = api_instance.mission_groups_guid_put(authorization, accept_language, guid, mission_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionGroupsApi->mission_groups_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **mission_group** | [**PutMissionGroup**](PutMissionGroup.md)| The new values of the mission_group | 

### Return type

[**GetMissionGroup**](GetMissionGroup.md)

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
api_instance = mir.MissionGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_group_id = 'mission_group_id_example' # str | The mission_group_id to search for

try:
    # GET /mission_groups/{mission_group_id}/actions
    api_response = api_instance.mission_groups_mission_group_id_actions_get(authorization, accept_language, mission_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionGroupsApi->mission_groups_mission_group_id_actions_get: %s\n" % e)
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

# **mission_groups_post**
> GetMissionGroups mission_groups_post(authorization, accept_language, mission_groups)

POST /mission_groups

Add a new mission group

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_groups = mir.PostMissionGroups() # PostMissionGroups | The details of the mission_groups

try:
    # POST /mission_groups
    api_response = api_instance.mission_groups_post(authorization, accept_language, mission_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionGroupsApi->mission_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_groups** | [**PostMissionGroups**](PostMissionGroups.md)| The details of the mission_groups | 

### Return type

[**GetMissionGroups**](GetMissionGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

