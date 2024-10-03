// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Returns the absolute value of a given float.
 * Example: abs(1) returns 1, and abs(-1) would also return 1, whereas abs(-3.14) would return 3.14.
 */
export function absMultiArgsReducedOutput(a: number, b?: number, opts?: pulumi.InvokeOptions): Promise<number> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeSingle("std:index:AbsMultiArgsReducedOutput", {
        "a": a,
        "b": b,
    }, opts);
}
/**
 * Returns the absolute value of a given float.
 * Example: abs(1) returns 1, and abs(-1) would also return 1, whereas abs(-3.14) would return 3.14.
 */
export function absMultiArgsReducedOutputOutput(a: pulumi.Input<number>, b?: pulumi.Input<number | undefined>, opts?: pulumi.InvokeOptions): pulumi.Output<number> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeSingleOutput("std:index:AbsMultiArgsReducedOutput", {
        "a": a,
        "b": b,
    }, opts);
}