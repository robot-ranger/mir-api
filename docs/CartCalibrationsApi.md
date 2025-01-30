# mir.CartCalibrationsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cart_calibrations_get**](CartCalibrationsApi.md#cart_calibrations_get) | **GET** /cart_calibrations | GET /cart_calibrations
[**cart_calibrations_guid_delete**](CartCalibrationsApi.md#cart_calibrations_guid_delete) | **DELETE** /cart_calibrations/{guid} | DELETE /cart_calibrations/{guid}
[**cart_calibrations_guid_get**](CartCalibrationsApi.md#cart_calibrations_guid_get) | **GET** /cart_calibrations/{guid} | GET /cart_calibrations/{guid}
[**cart_calibrations_guid_put**](CartCalibrationsApi.md#cart_calibrations_guid_put) | **PUT** /cart_calibrations/{guid} | PUT /cart_calibrations/{guid}
[**cart_calibrations_post**](CartCalibrationsApi.md#cart_calibrations_post) | **POST** /cart_calibrations | POST /cart_calibrations


# **cart_calibrations_get**
> list[GetCartCalibrations] cart_calibrations_get(authorization, accept_language)

GET /cart_calibrations

Retrieve the list of cart calibrations

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartCalibrationsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /cart_calibrations
    api_response = api_instance.cart_calibrations_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartCalibrationsApi->cart_calibrations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**list[GetCartCalibrations]**](GetCartCalibrations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_guid_delete**
> cart_calibrations_guid_delete(authorization, accept_language, guid)

DELETE /cart_calibrations/{guid}

Erase the cart calibration with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartCalibrationsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /cart_calibrations/{guid}
    api_instance.cart_calibrations_guid_delete(authorization, accept_language, guid)
except ApiException as e:
    print("Exception when calling CartCalibrationsApi->cart_calibrations_guid_delete: %s\n" % e)
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

# **cart_calibrations_guid_get**
> GetCartCalibration cart_calibrations_guid_get(authorization, accept_language, guid)

GET /cart_calibrations/{guid}

Retrieve the details about the cart calibration with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartCalibrationsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to search for

try:
    # GET /cart_calibrations/{guid}
    api_response = api_instance.cart_calibrations_guid_get(authorization, accept_language, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartCalibrationsApi->cart_calibrations_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to search for | 

### Return type

[**GetCartCalibration**](GetCartCalibration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_guid_put**
> GetCartCalibration cart_calibrations_guid_put(authorization, accept_language, guid, cart_calibration)

PUT /cart_calibrations/{guid}

Modify the values of the cart calibration with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartCalibrationsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
guid = 'guid_example' # str | The guid to modify
cart_calibration = mir.PutCartCalibration() # PutCartCalibration | The new values of the cart_calibration

try:
    # PUT /cart_calibrations/{guid}
    api_response = api_instance.cart_calibrations_guid_put(authorization, accept_language, guid, cart_calibration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartCalibrationsApi->cart_calibrations_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **guid** | **str**| The guid to modify | 
 **cart_calibration** | [**PutCartCalibration**](PutCartCalibration.md)| The new values of the cart_calibration | 

### Return type

[**GetCartCalibration**](GetCartCalibration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_post**
> GetCartCalibrations cart_calibrations_post(authorization, accept_language, cart_calibrations)

POST /cart_calibrations

Add a new cart calibration

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.CartCalibrationsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
cart_calibrations = mir.PostCartCalibrations() # PostCartCalibrations | The details of the cart_calibrations

try:
    # POST /cart_calibrations
    api_response = api_instance.cart_calibrations_post(authorization, accept_language, cart_calibrations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartCalibrationsApi->cart_calibrations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **cart_calibrations** | [**PostCartCalibrations**](PostCartCalibrations.md)| The details of the cart_calibrations | 

### Return type

[**GetCartCalibrations**](GetCartCalibrations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

