# openapi_client.CorePhotosApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**core_photos_create**](CorePhotosApi.md#core_photos_create) | **POST** /boreholes/{borehole_id}/core_photos/ | Create a new core photo
[**core_photos_delete**](CorePhotosApi.md#core_photos_delete) | **DELETE** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Delete a core_photo
[**core_photos_read_all**](CorePhotosApi.md#core_photos_read_all) | **GET** /boreholes/{borehole_id}/core_photos/ | Read all core photo ids in db, sorted by id
[**core_photos_read_one**](CorePhotosApi.md#core_photos_read_one) | **GET** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Read one core photo
[**core_photos_update**](CorePhotosApi.md#core_photos_update) | **PUT** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Update a core_photo


# **core_photos_create**
> CorePhotos core_photos_create(borehole_id, photo, data)

Create a new core photo

Create a new core photo

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CorePhotosApi(api_client)
    borehole_id = 56 # int | Id of Borehole
photo = '/path/to/file' # file | 
data = openapi_client.CorePhotosData() # CorePhotosData | 

    try:
        # Create a new core photo
        api_response = api_instance.core_photos_create(borehole_id, photo, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorePhotosApi->core_photos_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of Borehole | 
 **photo** | **file**|  | 
 **data** | [**CorePhotosData**](CorePhotosData.md)|  | 

### Return type

[**CorePhotos**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created core photo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_photos_delete**
> core_photos_delete(borehole_id, core_photo_id)

Delete a core_photo

Delete a core_photo

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CorePhotosApi(api_client)
    borehole_id = 56 # int | Id of Borehole
core_photo_id = 56 # int | Id of Borehole

    try:
        # Delete a core_photo
        api_instance.core_photos_delete(borehole_id, core_photo_id)
    except ApiException as e:
        print("Exception when calling CorePhotosApi->core_photos_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of Borehole | 
 **core_photo_id** | **int**| Id of Borehole | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted borehole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_photos_read_all**
> list[CorePhotos] core_photos_read_all(borehole_id)

Read all core photo ids in db, sorted by id

Read all core photo ids in db, sorted by id

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CorePhotosApi(api_client)
    borehole_id = 56 # int | Id of Borehole

    try:
        # Read all core photo ids in db, sorted by id
        api_response = api_instance.core_photos_read_all(borehole_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorePhotosApi->core_photos_read_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of Borehole | 

### Return type

[**list[CorePhotos]**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully read all core photos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_photos_read_one**
> CorePhotos core_photos_read_one(borehole_id, core_photo_id)

Read one core photo

Read one core photo

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CorePhotosApi(api_client)
    borehole_id = 56 # int | Id of Borehole
core_photo_id = 56 # int | Id of Borehole

    try:
        # Read one core photo
        api_response = api_instance.core_photos_read_one(borehole_id, core_photo_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorePhotosApi->core_photos_read_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of Borehole | 
 **core_photo_id** | **int**| Id of Borehole | 

### Return type

[**CorePhotos**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully read core photos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_photos_update**
> CorePhotos core_photos_update(borehole_id, core_photo_id, photo, data)

Update a core_photo

Update a core_photo

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CorePhotosApi(api_client)
    borehole_id = 56 # int | Id of Borehole
core_photo_id = 56 # int | Id of Borehole
photo = '/path/to/file' # file | 
data = openapi_client.CorePhotosData() # CorePhotosData | 

    try:
        # Update a core_photo
        api_response = api_instance.core_photos_update(borehole_id, core_photo_id, photo, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorePhotosApi->core_photos_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of Borehole | 
 **core_photo_id** | **int**| Id of Borehole | 
 **photo** | **file**|  | 
 **data** | [**CorePhotosData**](CorePhotosData.md)|  | 

### Return type

[**CorePhotos**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated borehole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

