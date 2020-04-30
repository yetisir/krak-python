# openapi_client.BoreholeApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**borehole_create**](BoreholeApi.md#borehole_create) | **POST** /borehole | Create a new borehole
[**borehole_delete**](BoreholeApi.md#borehole_delete) | **DELETE** /borehole/{borehole_id} | Delete a borehole
[**borehole_read_all**](BoreholeApi.md#borehole_read_all) | **GET** /borehole | Read all boreholes in db, sorted by id
[**borehole_read_one**](BoreholeApi.md#borehole_read_one) | **GET** /borehole/{borehole_id} | Read one borehole
[**borehole_update**](BoreholeApi.md#borehole_update) | **PUT** /borehole/{borehole_id} | Update a borehole


# **borehole_create**
> BoreholeOutput borehole_create(borehole_input)

Create a new borehole

Create a new borehole

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
    api_instance = openapi_client.BoreholeApi(api_client)
    borehole_input = openapi_client.BoreholeInput() # BoreholeInput | Borehole to create

    try:
        # Create a new borehole
        api_response = api_instance.borehole_create(borehole_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholeApi->borehole_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_input** | [**BoreholeInput**](BoreholeInput.md)| Borehole to create | 

### Return type

[**BoreholeOutput**](BoreholeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created borehole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **borehole_delete**
> borehole_delete(borehole_id)

Delete a borehole

Delete a borehole

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
    api_instance = openapi_client.BoreholeApi(api_client)
    borehole_id = 56 # int | Id of the borehole to delete

    try:
        # Delete a borehole
        api_instance.borehole_delete(borehole_id)
    except ApiException as e:
        print("Exception when calling BoreholeApi->borehole_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of the borehole to delete | 

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

# **borehole_read_all**
> list[BoreholeOutput] borehole_read_all()

Read all boreholes in db, sorted by id

Read all boreholes in db, sorted by id

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
    api_instance = openapi_client.BoreholeApi(api_client)
    
    try:
        # Read all boreholes in db, sorted by id
        api_response = api_instance.borehole_read_all()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholeApi->borehole_read_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BoreholeOutput]**](BoreholeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully read boreholes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **borehole_read_one**
> BoreholeOutput borehole_read_one(borehole_id)

Read one borehole

Read one borehole

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
    api_instance = openapi_client.BoreholeApi(api_client)
    borehole_id = 56 # int | Id of the borehole to get

    try:
        # Read one borehole
        api_response = api_instance.borehole_read_one(borehole_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholeApi->borehole_read_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of the borehole to get | 

### Return type

[**BoreholeOutput**](BoreholeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully read borehole from borehole data operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **borehole_update**
> BoreholeOutput borehole_update(borehole_id, borehole_input=borehole_input)

Update a borehole

Update a borehole

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
    api_instance = openapi_client.BoreholeApi(api_client)
    borehole_id = 56 # int | Id of the borehole to update
borehole_input = openapi_client.BoreholeInput() # BoreholeInput |  (optional)

    try:
        # Update a borehole
        api_response = api_instance.borehole_update(borehole_id, borehole_input=borehole_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholeApi->borehole_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of the borehole to update | 
 **borehole_input** | [**BoreholeInput**](BoreholeInput.md)|  | [optional] 

### Return type

[**BoreholeOutput**](BoreholeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated borehole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

