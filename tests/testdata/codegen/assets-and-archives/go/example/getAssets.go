// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package example

import (
	"context"
	"reflect"

	"assets-and-archives/example/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetAssets(ctx *pulumi.Context, args *GetAssetsArgs, opts ...pulumi.InvokeOption) (*GetAssetsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetAssetsResult
	err := ctx.Invoke("example::GetAssets", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetAssetsArgs struct {
	Archive pulumi.Archive        `pulumi:"archive"`
	Source  pulumi.AssetOrArchive `pulumi:"source"`
}

type GetAssetsResult struct {
	Archive pulumi.Archive        `pulumi:"archive"`
	Source  pulumi.AssetOrArchive `pulumi:"source"`
}

func GetAssetsOutput(ctx *pulumi.Context, args GetAssetsOutputArgs, opts ...pulumi.InvokeOption) GetAssetsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAssetsResultOutput, error) {
			args := v.(GetAssetsArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetAssetsResult
			secret, err := ctx.InvokePackageRaw("example::GetAssets", args, &rv, "", opts...)
			if err != nil {
				return GetAssetsResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetAssetsResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetAssetsResultOutput), nil
			}
			return output, nil
		}).(GetAssetsResultOutput)
}

type GetAssetsOutputArgs struct {
	Archive pulumi.ArchiveInput        `pulumi:"archive"`
	Source  pulumi.AssetOrArchiveInput `pulumi:"source"`
}

func (GetAssetsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAssetsArgs)(nil)).Elem()
}

type GetAssetsResultOutput struct{ *pulumi.OutputState }

func (GetAssetsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAssetsResult)(nil)).Elem()
}

func (o GetAssetsResultOutput) ToGetAssetsResultOutput() GetAssetsResultOutput {
	return o
}

func (o GetAssetsResultOutput) ToGetAssetsResultOutputWithContext(ctx context.Context) GetAssetsResultOutput {
	return o
}

func (o GetAssetsResultOutput) Archive() pulumi.ArchiveOutput {
	return o.ApplyT(func(v GetAssetsResult) pulumi.Archive { return v.Archive }).(pulumi.ArchiveOutput)
}

func (o GetAssetsResultOutput) Source() pulumi.AssetOrArchiveOutput {
	return o.ApplyT(func(v GetAssetsResult) pulumi.AssetOrArchive { return v.Source }).(pulumi.AssetOrArchiveOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAssetsResultOutput{})
}
