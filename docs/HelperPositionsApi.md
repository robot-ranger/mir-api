# mir.HelperPositionsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positions_parent_guid_helper_positions_get**](HelperPositionsApi.md#positions_parent_guid_helper_positions_get) | **GET** /positions/{parent_guid}/helper_positions | GET /positions/{parent_guid}/helper_positions


# **positions_parent_guid_helper_positions_get**
> list[GetHelperPositions] positions_parent_guid_helper_positions_get(authorization, accept_language, parent_guid)

GET /positions/{parent_guid}/helper_positions

Retrieve the list of helper positions for the position with the specified parent GUID. Only Charging Stations, V markers, VL markers, Shelf and Trolley positions have helper positions

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.HelperPositionsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
parent_guid = 'parent_guid_example' # str | The parent_guid to search for

try:
    # GET /positions/{parent_guid}/helper_positions
    api_response = api_instance.positions_parent_guid_helper_positions_get(authorization, accept_language, parent_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelperPositionsApi->positions_parent_guid_helper_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **parent_guid** | **str**| The parent_guid to search for | 

### Return type

[**list[GetHelperPositions]**](GetHelperPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

