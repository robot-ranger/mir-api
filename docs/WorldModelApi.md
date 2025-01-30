# mir.WorldModelApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**world_model_get**](WorldModelApi.md#world_model_get) | **GET** /world_model | GET /world_model
[**world_model_post**](WorldModelApi.md#world_model_post) | **POST** /world_model | POST /world_model


# **world_model_get**
> GetWorldModel world_model_get(authorization, accept_language)

GET /world_model

Retrieve the information about the needed resources from the robot

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WorldModelApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)

try:
    # GET /world_model
    api_response = api_instance.world_model_get(authorization, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldModelApi->world_model_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]

### Return type

[**GetWorldModel**](GetWorldModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **world_model_post**
> GetWorldModel world_model_post(authorization, accept_language, world_model)

POST /world_model

Upload the world model with the existing robots, resources and positions and their respective locks

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WorldModelApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
world_model = mir.PostWorldModel() # PostWorldModel | The details of the world_model

try:
    # POST /world_model
    api_response = api_instance.world_model_post(authorization, accept_language, world_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldModelApi->world_model_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **world_model** | [**PostWorldModel**](PostWorldModel.md)| The details of the world_model | 

### Return type

[**GetWorldModel**](GetWorldModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

