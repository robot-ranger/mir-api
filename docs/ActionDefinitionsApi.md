# mir.ActionDefinitionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_action_definitions_action_type_get**](ActionDefinitionsApi.md#zones_action_definitions_action_type_get) | **GET** /zones/action_definitions/{action_type} | GET /zones/action_definitions/{action_type}
[**zones_action_definitions_get**](ActionDefinitionsApi.md#zones_action_definitions_get) | **GET** /zones/action_definitions | GET /zones/action_definitions


# **zones_action_definitions_action_type_get**
> GetZoneActionDefinition zones_action_definitions_action_type_get(authorization, accept_language, action_type)

GET /zones/action_definitions/{action_type}

Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionDefinitionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
action_type = 'action_type_example' # str | The action_type to search for

try:
    # GET /zones/action_definitions/{action_type}
    api_response = api_instance.zones_action_definitions_action_type_get(authorization, accept_language, action_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionDefinitionsApi->zones_action_definitions_action_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **action_type** | **str**| The action_type to search for | 

### Return type

[**GetZoneActionDefinition**](GetZoneActionDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_action_definitions_get**
> GetZoneActionDefinitions zones_action_definitions_get(authorization, accept_language)

GET /zones/action_definitions

Retrieve definitions of zone actions and their parameters

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ActionDefinitionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /zones/action_definitions
    api_response = api_instance.zones_action_definitions_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionDefinitionsApi->zones_action_definitions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetZoneActionDefinitions**](GetZoneActionDefinitions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

