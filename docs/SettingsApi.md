# mir.SettingsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setting_groups_settings_group_id_settings_advanced_get**](SettingsApi.md#setting_groups_settings_group_id_settings_advanced_get) | **GET** /setting_groups/{settings_group_id}/settings/advanced | GET /setting_groups/{settings_group_id}/settings/advanced
[**setting_groups_settings_group_id_settings_get**](SettingsApi.md#setting_groups_settings_group_id_settings_get) | **GET** /setting_groups/{settings_group_id}/settings | GET /setting_groups/{settings_group_id}/settings
[**settings_advanced_get**](SettingsApi.md#settings_advanced_get) | **GET** /settings/advanced | GET /settings/advanced
[**settings_advanced_id_get**](SettingsApi.md#settings_advanced_id_get) | **GET** /settings/advanced/{id} | GET /settings/advanced/{id}
[**settings_advanced_id_put**](SettingsApi.md#settings_advanced_id_put) | **PUT** /settings/advanced/{id} | PUT /settings/advanced/{id}
[**settings_get**](SettingsApi.md#settings_get) | **GET** /settings | GET /settings
[**settings_id_get**](SettingsApi.md#settings_id_get) | **GET** /settings/{id} | GET /settings/{id}
[**settings_id_put**](SettingsApi.md#settings_id_put) | **PUT** /settings/{id} | PUT /settings/{id}


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
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
settings_group_id = 56 # int | The settings_group_id to search for

try:
    # GET /setting_groups/{settings_group_id}/settings/advanced
    api_response = api_instance.setting_groups_settings_group_id_settings_advanced_get(authorization, accept_language, settings_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->setting_groups_settings_group_id_settings_advanced_get: %s\n" % e)
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
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
settings_group_id = 56 # int | The settings_group_id to search for

try:
    # GET /setting_groups/{settings_group_id}/settings
    api_response = api_instance.setting_groups_settings_group_id_settings_get(authorization, accept_language, settings_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->setting_groups_settings_group_id_settings_get: %s\n" % e)
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

# **settings_advanced_get**
> list[GetSettingsAdvanced] settings_advanced_get(authorization, accept_language)

GET /settings/advanced

Retrieve the list with the advanced settings

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /settings/advanced
    api_response = api_instance.settings_advanced_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_advanced_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSettingsAdvanced]**](GetSettingsAdvanced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_advanced_id_get**
> GetSettingAdvanced settings_advanced_id_get(authorization, accept_language, id)

GET /settings/advanced/{id}

Retrieve the details of the advanced setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 'id_example' # str | The id to search for

try:
    # GET /settings/advanced/{id}
    api_response = api_instance.settings_advanced_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_advanced_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **str**| The id to search for | 

### Return type

[**GetSettingAdvanced**](GetSettingAdvanced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_advanced_id_put**
> GetSettingAdvanced settings_advanced_id_put(authorization, accept_language, id, setting_advanced)

PUT /settings/advanced/{id}

Modify the values of the advanced setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 'id_example' # str | The id to modify
setting_advanced = mir.PutSettingAdvanced() # PutSettingAdvanced | The new values of the setting_advanced

try:
    # PUT /settings/advanced/{id}
    api_response = api_instance.settings_advanced_id_put(authorization, accept_language, id, setting_advanced)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_advanced_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **str**| The id to modify | 
 **setting_advanced** | [**PutSettingAdvanced**](PutSettingAdvanced.md)| The new values of the setting_advanced | 

### Return type

[**GetSettingAdvanced**](GetSettingAdvanced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_get**
> list[GetSettings] settings_get(authorization, accept_language)

GET /settings

Retrieve a list with the settings

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /settings
    api_response = api_instance.settings_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSettings]**](GetSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_id_get**
> GetSetting settings_id_get(authorization, accept_language, id)

GET /settings/{id}

Retrieve the details of the setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 'id_example' # str | The id to search for

try:
    # GET /settings/{id}
    api_response = api_instance.settings_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **str**| The id to search for | 

### Return type

[**GetSetting**](GetSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_id_put**
> GetSetting settings_id_put(authorization, accept_language, id, setting)

PUT /settings/{id}

Modify the values of the setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SettingsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 'id_example' # str | The id to modify
setting = mir.PutSetting() # PutSetting | The new values of the setting

try:
    # PUT /settings/{id}
    api_response = api_instance.settings_id_put(authorization, accept_language, id, setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **str**| The id to modify | 
 **setting** | [**PutSetting**](PutSetting.md)| The new values of the setting | 

### Return type

[**GetSetting**](GetSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

