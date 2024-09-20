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
from .resource import Resource

__all__ = [
    'ArgFunctionResult',
    'AwaitableArgFunctionResult',
    'arg_function',
    'arg_function_output',
]

@pulumi.output_type
class ArgFunctionResult:
    def __init__(__self__, result=None):
        if result and not isinstance(result, Resource):
            raise TypeError("Expected argument 'result' to be a Resource")
        pulumi.set(__self__, "result", result)

    @property
    @pulumi.getter
    def result(self) -> Optional['Resource']:
        return pulumi.get(self, "result")


class AwaitableArgFunctionResult(ArgFunctionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ArgFunctionResult(
            result=self.result)


def arg_function(arg1: Optional['Resource'] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableArgFunctionResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['arg1'] = arg1
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('example::argFunction', __args__, opts=opts, typ=ArgFunctionResult).value

    return AwaitableArgFunctionResult(
        result=pulumi.get(__ret__, 'result'))


@_utilities.lift_output_func(arg_function)
def arg_function_output(arg1: Optional[pulumi.Input[Optional['Resource']]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ArgFunctionResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
