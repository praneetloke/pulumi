"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016-2022, Pulumi Corporation.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing
import pulumi.callback_pb2
import pulumi.provider_pb2
import pulumi.resource_pb2

class ResourceMonitorStub:
    """ResourceMonitor is the interface a source uses to talk back to the planning monitor orchestrating the execution."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    SupportsFeature: grpc.UnaryUnaryMultiCallable[
        pulumi.resource_pb2.SupportsFeatureRequest,
        pulumi.resource_pb2.SupportsFeatureResponse,
    ]
    Invoke: grpc.UnaryUnaryMultiCallable[
        pulumi.resource_pb2.ResourceInvokeRequest,
        pulumi.provider_pb2.InvokeResponse,
    ]
    StreamInvoke: grpc.UnaryStreamMultiCallable[
        pulumi.resource_pb2.ResourceInvokeRequest,
        pulumi.provider_pb2.InvokeResponse,
    ]
    Call: grpc.UnaryUnaryMultiCallable[
        pulumi.resource_pb2.ResourceCallRequest,
        pulumi.provider_pb2.CallResponse,
    ]
    ReadResource: grpc.UnaryUnaryMultiCallable[
        pulumi.resource_pb2.ReadResourceRequest,
        pulumi.resource_pb2.ReadResourceResponse,
    ]
    RegisterResource: grpc.UnaryUnaryMultiCallable[
        pulumi.resource_pb2.RegisterResourceRequest,
        pulumi.resource_pb2.RegisterResourceResponse,
    ]
    RegisterResourceOutputs: grpc.UnaryUnaryMultiCallable[
        pulumi.resource_pb2.RegisterResourceOutputsRequest,
        google.protobuf.empty_pb2.Empty,
    ]
    RegisterStackTransform: grpc.UnaryUnaryMultiCallable[
        pulumi.callback_pb2.Callback,
        google.protobuf.empty_pb2.Empty,
    ]
    """Register a resource transform for the stack"""
    RegisterStackInvokeTransform: grpc.UnaryUnaryMultiCallable[
        pulumi.callback_pb2.Callback,
        google.protobuf.empty_pb2.Empty,
    ]
    """Register an invoke transform for the stack"""
    RegisterPackage: grpc.UnaryUnaryMultiCallable[
        pulumi.resource_pb2.RegisterPackageRequest,
        pulumi.resource_pb2.RegisterPackageResponse,
    ]

class ResourceMonitorServicer(metaclass=abc.ABCMeta):
    """ResourceMonitor is the interface a source uses to talk back to the planning monitor orchestrating the execution."""

    
    def SupportsFeature(
        self,
        request: pulumi.resource_pb2.SupportsFeatureRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.resource_pb2.SupportsFeatureResponse: ...
    
    def Invoke(
        self,
        request: pulumi.resource_pb2.ResourceInvokeRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.provider_pb2.InvokeResponse: ...
    
    def StreamInvoke(
        self,
        request: pulumi.resource_pb2.ResourceInvokeRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[pulumi.provider_pb2.InvokeResponse]: ...
    
    def Call(
        self,
        request: pulumi.resource_pb2.ResourceCallRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.provider_pb2.CallResponse: ...
    
    def ReadResource(
        self,
        request: pulumi.resource_pb2.ReadResourceRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.resource_pb2.ReadResourceResponse: ...
    
    def RegisterResource(
        self,
        request: pulumi.resource_pb2.RegisterResourceRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.resource_pb2.RegisterResourceResponse: ...
    
    def RegisterResourceOutputs(
        self,
        request: pulumi.resource_pb2.RegisterResourceOutputsRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...
    
    def RegisterStackTransform(
        self,
        request: pulumi.callback_pb2.Callback,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty:
        """Register a resource transform for the stack"""
    
    def RegisterStackInvokeTransform(
        self,
        request: pulumi.callback_pb2.Callback,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty:
        """Register an invoke transform for the stack"""
    
    def RegisterPackage(
        self,
        request: pulumi.resource_pb2.RegisterPackageRequest,
        context: grpc.ServicerContext,
    ) -> pulumi.resource_pb2.RegisterPackageResponse: ...

def add_ResourceMonitorServicer_to_server(servicer: ResourceMonitorServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
