# mir.DefinitionApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**missions_guid_definition_get**](DefinitionApi.md#missions_guid_definition_get) | **GET** /missions/{guid}/definition | GET /missions/{guid}/definition


# **missions_guid_definition_get**
> list[GetMissionDefinition] missions_guid_definition_get(authorization, accept_language, guid)

GET /missions/{guid}/definition

Retrieve the mission with the specified GUID as an action definition that can be inserted in another mission

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.DefinitionApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /missions/{guid}/definition
    api_response = api_instance.missions_guid_definition_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefinitionApi->missions_guid_definition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**list[GetMissionDefinition]**](GetMissionDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

