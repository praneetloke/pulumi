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
    'ConfigMapArgs',
    'ConfigMapArgsDict',
    'ObjectWithNodeOptionalInputsArgs',
    'ObjectWithNodeOptionalInputsArgsDict',
    'ObjectArgs',
    'ObjectArgsDict',
    'SomeOtherObjectArgs',
    'SomeOtherObjectArgsDict',
]

MYPY = False

if not MYPY:
    class ConfigMapArgsDict(TypedDict):
        config: NotRequired[pulumi.Input[str]]
elif False:
    ConfigMapArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConfigMapArgs:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input[str]] = None):
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)


if not MYPY:
    class ObjectWithNodeOptionalInputsArgsDict(TypedDict):
        foo: pulumi.Input[str]
        bar: NotRequired[pulumi.Input[int]]
elif False:
    ObjectWithNodeOptionalInputsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ObjectWithNodeOptionalInputsArgs:
    def __init__(__self__, *,
                 foo: pulumi.Input[str],
                 bar: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "foo", foo)
        if bar is not None:
            pulumi.set(__self__, "bar", bar)

    @property
    @pulumi.getter
    def foo(self) -> pulumi.Input[str]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: pulumi.Input[str]):
        pulumi.set(self, "foo", value)

    @property
    @pulumi.getter
    def bar(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "bar")

    @bar.setter
    def bar(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bar", value)


if not MYPY:
    class ObjectArgsDict(TypedDict):
        bar: NotRequired[pulumi.Input[str]]
        configs: NotRequired[pulumi.Input[Sequence[pulumi.Input['ConfigMapArgsDict']]]]
        foo: NotRequired[pulumi.Input['Resource']]
        others: NotRequired[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgsDict']]]]]]
        """
        List of lists of other objects
        """
        still_others: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgsDict']]]]]]
        """
        Mapping from string to list of some other object
        """
elif False:
    ObjectArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ObjectArgs:
    def __init__(__self__, *,
                 bar: Optional[pulumi.Input[str]] = None,
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigMapArgs']]]] = None,
                 foo: Optional[pulumi.Input['Resource']] = None,
                 others: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]]] = None,
                 still_others: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]] others: List of lists of other objects
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]] still_others: Mapping from string to list of some other object
        """
        if bar is not None:
            pulumi.set(__self__, "bar", bar)
        if configs is not None:
            pulumi.set(__self__, "configs", configs)
        if foo is not None:
            pulumi.set(__self__, "foo", foo)
        if others is not None:
            pulumi.set(__self__, "others", others)
        if still_others is not None:
            pulumi.set(__self__, "still_others", still_others)

    @property
    @pulumi.getter
    def bar(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bar")

    @bar.setter
    def bar(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bar", value)

    @property
    @pulumi.getter
    def configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigMapArgs']]]]:
        return pulumi.get(self, "configs")

    @configs.setter
    def configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigMapArgs']]]]):
        pulumi.set(self, "configs", value)

    @property
    @pulumi.getter
    def foo(self) -> Optional[pulumi.Input['Resource']]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: Optional[pulumi.Input['Resource']]):
        pulumi.set(self, "foo", value)

    @property
    @pulumi.getter
    def others(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]]]:
        """
        List of lists of other objects
        """
        return pulumi.get(self, "others")

    @others.setter
    def others(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]]]):
        pulumi.set(self, "others", value)

    @property
    @pulumi.getter(name="stillOthers")
    def still_others(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]]]:
        """
        Mapping from string to list of some other object
        """
        return pulumi.get(self, "still_others")

    @still_others.setter
    def still_others(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['SomeOtherObjectArgs']]]]]]):
        pulumi.set(self, "still_others", value)


if not MYPY:
    class SomeOtherObjectArgsDict(TypedDict):
        baz: NotRequired[pulumi.Input[str]]
elif False:
    SomeOtherObjectArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SomeOtherObjectArgs:
    def __init__(__self__, *,
                 baz: Optional[pulumi.Input[str]] = None):
        if baz is not None:
            pulumi.set(__self__, "baz", baz)

    @property
    @pulumi.getter
    def baz(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "baz")

    @baz.setter
    def baz(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "baz", value)

