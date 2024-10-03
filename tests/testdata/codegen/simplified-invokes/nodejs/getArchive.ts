// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getArchive(a?: number, opts?: pulumi.InvokeOptions): Promise<pulumi.asset.Archive> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeSingle("std:index:GetArchive", {
        "a": a,
    }, opts);
}
export function getArchiveOutput(a?: pulumi.Input<number | undefined>, opts?: pulumi.InvokeOptions): pulumi.Output<pulumi.asset.Archive> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeSingleOutput("std:index:GetArchive", {
        "a": a,
    }, opts);
}