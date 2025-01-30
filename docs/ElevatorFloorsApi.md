# mir.ElevatorFloorsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevator_floors_get**](ElevatorFloorsApi.md#elevator_floors_get) | **GET** /elevator_floors | GET /elevator_floors
[**elevator_floors_guid_delete**](ElevatorFloorsApi.md#elevator_floors_guid_delete) | **DELETE** /elevator_floors/{guid} | DELETE /elevator_floors/{guid}
[**elevator_floors_guid_get**](ElevatorFloorsApi.md#elevator_floors_guid_get) | **GET** /elevator_floors/{guid} | GET /elevator_floors/{guid}
[**elevator_floors_guid_put**](ElevatorFloorsApi.md#elevator_floors_guid_put) | **PUT** /elevator_floors/{guid} | PUT /elevator_floors/{guid}
[**elevator_floors_post**](ElevatorFloorsApi.md#elevator_floors_post) | **POST** /elevator_floors | POST /elevator_floors
[**sessions_session_id_elevator_floors_get**](ElevatorFloorsApi.md#sessions_session_id_elevator_floors_get) | **GET** /sessions/{session_id}/elevator_floors | GET /sessions/{session_id}/elevator_floors


# **elevator_floors_get**
> list[GetElevatorFloors] elevator_floors_get(authorization, accept_language)

GET /elevator_floors

Retrieve the list of elevator floors in the fleet

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorFloorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /elevator_floors
    api_response = api_instance.elevator_floors_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorFloorsApi->elevator_floors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetElevatorFloors]**](GetElevatorFloors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elevator_floors_guid_delete**
> elevator_floors_guid_delete(authorization, accept_language, guid)

DELETE /elevator_floors/{guid}

Delete the specified elevator floor

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorFloorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /elevator_floors/{guid}
    api_instance.elevator_floors_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling ElevatorFloorsApi->elevator_floors_guid_delete: %s\n" % e)
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

# **elevator_floors_guid_get**
> GetElevatorFloor elevator_floors_guid_get(authorization, accept_language, guid)

GET /elevator_floors/{guid}

Retrieve the details about the specified elevator floor

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorFloorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /elevator_floors/{guid}
    api_response = api_instance.elevator_floors_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorFloorsApi->elevator_floors_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetElevatorFloor**](GetElevatorFloor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elevator_floors_guid_put**
> GetElevatorFloor elevator_floors_guid_put(authorization, accept_language, guid, elevator_floor)

PUT /elevator_floors/{guid}

Modify the values of the specified elevator floor

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorFloorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
elevator_floor = mir.PutElevatorFloor() # PutElevatorFloor | The new values of the elevator_floor

try:
    # PUT /elevator_floors/{guid}
    api_response = api_instance.elevator_floors_guid_put(authorization, accept_language, guid, elevator_floor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorFloorsApi->elevator_floors_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **elevator_floor** | [**PutElevatorFloor**](PutElevatorFloor.md)| The new values of the elevator_floor | 

### Return type

[**GetElevatorFloor**](GetElevatorFloor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elevator_floors_post**
> GetElevatorFloors elevator_floors_post(authorization, accept_language, elevator_floors)

POST /elevator_floors

Add a new elevator floor to the fleet

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorFloorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
elevator_floors = mir.PostElevatorFloors() # PostElevatorFloors | The details of the elevator_floors

try:
    # POST /elevator_floors
    api_response = api_instance.elevator_floors_post(authorization, accept_language, elevator_floors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorFloorsApi->elevator_floors_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **elevator_floors** | [**PostElevatorFloors**](PostElevatorFloors.md)| The details of the elevator_floors | 

### Return type

[**GetElevatorFloors**](GetElevatorFloors.md)

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
api_instance = mir.ElevatorFloorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/elevator_floors
    api_response = api_instance.sessions_session_id_elevator_floors_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorFloorsApi->sessions_session_id_elevator_floors_get: %s\n" % e)
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

