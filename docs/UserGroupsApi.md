# mir.UserGroupsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_groups_get**](UserGroupsApi.md#user_groups_get) | **GET** /user_groups | GET /user_groups
[**user_groups_guid_delete**](UserGroupsApi.md#user_groups_guid_delete) | **DELETE** /user_groups/{guid} | DELETE /user_groups/{guid}
[**user_groups_guid_get**](UserGroupsApi.md#user_groups_guid_get) | **GET** /user_groups/{guid} | GET /user_groups/{guid}
[**user_groups_guid_put**](UserGroupsApi.md#user_groups_guid_put) | **PUT** /user_groups/{guid} | PUT /user_groups/{guid}
[**user_groups_post**](UserGroupsApi.md#user_groups_post) | **POST** /user_groups | POST /user_groups
[**user_groups_user_group_guid_permissions_get**](UserGroupsApi.md#user_groups_user_group_guid_permissions_get) | **GET** /user_groups/{user_group_guid}/permissions | GET /user_groups/{user_group_guid}/permissions
[**user_groups_user_group_guid_permissions_post**](UserGroupsApi.md#user_groups_user_group_guid_permissions_post) | **POST** /user_groups/{user_group_guid}/permissions | POST /user_groups/{user_group_guid}/permissions


# **user_groups_get**
> list[GetUserGroups] user_groups_get(authorization, accept_language)

GET /user_groups

Retrieve the list of user groups

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UserGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /user_groups
    api_response = api_instance.user_groups_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetUserGroups]**](GetUserGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_guid_delete**
> user_groups_guid_delete(authorization, accept_language, guid)

DELETE /user_groups/{guid}

Erase the user group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UserGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /user_groups/{guid}
    api_instance.user_groups_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_guid_delete: %s\n" % e)
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

# **user_groups_guid_get**
> GetUserGroup user_groups_guid_get(authorization, accept_language, guid)

GET /user_groups/{guid}

Retrieve the details about the user group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UserGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /user_groups/{guid}
    api_response = api_instance.user_groups_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetUserGroup**](GetUserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_guid_put**
> GetUserGroup user_groups_guid_put(authorization, accept_language, guid, user_group)

PUT /user_groups/{guid}

Modify the values of the user group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UserGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
user_group = mir.PutUserGroup() # PutUserGroup | The new values of the user_group

try:
    # PUT /user_groups/{guid}
    api_response = api_instance.user_groups_guid_put(authorization, accept_language, guid, user_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **user_group** | [**PutUserGroup**](PutUserGroup.md)| The new values of the user_group | 

### Return type

[**GetUserGroup**](GetUserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_post**
> GetUserGroups user_groups_post(authorization, accept_language, user_groups)

POST /user_groups

Add a new user group

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UserGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
user_groups = mir.PostUserGroups() # PostUserGroups | The details of the user_groups

try:
    # POST /user_groups
    api_response = api_instance.user_groups_post(authorization, accept_language, user_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **user_groups** | [**PostUserGroups**](PostUserGroups.md)| The details of the user_groups | 

### Return type

[**GetUserGroups**](GetUserGroups.md)

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
api_instance = mir.UserGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
user_group_guid = 'user_group_guid_example' # str | The user_group_guid to search for

try:
    # GET /user_groups/{user_group_guid}/permissions
    api_response = api_instance.user_groups_user_group_guid_permissions_get(authorization, accept_language, user_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_user_group_guid_permissions_get: %s\n" % e)
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
api_instance = mir.UserGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
user_group_guid = 'user_group_guid_example' # str | The user_group_guid to add the new resource to
user_group_permission = mir.PostUserGroupPermission() # PostUserGroupPermission | The details of the user_group_permission

try:
    # POST /user_groups/{user_group_guid}/permissions
    api_response = api_instance.user_groups_user_group_guid_permissions_post(authorization, accept_language, user_group_guid, user_group_permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_groups_user_group_guid_permissions_post: %s\n" % e)
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

