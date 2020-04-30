# openapi_client.CorePhotosApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**core_photo_create**](CorePhotosApi.md#core_photo_create) | **POST** /core_photo | Create a new core photo
[**core_photo_read_all**](CorePhotosApi.md#core_photo_read_all) | **GET** /core_photo | Read all core photo ids in db, sorted by id


# **core_photo_create**
> CorePhotoOutput core_photo_create(core_photo_input)

Create a new core photo

Create a new core photo

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CorePhotosApi(api_client)
    core_photo_input = openapi_client.CorePhotoInput() # CorePhotoInput | Core photo to create

    try:
        # Create a new core photo
        api_response = api_instance.core_photo_create(core_photo_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorePhotosApi->core_photo_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **core_photo_input** | [**CorePhotoInput**](CorePhotoInput.md)| Core photo to create | 

### Return type

[**CorePhotoOutput**](CorePhotoOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created core photo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_photo_read_all**
> list[CorePhotoOutput] core_photo_read_all()

Read all core photo ids in db, sorted by id

Read all core photo ids in db, sorted by id

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CorePhotosApi(api_client)
    
    try:
        # Read all core photo ids in db, sorted by id
        api_response = api_instance.core_photo_read_all()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorePhotosApi->core_photo_read_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CorePhotoOutput]**](CorePhotoOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully read all core photos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

