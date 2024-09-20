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

__all__ = [
    'GetAssetsResult',
    'AwaitableGetAssetsResult',
    'get_assets',
    'get_assets_output',
]

@pulumi.output_type
class GetAssetsResult:
    def __init__(__self__, archive=None, source=None):
        if archive and not isinstance(archive, pulumi.Archive):
            raise TypeError("Expected argument 'archive' to be a pulumi.Archive")
        pulumi.set(__self__, "archive", archive)
        if source and not isinstance(source, Union[pulumi.Asset, pulumi.Archive]):
            raise TypeError("Expected argument 'source' to be a Union[pulumi.Asset, pulumi.Archive]")
        pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def archive(self) -> pulumi.Archive:
        return pulumi.get(self, "archive")

    @property
    @pulumi.getter
    def source(self) -> Union[pulumi.Asset, pulumi.Archive]:
        return pulumi.get(self, "source")


class AwaitableGetAssetsResult(GetAssetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssetsResult(
            archive=self.archive,
            source=self.source)


def get_assets(archive: Optional[pulumi.Archive] = None,
               source: Optional[Union[pulumi.Asset, pulumi.Archive]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssetsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['archive'] = archive
    __args__['source'] = source
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('example::GetAssets', __args__, opts=opts, typ=GetAssetsResult).value

    return AwaitableGetAssetsResult(
        archive=pulumi.get(__ret__, 'archive'),
        source=pulumi.get(__ret__, 'source'))


@_utilities.lift_output_func(get_assets)
def get_assets_output(archive: Optional[pulumi.Input[pulumi.Archive]] = None,
                      source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssetsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
