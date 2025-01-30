# mir.ElevatorsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevators_get**](ElevatorsApi.md#elevators_get) | **GET** /elevators | GET /elevators
[**elevators_guid_delete**](ElevatorsApi.md#elevators_guid_delete) | **DELETE** /elevators/{guid} | DELETE /elevators/{guid}
[**elevators_guid_get**](ElevatorsApi.md#elevators_guid_get) | **GET** /elevators/{guid} | GET /elevators/{guid}
[**elevators_guid_put**](ElevatorsApi.md#elevators_guid_put) | **PUT** /elevators/{guid} | PUT /elevators/{guid}
[**elevators_post**](ElevatorsApi.md#elevators_post) | **POST** /elevators | POST /elevators
[**sessions_session_id_elevators_get**](ElevatorsApi.md#sessions_session_id_elevators_get) | **GET** /sessions/{session_id}/elevators | GET /sessions/{session_id}/elevators


# **elevators_get**
> list[GetElevators] elevators_get(authorization, accept_language)

GET /elevators

Retrieve a list of elevators in the fleet

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /elevators
    api_response = api_instance.elevators_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorsApi->elevators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetElevators]**](GetElevators.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elevators_guid_delete**
> elevators_guid_delete(authorization, accept_language, guid)

DELETE /elevators/{guid}

Delete the elevator with the specified guid

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /elevators/{guid}
    api_instance.elevators_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling ElevatorsApi->elevators_guid_delete: %s\n" % e)
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

# **elevators_guid_get**
> GetElevator elevators_guid_get(authorization, accept_language, guid)

GET /elevators/{guid}

Retrieve the details about the elevator with the specified guid

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /elevators/{guid}
    api_response = api_instance.elevators_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorsApi->elevators_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetElevator**](GetElevator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elevators_guid_put**
> GetElevator elevators_guid_put(authorization, accept_language, guid, elevator)

PUT /elevators/{guid}

Modify the values of the elevator with the specified guid

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
elevator = mir.PutElevator() # PutElevator | The new values of the elevator

try:
    # PUT /elevators/{guid}
    api_response = api_instance.elevators_guid_put(authorization, accept_language, guid, elevator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorsApi->elevators_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **elevator** | [**PutElevator**](PutElevator.md)| The new values of the elevator | 

### Return type

[**GetElevator**](GetElevator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elevators_post**
> GetElevators elevators_post(authorization, accept_language, elevators)

POST /elevators

Add a new elevator to the fleet

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ElevatorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
elevators = mir.PostElevators() # PostElevators | The details of the elevators

try:
    # POST /elevators
    api_response = api_instance.elevators_post(authorization, accept_language, elevators)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorsApi->elevators_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **elevators** | [**PostElevators**](PostElevators.md)| The details of the elevators | 

### Return type

[**GetElevators**](GetElevators.md)

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
api_instance = mir.ElevatorsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
session_id = 'session_id_example' # str | The session_id to search for

try:
    # GET /sessions/{session_id}/elevators
    api_response = api_instance.sessions_session_id_elevators_get(authorization, accept_language, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevatorsApi->sessions_session_id_elevators_get: %s\n" % e)
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

