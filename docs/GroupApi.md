# mir.GroupApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_me_group_get**](GroupApi.md#users_me_group_get) | **GET** /users/me/group | GET /users/me/group


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
api_instance = mir.GroupApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /users/me/group
    api_response = api_instance.users_me_group_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->users_me_group_get: %s\n" % e)
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

