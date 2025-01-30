# mir.SslApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssl_cert_delete**](SslApi.md#ssl_cert_delete) | **DELETE** /ssl/cert | DELETE /ssl/cert
[**ssl_cert_post**](SslApi.md#ssl_cert_post) | **POST** /ssl/cert | POST /ssl/cert


# **ssl_cert_delete**
> ssl_cert_delete(authorization, accept_language)

DELETE /ssl/cert

Use default self-signed certificate

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SslApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # DELETE /ssl/cert
    api_instance.ssl_cert_delete(authorization, accept_language)
except ApiException as e:
    print("Exception when calling SslApi->ssl_cert_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssl_cert_post**
> GetCert ssl_cert_post(authorization, accept_language, cert)

POST /ssl/cert

Upload new certificate pair

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.SslApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
cert = mir.PostCert() # PostCert | The details of the cert

try:
    # POST /ssl/cert
    api_response = api_instance.ssl_cert_post(authorization, accept_language, cert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslApi->ssl_cert_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **cert** | [**PostCert**](PostCert.md)| The details of the cert | 

### Return type

[**GetCert**](GetCert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

