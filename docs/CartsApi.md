# mir.CartsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**carts_get**](CartsApi.md#carts_get) | **GET** /carts | GET /carts
[**carts_guid_delete**](CartsApi.md#carts_guid_delete) | **DELETE** /carts/{guid} | DELETE /carts/{guid}
[**carts_guid_get**](CartsApi.md#carts_guid_get) | **GET** /carts/{guid} | GET /carts/{guid}
[**carts_guid_put**](CartsApi.md#carts_guid_put) | **PUT** /carts/{guid} | PUT /carts/{guid}
[**carts_post**](CartsApi.md#carts_post) | **POST** /carts | POST /carts


# **carts_get**
> list[GetCarts] carts_get(authorization, accept_language)

GET /carts

Retrieve the list of carts

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /carts
    api_response = api_instance.carts_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->carts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetCarts]**](GetCarts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_guid_delete**
> carts_guid_delete(authorization, accept_language, guid)

DELETE /carts/{guid}

Erase the cart with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /carts/{guid}
    api_instance.carts_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling CartsApi->carts_guid_delete: %s\n" % e)
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

# **carts_guid_get**
> GetCart carts_guid_get(authorization, accept_language, guid)

GET /carts/{guid}

Retrieve the details about the cart with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /carts/{guid}
    api_response = api_instance.carts_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->carts_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetCart**](GetCart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_guid_put**
> GetCart carts_guid_put(authorization, accept_language, guid, cart)

PUT /carts/{guid}

Modify the values of the cart with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
cart = mir.PutCart() # PutCart | The new values of the cart

try:
    # PUT /carts/{guid}
    api_response = api_instance.carts_guid_put(authorization, accept_language, guid, cart)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->carts_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **cart** | [**PutCart**](PutCart.md)| The new values of the cart | 

### Return type

[**GetCart**](GetCart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_post**
> GetCarts carts_post(authorization, accept_language, carts)

POST /carts

Add a new cart

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
carts = mir.PostCarts() # PostCarts | The details of the carts

try:
    # POST /carts
    api_response = api_instance.carts_post(authorization, accept_language, carts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->carts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **carts** | [**PostCarts**](PostCarts.md)| The details of the carts | 

### Return type

[**GetCarts**](GetCarts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

