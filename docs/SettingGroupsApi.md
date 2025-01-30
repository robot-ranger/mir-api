# mir.SettingGroupsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setting_groups_get**](SettingGroupsApi.md#setting_groups_get) | **GET** /setting_groups | GET /setting_groups
[**setting_groups_id_get**](SettingGroupsApi.md#setting_groups_id_get) | **GET** /setting_groups/{id} | GET /setting_groups/{id}
[**setting_groups_settings_group_id_settings_advanced_get**](SettingGroupsApi.md#setting_groups_settings_group_id_settings_advanced_get) | **GET** /setting_groups/{settings_group_id}/settings/advanced | GET /setting_groups/{settings_group_id}/settings/advanced
[**setting_groups_settings_group_id_settings_get**](SettingGroupsApi.md#setting_groups_settings_group_id_settings_get) | **GET** /setting_groups/{settings_group_id}/settings | GET /setting_groups/{settings_group_id}/settings


# **setting_groups_get**
> list[GetSettingGroups] setting_groups_get(authorization, accept_language)

GET /setting_groups

Retrieve a list with the settings groups

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /setting_groups
    api_response = api_instance.setting_groups_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingGroupsApi->setting_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSettingGroups]**](GetSettingGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_groups_id_get**
> GetSettingGroup setting_groups_id_get(authorization, accept_language, id)

GET /setting_groups/{id}

Retrieve the details about the settings group with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 'id_example' # str | The id to search for

try:
    # GET /setting_groups/{id}
    api_response = api_instance.setting_groups_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingGroupsApi->setting_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **str**| The id to search for | 

### Return type

[**GetSettingGroup**](GetSettingGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_groups_settings_group_id_settings_advanced_get**
> list[GetSettingGroupAdvancedSettings] setting_groups_settings_group_id_settings_advanced_get(authorization, accept_language, settings_group_id)

GET /setting_groups/{settings_group_id}/settings/advanced

Retrieve the list of advanced settings from the settings group with the specified settings group ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
settings_group_id = 56 # int | The settings_group_id to search for

try:
    # GET /setting_groups/{settings_group_id}/settings/advanced
    api_response = api_instance.setting_groups_settings_group_id_settings_advanced_get(authorization, accept_language, settings_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingGroupsApi->setting_groups_settings_group_id_settings_advanced_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **settings_group_id** | **int**| The settings_group_id to search for | 

### Return type

[**list[GetSettingGroupAdvancedSettings]**](GetSettingGroupAdvancedSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_groups_settings_group_id_settings_get**
> list[GetSettingGroupSettings] setting_groups_settings_group_id_settings_get(authorization, accept_language, settings_group_id)

GET /setting_groups/{settings_group_id}/settings

Retrieve the list of settings from the settings group with the specified settings group ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingGroupsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
settings_group_id = 56 # int | The settings_group_id to search for

try:
    # GET /setting_groups/{settings_group_id}/settings
    api_response = api_instance.setting_groups_settings_group_id_settings_get(authorization, accept_language, settings_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingGroupsApi->setting_groups_settings_group_id_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **settings_group_id** | **int**| The settings_group_id to search for | 

### Return type

[**list[GetSettingGroupSettings]**](GetSettingGroupSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

