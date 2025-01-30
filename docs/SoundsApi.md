# mir.SoundsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sounds_get**](SoundsApi.md#sounds_get) | **GET** /sounds | GET /sounds
[**sounds_guid_delete**](SoundsApi.md#sounds_guid_delete) | **DELETE** /sounds/{guid} | DELETE /sounds/{guid}
[**sounds_guid_get**](SoundsApi.md#sounds_guid_get) | **GET** /sounds/{guid} | GET /sounds/{guid}
[**sounds_guid_put**](SoundsApi.md#sounds_guid_put) | **PUT** /sounds/{guid} | PUT /sounds/{guid}
[**sounds_guid_stream_get**](SoundsApi.md#sounds_guid_stream_get) | **GET** /sounds/{guid}/stream | GET /sounds/{guid}/stream
[**sounds_post**](SoundsApi.md#sounds_post) | **POST** /sounds | POST /sounds


# **sounds_get**
> list[GetSounds] sounds_get(authorization, accept_language)

GET /sounds

Retrieve the list of sounds

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoundsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /sounds
    api_response = api_instance.sounds_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoundsApi->sounds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSounds]**](GetSounds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_guid_delete**
> sounds_guid_delete(authorization, accept_language, guid)

DELETE /sounds/{guid}

Erase the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoundsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /sounds/{guid}
    api_instance.sounds_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling SoundsApi->sounds_guid_delete: %s\n" % e)
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

# **sounds_guid_get**
> GetSound sounds_guid_get(authorization, accept_language, guid)

GET /sounds/{guid}

Retrieve the details about the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoundsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /sounds/{guid}
    api_response = api_instance.sounds_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoundsApi->sounds_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSound**](GetSound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_guid_put**
> GetSound sounds_guid_put(authorization, accept_language, guid, sound)

PUT /sounds/{guid}

Modify the values of the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoundsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
sound = mir.PutSound() # PutSound | The new values of the sound

try:
    # PUT /sounds/{guid}
    api_response = api_instance.sounds_guid_put(authorization, accept_language, guid, sound)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoundsApi->sounds_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **sound** | [**PutSound**](PutSound.md)| The new values of the sound | 

### Return type

[**GetSound**](GetSound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_guid_stream_get**
> GetSoundStream sounds_guid_stream_get(authorization, accept_language, guid)

GET /sounds/{guid}/stream

Download the sound file of the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoundsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /sounds/{guid}/stream
    api_response = api_instance.sounds_guid_stream_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoundsApi->sounds_guid_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoundStream**](GetSoundStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_post**
> GetSounds sounds_post(authorization, accept_language, sounds)

POST /sounds

Add a new sound

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SoundsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
sounds = mir.PostSounds() # PostSounds | The details of the sounds

try:
    # POST /sounds
    api_response = api_instance.sounds_post(authorization, accept_language, sounds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoundsApi->sounds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **sounds** | [**PostSounds**](PostSounds.md)| The details of the sounds | 

### Return type

[**GetSounds**](GetSounds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

