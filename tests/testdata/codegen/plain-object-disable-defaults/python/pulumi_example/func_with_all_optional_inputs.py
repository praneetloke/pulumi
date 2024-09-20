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
from ._inputs import *

__all__ = [
    'FuncWithAllOptionalInputsResult',
    'AwaitableFuncWithAllOptionalInputsResult',
    'func_with_all_optional_inputs',
    'func_with_all_optional_inputs_output',
]

@pulumi.output_type
class FuncWithAllOptionalInputsResult:
    def __init__(__self__, r=None):
        if r and not isinstance(r, str):
            raise TypeError("Expected argument 'r' to be a str")
        pulumi.set(__self__, "r", r)

    @property
    @pulumi.getter
    def r(self) -> str:
        return pulumi.get(self, "r")


class AwaitableFuncWithAllOptionalInputsResult(FuncWithAllOptionalInputsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return FuncWithAllOptionalInputsResult(
            r=self.r)


def func_with_all_optional_inputs(a: Optional[Union['HelmReleaseSettings', 'HelmReleaseSettingsDict']] = None,
                                  b: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableFuncWithAllOptionalInputsResult:
    """
    Check codegen of functions with all optional inputs.


    :param Union['HelmReleaseSettings', 'HelmReleaseSettingsDict'] a: Property A
    :param str b: Property B
    """
    __args__ = dict()
    __args__['a'] = a
    __args__['b'] = b
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mypkg::funcWithAllOptionalInputs', __args__, opts=opts, typ=FuncWithAllOptionalInputsResult).value

    return AwaitableFuncWithAllOptionalInputsResult(
        r=pulumi.get(__ret__, 'r'))


@_utilities.lift_output_func(func_with_all_optional_inputs)
def func_with_all_optional_inputs_output(a: Optional[pulumi.Input[Optional[Union['HelmReleaseSettings', 'HelmReleaseSettingsDict']]]] = None,
                                         b: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[FuncWithAllOptionalInputsResult]:
    """
    Check codegen of functions with all optional inputs.


    :param Union['HelmReleaseSettings', 'HelmReleaseSettingsDict'] a: Property A
    :param str b: Property B
    """
    ...
