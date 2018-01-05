# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.dps_certificate_operations import DpsCertificateOperations
from .operations.iot_dps_resource_operations import IotDpsResourceOperations
from .operations.dps_certificates_operations import DpsCertificatesOperations
from . import models


class IotDpsClientConfiguration(AzureConfiguration):
    """Configuration for IotDpsClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(IotDpsClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-iothubprovisioningservices/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class IotDpsClient(object):
    """API for using the Azure IoT Hub Device Provisioning Service features.

    :ivar config: Configuration for client.
    :vartype config: IotDpsClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.iothubprovisioningservices.operations.Operations
    :ivar dps_certificate: DpsCertificate operations
    :vartype dps_certificate: azure.mgmt.iothubprovisioningservices.operations.DpsCertificateOperations
    :ivar iot_dps_resource: IotDpsResource operations
    :vartype iot_dps_resource: azure.mgmt.iothubprovisioningservices.operations.IotDpsResourceOperations
    :ivar dps_certificates: DpsCertificates operations
    :vartype dps_certificates: azure.mgmt.iothubprovisioningservices.operations.DpsCertificatesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = IotDpsClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-11-15'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dps_certificate = DpsCertificateOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.iot_dps_resource = IotDpsResourceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dps_certificates = DpsCertificatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
