# mir.MeApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_me_get**](MeApi.md#users_me_get) | **GET** /users/me | GET /users/me
[**users_me_group_get**](MeApi.md#users_me_group_get) | **GET** /users/me/group | GET /users/me/group
[**users_me_permissions_get**](MeApi.md#users_me_permissions_get) | **GET** /users/me/permissions | GET /users/me/permissions
[**users_me_put**](MeApi.md#users_me_put) | **PUT** /users/me | PUT /users/me


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
api_instance = mir.MeApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me
    api_response = api_instance.users_me_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->users_me_get: %s\n" % e)
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
api_instance = mir.MeApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me/group
    api_response = api_instance.users_me_group_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->users_me_group_get: %s\n" % e)
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
api_instance = mir.MeApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me/permissions
    api_response = api_instance.users_me_permissions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->users_me_permissions_get: %s\n" % e)
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
api_instance = mir.MeApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
me = mir.PutMe() # PutMe | The new values of the me

try:
    # PUT /users/me
    api_response = api_instance.users_me_put(authorization, accept_language, me)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->users_me_put: %s\n" % e)
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

