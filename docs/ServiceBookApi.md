# mir.ServiceBookApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_book_get**](ServiceBookApi.md#service_book_get) | **GET** /service_book | GET /service_book
[**service_book_guid_delete**](ServiceBookApi.md#service_book_guid_delete) | **DELETE** /service_book/{guid} | DELETE /service_book/{guid}
[**service_book_guid_get**](ServiceBookApi.md#service_book_guid_get) | **GET** /service_book/{guid} | GET /service_book/{guid}
[**service_book_post**](ServiceBookApi.md#service_book_post) | **POST** /service_book | POST /service_book


# **service_book_get**
> GetServiceBooks service_book_get(authorization, accept_language)

GET /service_book

Retrieve service book entries accessible by user

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ServiceBookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /service_book
    api_response = api_instance.service_book_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceBookApi->service_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetServiceBooks**](GetServiceBooks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_book_guid_delete**
> service_book_guid_delete(authorization, accept_language, guid)

DELETE /service_book/{guid}

Erase the note with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ServiceBookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /service_book/{guid}
    api_instance.service_book_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling ServiceBookApi->service_book_guid_delete: %s\n" % e)
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

# **service_book_guid_get**
> GetServiceBook service_book_guid_get(authorization, accept_language, guid)

GET /service_book/{guid}

Retrieve note with the GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ServiceBookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /service_book/{guid}
    api_response = api_instance.service_book_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceBookApi->service_book_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetServiceBook**](GetServiceBook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_book_post**
> GetServiceBooks service_book_post(authorization, accept_language, service_books)

POST /service_book

Add a service book note

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.ServiceBookApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
service_books = mir.PostServiceBooks() # PostServiceBooks | The details of the service_books

try:
    # POST /service_book
    api_response = api_instance.service_book_post(authorization, accept_language, service_books)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceBookApi->service_book_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **service_books** | [**PostServiceBooks**](PostServiceBooks.md)| The details of the service_books | 

### Return type

[**GetServiceBooks**](GetServiceBooks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

