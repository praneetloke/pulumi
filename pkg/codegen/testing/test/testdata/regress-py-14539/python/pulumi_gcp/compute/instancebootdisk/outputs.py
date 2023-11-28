# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ... import compute as _compute

__all__ = [
    'InstanceBootDisk',
]

@pulumi.output_type
class InstanceBootDisk(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "initializeParams":
            suggest = "initialize_params"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceBootDisk. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceBootDisk.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceBootDisk.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 initialize_params: '_compute.instancebootdiskinitializeparams.outputs.InstanceBootDiskInitializeParams'):
        """
        :param '_compute.instancebootdiskinitializeparams.InstanceBootDiskInitializeParamsArgs' initialize_params: Parameters for a new disk that will be created
               alongside the new instance. Either `initialize_params` or `source` must be set.
               Structure is documented below.
        """
        pulumi.set(__self__, "initialize_params", initialize_params)

    @property
    @pulumi.getter(name="initializeParams")
    def initialize_params(self) -> '_compute.instancebootdiskinitializeparams.outputs.InstanceBootDiskInitializeParams':
        """
        Parameters for a new disk that will be created
        alongside the new instance. Either `initialize_params` or `source` must be set.
        Structure is documented below.
        """
        return pulumi.get(self, "initialize_params")


