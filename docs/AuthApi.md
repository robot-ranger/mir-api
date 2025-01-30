# mir.AuthApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_auth_delete**](AuthApi.md#users_auth_delete) | **DELETE** /users/auth | DELETE /users/auth
[**users_auth_post**](AuthApi.md#users_auth_post) | **POST** /users/auth | POST /users/auth


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
api_instance = mir.AuthApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # DELETE /users/auth
    api_instance.users_auth_delete(authorization, accept_language)
except ApiException as e:
    print("Exception when calling AuthApi->users_auth_delete: %s\n" % e)
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
api_instance = mir.AuthApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # POST /users/auth
    api_response = api_instance.users_auth_post(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->users_auth_post: %s\n" % e)
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

