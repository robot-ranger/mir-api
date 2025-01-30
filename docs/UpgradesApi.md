# mir.UpgradesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_upgrades_get**](UpgradesApi.md#software_upgrades_get) | **GET** /software/upgrades | GET /software/upgrades
[**software_upgrades_guid_delete**](UpgradesApi.md#software_upgrades_guid_delete) | **DELETE** /software/upgrades/{guid} | DELETE /software/upgrades/{guid}
[**software_upgrades_guid_get**](UpgradesApi.md#software_upgrades_guid_get) | **GET** /software/upgrades/{guid} | GET /software/upgrades/{guid}
[**software_upgrades_guid_post**](UpgradesApi.md#software_upgrades_guid_post) | **POST** /software/upgrades/{guid} | POST /software/upgrades/{guid}
[**software_upgrades_post**](UpgradesApi.md#software_upgrades_post) | **POST** /software/upgrades | POST /software/upgrades


# **software_upgrades_get**
> list[GetSoftwareUpgrades] software_upgrades_get(authorization, accept_language)

GET /software/upgrades

Retrieve a list of the software upgrade performed

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UpgradesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /software/upgrades
    api_response = api_instance.software_upgrades_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradesApi->software_upgrades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetSoftwareUpgrades]**](GetSoftwareUpgrades.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_delete**
> software_upgrades_guid_delete(authorization, accept_language, guid)

DELETE /software/upgrades/{guid}

Erase the upgrade file with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UpgradesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /software/upgrades/{guid}
    api_instance.software_upgrades_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling UpgradesApi->software_upgrades_guid_delete: %s\n" % e)
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

# **software_upgrades_guid_get**
> GetSoftwareUpgrade software_upgrades_guid_get(authorization, accept_language, guid)

GET /software/upgrades/{guid}

Retrieve the details of the software upgrade with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UpgradesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /software/upgrades/{guid}
    api_response = api_instance.software_upgrades_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradesApi->software_upgrades_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetSoftwareUpgrade**](GetSoftwareUpgrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_post**
> GetSoftwareUpgrade software_upgrades_guid_post(authorization, accept_language, guid)

POST /software/upgrades/{guid}

Upgrade to the version of the upgrade file with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UpgradesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to add the new resource to

try:
    # POST /software/upgrades/{guid}
    api_response = api_instance.software_upgrades_guid_post(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradesApi->software_upgrades_guid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to add the new resource to | 

### Return type

[**GetSoftwareUpgrade**](GetSoftwareUpgrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_post**
> GetSoftwareUpgrades software_upgrades_post(authorization, accept_language)

POST /software/upgrades

Upgrade with the provided upgrade file

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.UpgradesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # POST /software/upgrades
    api_response = api_instance.software_upgrades_post(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradesApi->software_upgrades_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetSoftwareUpgrades**](GetSoftwareUpgrades.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

