# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SparkJobDefinitionOperations(object):
    """SparkJobDefinitionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_spark_job_definitions_by_workspace(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.SparkJobDefinitionsListResponse"]
        """Lists spark job definitions.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SparkJobDefinitionsListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.synapse.artifacts.models.SparkJobDefinitionsListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkJobDefinitionsListResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_spark_job_definitions_by_workspace.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('SparkJobDefinitionsListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.CloudError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_spark_job_definitions_by_workspace.metadata = {'url': '/sparkJobDefinitions'}  # type: ignore

    def create_or_update_spark_job_definition(
        self,
        spark_job_definition_name,  # type: str
        properties,  # type: "models.SparkJobDefinition"
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SparkJobDefinitionResource"
        """Creates or updates a Spark Job Definition.

        :param spark_job_definition_name: The spark job definition name.
        :type spark_job_definition_name: str
        :param properties: Properties of spark job definition.
        :type properties: ~azure.synapse.artifacts.models.SparkJobDefinition
        :param if_match: ETag of the Spark Job Definition entity.  Should only be specified for update,
         for which it should match existing entity or can be * for unconditional update.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkJobDefinitionResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.SparkJobDefinitionResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkJobDefinitionResource"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _spark_job_definition = models.SparkJobDefinitionResource(properties=properties)
        api_version = "2019-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update_spark_job_definition.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'sparkJobDefinitionName': self._serialize.url("spark_job_definition_name", spark_job_definition_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_spark_job_definition, 'SparkJobDefinitionResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SparkJobDefinitionResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update_spark_job_definition.metadata = {'url': '/sparkJobDefinitions/{sparkJobDefinitionName}'}  # type: ignore

    def get_spark_job_definition(
        self,
        spark_job_definition_name,  # type: str
        if_none_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["models.SparkJobDefinitionResource"]
        """Gets a Spark Job Definition.

        :param spark_job_definition_name: The spark job definition name.
        :type spark_job_definition_name: str
        :param if_none_match: ETag of the Spark Job Definition entity. Should only be specified for
         get. If the ETag matches the existing entity tag, or if * was provided, then no content will be
         returned.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkJobDefinitionResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.SparkJobDefinitionResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.SparkJobDefinitionResource"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_spark_job_definition.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'sparkJobDefinitionName': self._serialize.url("spark_job_definition_name", spark_job_definition_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SparkJobDefinitionResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_spark_job_definition.metadata = {'url': '/sparkJobDefinitions/{sparkJobDefinitionName}'}  # type: ignore

    def delete_spark_job_definition(
        self,
        spark_job_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a Spark Job Definition.

        :param spark_job_definition_name: The spark job definition name.
        :type spark_job_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete_spark_job_definition.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'sparkJobDefinitionName': self._serialize.url("spark_job_definition_name", spark_job_definition_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_spark_job_definition.metadata = {'url': '/sparkJobDefinitions/{sparkJobDefinitionName}'}  # type: ignore

    def _execute_spark_job_definition_initial(
        self,
        spark_job_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SparkBatchJob"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkBatchJob"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"
        accept = "application/json"

        # Construct URL
        url = self._execute_spark_job_definition_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'sparkJobDefinitionName': self._serialize.url("spark_job_definition_name", spark_job_definition_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('SparkBatchJob', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('SparkBatchJob', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _execute_spark_job_definition_initial.metadata = {'url': '/sparkJobDefinitions/{sparkJobDefinitionName}/execute'}  # type: ignore

    def begin_execute_spark_job_definition(
        self,
        spark_job_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.SparkBatchJob"]
        """Executes the spark job definition.

        :param spark_job_definition_name: The spark job definition name.
        :type spark_job_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either SparkBatchJob or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.SparkBatchJob]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkBatchJob"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._execute_spark_job_definition_initial(
                spark_job_definition_name=spark_job_definition_name,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('SparkBatchJob', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_execute_spark_job_definition.metadata = {'url': '/sparkJobDefinitions/{sparkJobDefinitionName}/execute'}  # type: ignore

    def _debug_spark_job_definition_initial(
        self,
        properties,  # type: "models.SparkJobDefinition"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SparkBatchJob"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkBatchJob"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _spark_job_definition_azure_resource = models.SparkJobDefinitionResource(properties=properties)
        api_version = "2019-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._debug_spark_job_definition_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_spark_job_definition_azure_resource, 'SparkJobDefinitionResource')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('SparkBatchJob', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('SparkBatchJob', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _debug_spark_job_definition_initial.metadata = {'url': '/debugSparkJobDefinition'}  # type: ignore

    def begin_debug_spark_job_definition(
        self,
        properties,  # type: "models.SparkJobDefinition"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.SparkBatchJob"]
        """Debug the spark job definition.

        :param properties: Properties of spark job definition.
        :type properties: ~azure.synapse.artifacts.models.SparkJobDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either SparkBatchJob or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.SparkBatchJob]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkBatchJob"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._debug_spark_job_definition_initial(
                properties=properties,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('SparkBatchJob', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_debug_spark_job_definition.metadata = {'url': '/debugSparkJobDefinition'}  # type: ignore
