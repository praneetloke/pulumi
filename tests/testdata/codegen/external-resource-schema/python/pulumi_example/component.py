# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
import pulumi_aws
import pulumi_kubernetes

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 required_metadata: pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs'],
                 required_metadata_array: pulumi.Input[Sequence[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]],
                 required_metadata_map: pulumi.Input[Mapping[str, pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]],
                 metadata: Optional[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']] = None,
                 metadata_array: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]] = None,
                 metadata_map: Optional[pulumi.Input[Mapping[str, pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]] = None):
        """
        The set of arguments for constructing a Component resource.
        """
        pulumi.set(__self__, "required_metadata", required_metadata)
        pulumi.set(__self__, "required_metadata_array", required_metadata_array)
        pulumi.set(__self__, "required_metadata_map", required_metadata_map)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if metadata_array is not None:
            pulumi.set(__self__, "metadata_array", metadata_array)
        if metadata_map is not None:
            pulumi.set(__self__, "metadata_map", metadata_map)

    @property
    @pulumi.getter(name="requiredMetadata")
    def required_metadata(self) -> pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']:
        return pulumi.get(self, "required_metadata")

    @required_metadata.setter
    def required_metadata(self, value: pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']):
        pulumi.set(self, "required_metadata", value)

    @property
    @pulumi.getter(name="requiredMetadataArray")
    def required_metadata_array(self) -> pulumi.Input[Sequence[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]:
        return pulumi.get(self, "required_metadata_array")

    @required_metadata_array.setter
    def required_metadata_array(self, value: pulumi.Input[Sequence[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]):
        pulumi.set(self, "required_metadata_array", value)

    @property
    @pulumi.getter(name="requiredMetadataMap")
    def required_metadata_map(self) -> pulumi.Input[Mapping[str, pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]:
        return pulumi.get(self, "required_metadata_map")

    @required_metadata_map.setter
    def required_metadata_map(self, value: pulumi.Input[Mapping[str, pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]):
        pulumi.set(self, "required_metadata_map", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]:
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="metadataArray")
    def metadata_array(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]:
        return pulumi.get(self, "metadata_array")

    @metadata_array.setter
    def metadata_array(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]):
        pulumi.set(self, "metadata_array", value)

    @property
    @pulumi.getter(name="metadataMap")
    def metadata_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]:
        return pulumi.get(self, "metadata_map")

    @metadata_map.setter
    def metadata_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]):
        pulumi.set(self, "metadata_map", value)


class Component(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]] = None,
                 metadata_array: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 metadata_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 required_metadata: Optional[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]] = None,
                 required_metadata_array: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 required_metadata_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 __props__=None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Component resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]] = None,
                 metadata_array: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 metadata_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 required_metadata: Optional[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]] = None,
                 required_metadata_array: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 required_metadata_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['pulumi_kubernetes.meta.v1.ObjectMetaArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["metadata_array"] = metadata_array
            __props__.__dict__["metadata_map"] = metadata_map
            if required_metadata is None and not opts.urn:
                raise TypeError("Missing required property 'required_metadata'")
            __props__.__dict__["required_metadata"] = required_metadata
            if required_metadata_array is None and not opts.urn:
                raise TypeError("Missing required property 'required_metadata_array'")
            __props__.__dict__["required_metadata_array"] = required_metadata_array
            if required_metadata_map is None and not opts.urn:
                raise TypeError("Missing required property 'required_metadata_map'")
            __props__.__dict__["required_metadata_map"] = required_metadata_map
            __props__.__dict__["provider"] = None
            __props__.__dict__["security_group"] = None
            __props__.__dict__["storage_classes"] = None
        super(Component, __self__).__init__(
            'example::Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentArgs.__new__(ComponentArgs)

        __props__.__dict__["provider"] = None
        __props__.__dict__["security_group"] = None
        __props__.__dict__["storage_classes"] = None
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def provider(self) -> pulumi.Output[Optional['pulumi_kubernetes.Provider']]:
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> pulumi.Output['pulumi_aws.ec2.SecurityGroup']:
        return pulumi.get(self, "security_group")

    @property
    @pulumi.getter(name="storageClasses")
    def storage_classes(self) -> pulumi.Output[Optional[Mapping[str, 'pulumi_kubernetes.storage.v1.StorageClass']]]:
        return pulumi.get(self, "storage_classes")

