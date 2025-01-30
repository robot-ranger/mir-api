# mir.BackupsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_backups_get**](BackupsApi.md#software_backups_get) | **GET** /software/backups | GET /software/backups
[**software_backups_guid_delete**](BackupsApi.md#software_backups_guid_delete) | **DELETE** /software/backups/{guid} | DELETE /software/backups/{guid}
[**software_backups_guid_get**](BackupsApi.md#software_backups_guid_get) | **GET** /software/backups/{guid} | GET /software/backups/{guid}
[**software_backups_guid_post**](BackupsApi.md#software_backups_guid_post) | **POST** /software/backups/{guid} | POST /software/backups/{guid}
[**software_backups_post**](BackupsApi.md#software_backups_post) | **POST** /software/backups | POST /software/backups


# **software_backups_get**
> list[GetSoftwareBackups] software_backups_get(authorization, accept_language)

GET /software/backups

Retrieve the list with all the software backups

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.BackupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/backups
    api_response = api_instance.software_backups_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupsApi->software_backups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareBackups]**](GetSoftwareBackups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_delete**
> software_backups_guid_delete(authorization, accept_language, guid)

DELETE /software/backups/{guid}

Erase the software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.BackupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /software/backups/{guid}
    api_instance.software_backups_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling BackupsApi->software_backups_guid_delete: %s\n" % e)
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

# **software_backups_guid_get**
> GetSoftwareBackup software_backups_guid_get(authorization, accept_language, guid)

GET /software/backups/{guid}

Retrieve the details about the software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.BackupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /software/backups/{guid}
    api_response = api_instance.software_backups_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupsApi->software_backups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoftwareBackup**](GetSoftwareBackup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_post**
> GetSoftwareBackup software_backups_guid_post(authorization, accept_language, guid)

POST /software/backups/{guid}

If it exists a software backup with the specified GUID it will restore that backup. Otherwise, it will create a software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.BackupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to

try:
    # POST /software/backups/{guid}
    api_response = api_instance.software_backups_guid_post(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupsApi->software_backups_guid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to add the new resource to | 

### Return type

[**GetSoftwareBackup**](GetSoftwareBackup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_post**
> GetSoftwareBackups software_backups_post(authorization, accept_language)

POST /software/backups

Create a new software backup

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.BackupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # POST /software/backups
    api_response = api_instance.software_backups_post(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupsApi->software_backups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSoftwareBackups**](GetSoftwareBackups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

