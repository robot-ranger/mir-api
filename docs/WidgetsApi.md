# mir.WidgetsApi

All URIs are relative to *http://localhost/api/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboards_dashboard_id_widgets_get**](WidgetsApi.md#dashboards_dashboard_id_widgets_get) | **GET** /dashboards/{dashboard_id}/widgets | GET /dashboards/{dashboard_id}/widgets
[**dashboards_dashboard_id_widgets_guid_delete**](WidgetsApi.md#dashboards_dashboard_id_widgets_guid_delete) | **DELETE** /dashboards/{dashboard_id}/widgets/{guid} | DELETE /dashboards/{dashboard_id}/widgets/{guid}
[**dashboards_dashboard_id_widgets_guid_get**](WidgetsApi.md#dashboards_dashboard_id_widgets_guid_get) | **GET** /dashboards/{dashboard_id}/widgets/{guid} | GET /dashboards/{dashboard_id}/widgets/{guid}
[**dashboards_dashboard_id_widgets_guid_put**](WidgetsApi.md#dashboards_dashboard_id_widgets_guid_put) | **PUT** /dashboards/{dashboard_id}/widgets/{guid} | PUT /dashboards/{dashboard_id}/widgets/{guid}
[**dashboards_dashboard_id_widgets_post**](WidgetsApi.md#dashboards_dashboard_id_widgets_post) | **POST** /dashboards/{dashboard_id}/widgets | POST /dashboards/{dashboard_id}/widgets


# **dashboards_dashboard_id_widgets_get**
> list[GetDashboardWidgets] dashboards_dashboard_id_widgets_get(authorization, accept_language, dashboard_id)

GET /dashboards/{dashboard_id}/widgets

Retrieve the list of widgets of the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WidgetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to search for

try:
    # GET /dashboards/{dashboard_id}/widgets
    api_response = api_instance.dashboards_dashboard_id_widgets_get(authorization, accept_language, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->dashboards_dashboard_id_widgets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **dashboard_id** | **str**| The dashboard_id to search for | 

### Return type

[**list[GetDashboardWidgets]**](GetDashboardWidgets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_guid_delete**
> dashboards_dashboard_id_widgets_guid_delete(authorization, accept_language, dashboard_id, guid)

DELETE /dashboards/{dashboard_id}/widgets/{guid}

Erase the widget with the specified GUID from the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WidgetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to delete
guid = 'guid_example' # str | The guid to delete

try:
    # DELETE /dashboards/{dashboard_id}/widgets/{guid}
    api_instance.dashboards_dashboard_id_widgets_guid_delete(authorization, accept_language, dashboard_id, guid)
except ApiException as e:
    print("Exception when calling WidgetsApi->dashboards_dashboard_id_widgets_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **dashboard_id** | **str**| The dashboard_id to delete | 
 **guid** | **str**| The guid to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_guid_get**
> GetDashboardWidget dashboards_dashboard_id_widgets_guid_get(authorization, accept_language, dashboard_id, guid)

GET /dashboards/{dashboard_id}/widgets/{guid}

Retrieve the details about the widget with the specified GUID in the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WidgetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to search for
guid = 'guid_example' # str | The guid to search for

try:
    # GET /dashboards/{dashboard_id}/widgets/{guid}
    api_response = api_instance.dashboards_dashboard_id_widgets_guid_get(authorization, accept_language, dashboard_id, guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->dashboards_dashboard_id_widgets_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **dashboard_id** | **str**| The dashboard_id to search for | 
 **guid** | **str**| The guid to search for | 

### Return type

[**GetDashboardWidget**](GetDashboardWidget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_guid_put**
> GetDashboardWidget dashboards_dashboard_id_widgets_guid_put(authorization, accept_language, dashboard_id, guid, dashboard_widget)

PUT /dashboards/{dashboard_id}/widgets/{guid}

Modify the values of the widget with the specified GUID in the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WidgetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to modify
guid = 'guid_example' # str | The guid to modify
dashboard_widget = mir.PutDashboardWidget() # PutDashboardWidget | The new values of the dashboard_widget

try:
    # PUT /dashboards/{dashboard_id}/widgets/{guid}
    api_response = api_instance.dashboards_dashboard_id_widgets_guid_put(authorization, accept_language, dashboard_id, guid, dashboard_widget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->dashboards_dashboard_id_widgets_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **dashboard_id** | **str**| The dashboard_id to modify | 
 **guid** | **str**| The guid to modify | 
 **dashboard_widget** | [**PutDashboardWidget**](PutDashboardWidget.md)| The new values of the dashboard_widget | 

### Return type

[**GetDashboardWidget**](GetDashboardWidget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_post**
> GetDashboardWidgets dashboards_dashboard_id_widgets_post(authorization, accept_language, dashboard_id, dashboard_widgets)

POST /dashboards/{dashboard_id}/widgets

Add a new widget to the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir
from mir.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mir.WidgetsApi()
authorization = 'authorization_example' # str | Authorization header
accept_language = 'en-US' # str | Language header (default to en-US)
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to add the new resource to
dashboard_widgets = mir.PostDashboardWidgets() # PostDashboardWidgets | The details of the dashboard_widgets

try:
    # POST /dashboards/{dashboard_id}/widgets
    api_response = api_instance.dashboards_dashboard_id_widgets_post(authorization, accept_language, dashboard_id, dashboard_widgets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsApi->dashboards_dashboard_id_widgets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization header | 
 **accept_language** | **str**| Language header | [default to en-US]
 **dashboard_id** | **str**| The dashboard_id to add the new resource to | 
 **dashboard_widgets** | [**PostDashboardWidgets**](PostDashboardWidgets.md)| The details of the dashboard_widgets | 

### Return type

[**GetDashboardWidgets**](GetDashboardWidgets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

