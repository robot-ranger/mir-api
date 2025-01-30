# mir.CartTypesApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cart_types_get**](CartTypesApi.md#cart_types_get) | **GET** /cart_types | GET /cart_types
[**cart_types_guid_delete**](CartTypesApi.md#cart_types_guid_delete) | **DELETE** /cart_types/{guid} | DELETE /cart_types/{guid}
[**cart_types_guid_get**](CartTypesApi.md#cart_types_guid_get) | **GET** /cart_types/{guid} | GET /cart_types/{guid}
[**cart_types_guid_put**](CartTypesApi.md#cart_types_guid_put) | **PUT** /cart_types/{guid} | PUT /cart_types/{guid}
[**cart_types_post**](CartTypesApi.md#cart_types_post) | **POST** /cart_types | POST /cart_types


# **cart_types_get**
> list[GetCartTypes] cart_types_get(authorization, accept_language)

GET /cart_types

Retrieve the list of cart types

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartTypesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /cart_types
    api_response = api_instance.cart_types_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartTypesApi->cart_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetCartTypes]**](GetCartTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_guid_delete**
> cart_types_guid_delete(authorization, accept_language, guid)

DELETE /cart_types/{guid}

Erase the cart type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartTypesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /cart_types/{guid}
    api_instance.cart_types_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling CartTypesApi->cart_types_guid_delete: %s\n" % e)
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

# **cart_types_guid_get**
> GetCartType cart_types_guid_get(authorization, accept_language, guid)

GET /cart_types/{guid}

Retrieve the details about the cart type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartTypesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /cart_types/{guid}
    api_response = api_instance.cart_types_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartTypesApi->cart_types_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetCartType**](GetCartType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_guid_put**
> GetCartType cart_types_guid_put(authorization, accept_language, guid, cart_type)

PUT /cart_types/{guid}

Modify the values of the cart type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartTypesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
cart_type = mir.PutCartType() # PutCartType | The new values of the cart_type

try:
    # PUT /cart_types/{guid}
    api_response = api_instance.cart_types_guid_put(authorization, accept_language, guid, cart_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartTypesApi->cart_types_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **cart_type** | [**PutCartType**](PutCartType.md)| The new values of the cart_type | 

### Return type

[**GetCartType**](GetCartType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_post**
> GetCartTypes cart_types_post(authorization, accept_language, cart_types)

POST /cart_types

Add a new cart type

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartTypesApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
cart_types = mir.PostCartTypes() # PostCartTypes | The details of the cart_types

try:
    # POST /cart_types
    api_response = api_instance.cart_types_post(authorization, accept_language, cart_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartTypesApi->cart_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **cart_types** | [**PostCartTypes**](PostCartTypes.md)| The details of the cart_types | 

### Return type

[**GetCartTypes**](GetCartTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

