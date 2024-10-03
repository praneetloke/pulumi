# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload, Awaitable
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from ._inputs import *

__all__ = [
    'do_foo',
]

def do_foo(foo: Optional[Union['Foo', 'FooDict']] = None,
           opts: Optional[pulumi.InvokeOptions] = None) -> Awaitable[None]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['foo'] = foo
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('example::doFoo', __args__, opts=opts).value
