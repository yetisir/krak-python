# openapi_client.BoreholesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boreholes_create**](BoreholesApi.md#boreholes_create) | **POST** /boreholes/ | Create a new borehole
[**boreholes_delete**](BoreholesApi.md#boreholes_delete) | **DELETE** /boreholes/{borehole_id} | Delete a borehole
[**boreholes_read_all**](BoreholesApi.md#boreholes_read_all) | **GET** /boreholes/ | Read all boreholes in db, sorted by id
[**boreholes_read_one**](BoreholesApi.md#boreholes_read_one) | **GET** /boreholes/{borehole_id} | Read one borehole
[**boreholes_update**](BoreholesApi.md#boreholes_update) | **PUT** /boreholes/{borehole_id} | Update a borehole


# **boreholes_create**
> Boreholes boreholes_create(boreholes)

Create a new borehole

Create a new borehole

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
    api_instance = openapi_client.BoreholesApi(api_client)
    boreholes = openapi_client.Boreholes() # Boreholes | Borehole to create

    try:
        # Create a new borehole
        api_response = api_instance.boreholes_create(boreholes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholesApi->boreholes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholes** | [**Boreholes**](Boreholes.md)| Borehole to create | 

### Return type

[**Boreholes**](Boreholes.md)

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

# **boreholes_delete**
> boreholes_delete(borehole_id)

Delete a borehole

Delete a borehole

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
    api_instance = openapi_client.BoreholesApi(api_client)
    borehole_id = 56 # int | Id of the borehole to get

    try:
        # Delete a borehole
        api_instance.boreholes_delete(borehole_id)
    except ApiException as e:
        print("Exception when calling BoreholesApi->boreholes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of the borehole to get | 

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

# **boreholes_read_all**
> list[Boreholes] boreholes_read_all()

Read all boreholes in db, sorted by id

Read all boreholes in db, sorted by id

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
    api_instance = openapi_client.BoreholesApi(api_client)
    
    try:
        # Read all boreholes in db, sorted by id
        api_response = api_instance.boreholes_read_all()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholesApi->boreholes_read_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Boreholes]**](Boreholes.md)

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

# **boreholes_read_one**
> Boreholes boreholes_read_one(borehole_id)

Read one borehole

Read one borehole

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
    api_instance = openapi_client.BoreholesApi(api_client)
    borehole_id = 56 # int | Id of the borehole to get

    try:
        # Read one borehole
        api_response = api_instance.boreholes_read_one(borehole_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholesApi->boreholes_read_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of the borehole to get | 

### Return type

[**Boreholes**](Boreholes.md)

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

# **boreholes_update**
> Boreholes boreholes_update(borehole_id, boreholes=boreholes)

Update a borehole

Update a borehole

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
    api_instance = openapi_client.BoreholesApi(api_client)
    borehole_id = 56 # int | Id of the borehole to get
boreholes = openapi_client.Boreholes() # Boreholes |  (optional)

    try:
        # Update a borehole
        api_response = api_instance.boreholes_update(borehole_id, boreholes=boreholes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoreholesApi->boreholes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **borehole_id** | **int**| Id of the borehole to get | 
 **boreholes** | [**Boreholes**](Boreholes.md)|  | [optional] 

### Return type

[**Boreholes**](Boreholes.md)

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

