# mir.UsersApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_auth_delete**](UsersApi.md#users_auth_delete) | **DELETE** /users/auth | DELETE /users/auth
[**users_auth_post**](UsersApi.md#users_auth_post) | **POST** /users/auth | POST /users/auth
[**users_get**](UsersApi.md#users_get) | **GET** /users | GET /users
[**users_guid_delete**](UsersApi.md#users_guid_delete) | **DELETE** /users/{guid} | DELETE /users/{guid}
[**users_guid_get**](UsersApi.md#users_guid_get) | **GET** /users/{guid} | GET /users/{guid}
[**users_guid_put**](UsersApi.md#users_guid_put) | **PUT** /users/{guid} | PUT /users/{guid}
[**users_me_get**](UsersApi.md#users_me_get) | **GET** /users/me | GET /users/me
[**users_me_group_get**](UsersApi.md#users_me_group_get) | **GET** /users/me/group | GET /users/me/group
[**users_me_permissions_get**](UsersApi.md#users_me_permissions_get) | **GET** /users/me/permissions | GET /users/me/permissions
[**users_me_put**](UsersApi.md#users_me_put) | **PUT** /users/me | PUT /users/me
[**users_post**](UsersApi.md#users_post) | **POST** /users | POST /users


# **users_auth_delete**
> users_auth_delete(authorization, accept_language)

DELETE /users/auth

Logout user

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # DELETE /users/auth
    api_instance.users_auth_delete(authorization, accept_language)
except ApiException as e:
    print("Exception when calling UsersApi->users_auth_delete: %s\n" % e)
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

# **users_auth_post**
> GetUsersAuth users_auth_post(authorization, accept_language)

POST /users/auth

Login with user credentials

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # POST /users/auth
    api_response = api_instance.users_auth_post(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetUsersAuth**](GetUsersAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> list[GetUsers] users_get(authorization, accept_language)

GET /users

Retrieve the list of users

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users
    api_response = api_instance.users_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetUsers]**](GetUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_guid_delete**
> users_guid_delete(authorization, accept_language, guid)

DELETE /users/{guid}

Erase the user with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /users/{guid}
    api_instance.users_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling UsersApi->users_guid_delete: %s\n" % e)
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

# **users_guid_get**
> GetUser users_guid_get(authorization, accept_language, guid)

GET /users/{guid}

Retrieve the details about the user with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /users/{guid}
    api_response = api_instance.users_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetUser**](GetUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_guid_put**
> GetUser users_guid_put(authorization, accept_language, guid, user)

PUT /users/{guid}

Modify the values of the user with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
user = mir.PutUser() # PutUser | The new values of the user

try:
    # PUT /users/{guid}
    api_response = api_instance.users_guid_put(authorization, accept_language, guid, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **user** | [**PutUser**](PutUser.md)| The new values of the user | 

### Return type

[**GetUser**](GetUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_get**
> list[GetMe] users_me_get(authorization, accept_language)

GET /users/me

Retrieve the details about the user currently authorized in the API

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me
    api_response = api_instance.users_me_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetMe]**](GetMe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_group_get**
> list[GetUserMeGroup] users_me_group_get(authorization, accept_language)

GET /users/me/group

Retrieve the group of the user currently authorized in the API

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me/group
    api_response = api_instance.users_me_group_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetUserMeGroup]**](GetUserMeGroup.md)

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
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me/permissions
    api_response = api_instance.users_me_permissions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me_permissions_get: %s\n" % e)
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

# **users_me_put**
> GetMe users_me_put(authorization, accept_language, me)

PUT /users/me

Modify the values of the user currently authorized in the API

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
me = mir.PutMe() # PutMe | The new values of the me

try:
    # PUT /users/me
    api_response = api_instance.users_me_put(authorization, accept_language, me)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **me** | [**PutMe**](PutMe.md)| The new values of the me | 

### Return type

[**GetMe**](GetMe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> GetUsers users_post(authorization, accept_language, users)

POST /users

Add a new user

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UsersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
users = mir.PostUsers() # PostUsers | The details of the users

try:
    # POST /users
    api_response = api_instance.users_post(authorization, accept_language, users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **users** | [**PostUsers**](PostUsers.md)| The details of the users | 

### Return type

[**GetUsers**](GetUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

