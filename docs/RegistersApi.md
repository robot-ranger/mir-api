# mir.RegistersApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registers_get**](RegistersApi.md#registers_get) | **GET** /registers | GET /registers
[**registers_id_get**](RegistersApi.md#registers_id_get) | **GET** /registers/{id} | GET /registers/{id}
[**registers_id_post**](RegistersApi.md#registers_id_post) | **POST** /registers/{id} | POST /registers/{id}
[**registers_id_put**](RegistersApi.md#registers_id_put) | **PUT** /registers/{id} | PUT /registers/{id}


# **registers_get**
> list[GetRegisters] registers_get(authorization, accept_language)

GET /registers

Retrieve the list of PLC registers from the robot. Registers 1 to 100 are integers and registers 101-200 are float

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RegistersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /registers
    api_response = api_instance.registers_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistersApi->registers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetRegisters]**](GetRegisters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_id_get**
> GetRegister registers_id_get(authorization, accept_language, id)

GET /registers/{id}

Retrieve the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RegistersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to search for

try:
    # GET /registers/{id}
    api_response = api_instance.registers_id_get(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistersApi->registers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to search for | 

### Return type

[**GetRegister**](GetRegister.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_id_post**
> GetRegister registers_id_post(authorization, accept_language, id, register)

POST /registers/{id}

Modify the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float. Even though this is not a standard use of the POST call it has been included for compatibility purposes

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RegistersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to add the new resource to
register = mir.PostRegister() # PostRegister | The details of the register

try:
    # POST /registers/{id}
    api_response = api_instance.registers_id_post(authorization, accept_language, id, register)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistersApi->registers_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to add the new resource to | 
 **register** | [**PostRegister**](PostRegister.md)| The details of the register | 

### Return type

[**GetRegister**](GetRegister.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_id_put**
> GetRegister registers_id_put(authorization, accept_language, id)

PUT /registers/{id}

Modify the value of the PLC register with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.RegistersApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
id = 56 # int | The id to modify

try:
    # PUT /registers/{id}
    api_response = api_instance.registers_id_put(authorization, accept_language, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistersApi->registers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **id** | **int**| The id to modify | 

### Return type

[**GetRegister**](GetRegister.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

