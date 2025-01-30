# mir.MissionQueueApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mission_queue_delete**](MissionQueueApi.md#mission_queue_delete) | **DELETE** /mission_queue | DELETE /mission_queue
[**mission_queue_get**](MissionQueueApi.md#mission_queue_get) | **GET** /mission_queue | GET /mission_queue
[**mission_queue_id_delete**](MissionQueueApi.md#mission_queue_id_delete) | **DELETE** /mission_queue/{id} | DELETE /mission_queue/{id}
[**mission_queue_id_get**](MissionQueueApi.md#mission_queue_id_get) | **GET** /mission_queue/{id} | GET /mission_queue/{id}
[**mission_queue_id_put**](MissionQueueApi.md#mission_queue_id_put) | **PUT** /mission_queue/{id} | PUT /mission_queue/{id}
[**mission_queue_mission_queue_id_actions_get**](MissionQueueApi.md#mission_queue_mission_queue_id_actions_get) | **GET** /mission_queue/{mission_queue_id}/actions | GET /mission_queue/{mission_queue_id}/actions
[**mission_queue_mission_queue_id_actions_id_get**](MissionQueueApi.md#mission_queue_mission_queue_id_actions_id_get) | **GET** /mission_queue/{mission_queue_id}/actions/{id} | GET /mission_queue/{mission_queue_id}/actions/{id}
[**mission_queue_post**](MissionQueueApi.md#mission_queue_post) | **POST** /mission_queue | POST /mission_queue


# **mission_queue_delete**
> mission_queue_delete(authorization, accept_language)

DELETE /mission_queue

Abort all the pending and executing missions from the mission queue

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # DELETE /mission_queue
    api_instance.mission_queue_delete(authorization, accept_language)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_delete: %s\n" % e)
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

# **mission_queue_get**
> list[GetMissionQueues] mission_queue_get(authorization, accept_language)

GET /mission_queue

Retrieve the list of missions in the queue. Finished, failed, pending and executing missions will be displayed here

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /mission_queue
    api_response = api_instance.mission_queue_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetMissionQueues]**](GetMissionQueues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_id_delete**
> mission_queue_id_delete(authorization, accept_language, id)

DELETE /mission_queue/{id}

Abort the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to delete

try:
    # DELETE /mission_queue/{id}
    api_instance.mission_queue_id_delete(authorization, accept_language, id)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_id_get**
> GetMissionQueue mission_queue_id_get(authorization, accept_language, id)

GET /mission_queue/{id}

Retrieve the details about the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /mission_queue/{id}
    api_response = api_instance.mission_queue_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to search for | 

### Return type

[**GetMissionQueue**](GetMissionQueue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_id_put**
> GetMissionQueue mission_queue_id_put(authorization, accept_language, id, mission_queue)

PUT /mission_queue/{id}

Modify the values of the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to modify
mission_queue = mir.PutMissionQueue() # PutMissionQueue | The new values of the mission_queue

try:
    # PUT /mission_queue/{id}
    api_response = api_instance.mission_queue_id_put(authorization, accept_language, id, mission_queue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to modify | 
 **mission_queue** | [**PutMissionQueue**](PutMissionQueue.md)| The new values of the mission_queue | 

### Return type

[**GetMissionQueue**](GetMissionQueue.md)

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
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_queue_id = 56 # int | The mission_queue_id to search for

try:
    # GET /mission_queue/{mission_queue_id}/actions
    api_response = api_instance.mission_queue_mission_queue_id_actions_get(authorization, accept_language, mission_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_mission_queue_id_actions_get: %s\n" % e)
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
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_queue_id = 56 # int | The mission_queue_id to search for
id = 56 # int | The id to search for

try:
    # GET /mission_queue/{mission_queue_id}/actions/{id}
    api_response = api_instance.mission_queue_mission_queue_id_actions_id_get(authorization, accept_language, mission_queue_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_mission_queue_id_actions_id_get: %s\n" % e)
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

# **mission_queue_post**
> GetMissionQueues mission_queue_post(authorization, accept_language, mission_queues)

POST /mission_queue

Add a new mission to the mission queue. The mission will always go to the end of the queue

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.MissionQueueApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
mission_queues = mir.PostMissionQueues() # PostMissionQueues | The details of the mission_queues

try:
    # POST /mission_queue
    api_response = api_instance.mission_queue_post(authorization, accept_language, mission_queues)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MissionQueueApi->mission_queue_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **mission_queues** | [**PostMissionQueues**](PostMissionQueues.md)| The details of the mission_queues | 

### Return type

[**GetMissionQueues**](GetMissionQueues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

