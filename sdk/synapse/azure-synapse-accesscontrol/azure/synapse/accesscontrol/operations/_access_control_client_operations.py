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

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AccessControlClientOperationsMixin(object):

    def get_role_definitions(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.RolesListResponse"]
        """List roles.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RolesListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.synapse.accesscontrol.models.RolesListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RolesListResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_role_definitions.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('RolesListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorContract, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_role_definitions.metadata = {'url': '/rbac/roles'}  # type: ignore

    def get_role_definition_by_id(
        self,
        role_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SynapseRole"
        """Get role by role Id.

        :param role_id: Synapse Built-In Role Id.
        :type role_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynapseRole, or the result of cls(response)
        :rtype: ~azure.synapse.accesscontrol.models.SynapseRole
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SynapseRole"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_role_definition_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'roleId': self._serialize.url("role_id", role_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorContract, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SynapseRole', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_role_definition_by_id.metadata = {'url': '/rbac/roles/{roleId}'}  # type: ignore

    def create_role_assignment(
        self,
        create_role_assignment_options,  # type: "models.RoleAssignmentOptions"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.RoleAssignmentDetails"
        """Create role assignment.

        :param create_role_assignment_options: Details of role id and object id.
        :type create_role_assignment_options: ~azure.synapse.accesscontrol.models.RoleAssignmentOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentDetails, or the result of cls(response)
        :rtype: ~azure.synapse.accesscontrol.models.RoleAssignmentDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RoleAssignmentDetails"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_role_assignment.metadata['url']  # type: ignore
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
        body_content = self._serialize.body(create_role_assignment_options, 'RoleAssignmentOptions')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorContract, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleAssignmentDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_role_assignment.metadata = {'url': '/rbac/roleAssignments'}  # type: ignore

    def get_role_assignments(
        self,
        role_id=None,  # type: Optional[str]
        principal_id=None,  # type: Optional[str]
        continuation_token_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.RoleAssignmentDetails"]
        """List role assignments.

        :param role_id: Synapse Built-In Role Id.
        :type role_id: str
        :param principal_id: Object ID of the AAD principal or security-group.
        :type principal_id: str
        :param continuation_token_parameter: Continuation token.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of RoleAssignmentDetails, or the result of cls(response)
        :rtype: list[~azure.synapse.accesscontrol.models.RoleAssignmentDetails]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.RoleAssignmentDetails"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_role_assignments.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if role_id is not None:
            query_parameters['roleId'] = self._serialize.query("role_id", role_id, 'str')
        if principal_id is not None:
            query_parameters['principalId'] = self._serialize.query("principal_id", principal_id, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if continuation_token_parameter is not None:
            header_parameters['x-ms-continuation'] = self._serialize.header("continuation_token_parameter", continuation_token_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorContract, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-continuation']=self._deserialize('str', response.headers.get('x-ms-continuation'))
        deserialized = self._deserialize('[RoleAssignmentDetails]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_role_assignments.metadata = {'url': '/rbac/roleAssignments'}  # type: ignore

    def get_role_assignment_by_id(
        self,
        role_assignment_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.RoleAssignmentDetails"
        """Get role assignment by role assignment Id.

        :param role_assignment_id: The ID of the role assignment.
        :type role_assignment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentDetails, or the result of cls(response)
        :rtype: ~azure.synapse.accesscontrol.models.RoleAssignmentDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RoleAssignmentDetails"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_role_assignment_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'roleAssignmentId': self._serialize.url("role_assignment_id", role_assignment_id, 'str', min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorContract, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleAssignmentDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_role_assignment_by_id.metadata = {'url': '/rbac/roleAssignments/{roleAssignmentId}'}  # type: ignore

    def delete_role_assignment_by_id(
        self,
        role_assignment_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete role assignment by role assignment Id.

        :param role_assignment_id: The ID of the role assignment.
        :type role_assignment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete_role_assignment_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'roleAssignmentId': self._serialize.url("role_assignment_id", role_assignment_id, 'str', min_length=1),
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
            error = self._deserialize(models.ErrorContract, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_role_assignment_by_id.metadata = {'url': '/rbac/roleAssignments/{roleAssignmentId}'}  # type: ignore

    def get_caller_role_assignments(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List[str]
        """List role assignments of the caller.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List[str]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_caller_role_assignments.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorContract, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_caller_role_assignments.metadata = {'url': '/rbac/getMyAssignedRoles'}  # type: ignore
