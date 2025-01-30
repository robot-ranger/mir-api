# mir.PermissionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_get**](PermissionsApi.md#permissions_get) | **GET** /permissions | GET /permissions
[**permissions_guid_delete**](PermissionsApi.md#permissions_guid_delete) | **DELETE** /permissions/{guid} | DELETE /permissions/{guid}
[**permissions_guid_get**](PermissionsApi.md#permissions_guid_get) | **GET** /permissions/{guid} | GET /permissions/{guid}
[**permissions_post**](PermissionsApi.md#permissions_post) | **POST** /permissions | POST /permissions
[**user_groups_user_group_guid_permissions_get**](PermissionsApi.md#user_groups_user_group_guid_permissions_get) | **GET** /user_groups/{user_group_guid}/permissions | GET /user_groups/{user_group_guid}/permissions
[**user_groups_user_group_guid_permissions_post**](PermissionsApi.md#user_groups_user_group_guid_permissions_post) | **POST** /user_groups/{user_group_guid}/permissions | POST /user_groups/{user_group_guid}/permissions
[**users_me_permissions_get**](PermissionsApi.md#users_me_permissions_get) | **GET** /users/me/permissions | GET /users/me/permissions


# **permissions_get**
> list[GetPermissions] permissions_get(authorization, accept_language)

GET /permissions

TODO

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PermissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /permissions
    api_response = api_instance.permissions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetPermissions]**](GetPermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_guid_delete**
> permissions_guid_delete(authorization, accept_language, guid)

DELETE /permissions/{guid}

Erase the permission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PermissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /permissions/{guid}
    api_instance.permissions_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling PermissionsApi->permissions_guid_delete: %s\n" % e)
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

# **permissions_guid_get**
> GetPermission permissions_guid_get(authorization, accept_language, guid)

GET /permissions/{guid}

Retrieve the details about the permission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PermissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /permissions/{guid}
    api_response = api_instance.permissions_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->permissions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetPermission**](GetPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_post**
> GetPermissions permissions_post(authorization, accept_language, permissions)

POST /permissions

TODO

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PermissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
permissions = mir.PostPermissions() # PostPermissions | The details of the permissions

try:
    # POST /permissions
    api_response = api_instance.permissions_post(authorization, accept_language, permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->permissions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **permissions** | [**PostPermissions**](PostPermissions.md)| The details of the permissions | 

### Return type

[**GetPermissions**](GetPermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_user_group_guid_permissions_get**
> list[GetUserGroupPermission] user_groups_user_group_guid_permissions_get(authorization, accept_language, user_group_guid)

GET /user_groups/{user_group_guid}/permissions

Retrieve the list of permissions of the user group with the specified group GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PermissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
user_group_guid = 'user_group_guid_example' # str | The user_group_guid to search for

try:
    # GET /user_groups/{user_group_guid}/permissions
    api_response = api_instance.user_groups_user_group_guid_permissions_get(authorization, accept_language, user_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->user_groups_user_group_guid_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **user_group_guid** | **str**| The user_group_guid to search for | 

### Return type

[**list[GetUserGroupPermission]**](GetUserGroupPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_user_group_guid_permissions_post**
> GetUserGroupPermission user_groups_user_group_guid_permissions_post(authorization, accept_language, user_group_guid, user_group_permission)

POST /user_groups/{user_group_guid}/permissions

Add a new permission to the group with the specified group GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PermissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
user_group_guid = 'user_group_guid_example' # str | The user_group_guid to add the new resource to
user_group_permission = mir.PostUserGroupPermission() # PostUserGroupPermission | The details of the user_group_permission

try:
    # POST /user_groups/{user_group_guid}/permissions
    api_response = api_instance.user_groups_user_group_guid_permissions_post(authorization, accept_language, user_group_guid, user_group_permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->user_groups_user_group_guid_permissions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **user_group_guid** | **str**| The user_group_guid to add the new resource to | 
 **user_group_permission** | [**PostUserGroupPermission**](PostUserGroupPermission.md)| The details of the user_group_permission | 

### Return type

[**GetUserGroupPermission**](GetUserGroupPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_permissions_get**
> list[GetUserMePermissions] users_me_permissions_get(authorization, accept_language)

GET /users/me/permissions

Retrieve the permission of the user currently authorized in the API

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.PermissionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me/permissions
    api_response = api_instance.users_me_permissions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->users_me_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetUserMePermissions]**](GetUserMePermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

