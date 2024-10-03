// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mypkg

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"output-funcs/mypkg/internal"
)

// Response for all the Bastion Shareable Link endpoints.
// API Version: 2020-11-01.
func GetBastionShareableLink(ctx *pulumi.Context, args *GetBastionShareableLinkArgs, opts ...pulumi.InvokeOption) (*GetBastionShareableLinkResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetBastionShareableLinkResult
	err := ctx.Invoke("mypkg::getBastionShareableLink", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetBastionShareableLinkArgs struct {
	// The name of the Bastion Host.
	BastionHostName string `pulumi:"bastionHostName"`
	// The name of the resource group.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// List of VM references.
	Vms []BastionShareableLink `pulumi:"vms"`
}

// Response for all the Bastion Shareable Link endpoints.
type GetBastionShareableLinkResult struct {
	// The URL to get the next set of results.
	NextLink *string `pulumi:"nextLink"`
}

func GetBastionShareableLinkOutput(ctx *pulumi.Context, args GetBastionShareableLinkOutputArgs, opts ...pulumi.InvokeOption) GetBastionShareableLinkResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetBastionShareableLinkResultOutput, error) {
			args := v.(GetBastionShareableLinkArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetBastionShareableLinkResult
			secret, err := ctx.InvokePackageRaw("mypkg::getBastionShareableLink", args, &rv, "", opts...)
			if err != nil {
				return GetBastionShareableLinkResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetBastionShareableLinkResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetBastionShareableLinkResultOutput), nil
			}
			return output, nil
		}).(GetBastionShareableLinkResultOutput)
}

type GetBastionShareableLinkOutputArgs struct {
	// The name of the Bastion Host.
	BastionHostName pulumi.StringInput `pulumi:"bastionHostName"`
	// The name of the resource group.
	ResourceGroupName pulumi.StringInput `pulumi:"resourceGroupName"`
	// List of VM references.
	Vms BastionShareableLinkArrayInput `pulumi:"vms"`
}

func (GetBastionShareableLinkOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetBastionShareableLinkArgs)(nil)).Elem()
}

// Response for all the Bastion Shareable Link endpoints.
type GetBastionShareableLinkResultOutput struct{ *pulumi.OutputState }

func (GetBastionShareableLinkResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetBastionShareableLinkResult)(nil)).Elem()
}

func (o GetBastionShareableLinkResultOutput) ToGetBastionShareableLinkResultOutput() GetBastionShareableLinkResultOutput {
	return o
}

func (o GetBastionShareableLinkResultOutput) ToGetBastionShareableLinkResultOutputWithContext(ctx context.Context) GetBastionShareableLinkResultOutput {
	return o
}

func (o GetBastionShareableLinkResultOutput) ToOutput(ctx context.Context) pulumix.Output[GetBastionShareableLinkResult] {
	return pulumix.Output[GetBastionShareableLinkResult]{
		OutputState: o.OutputState,
	}
}

// The URL to get the next set of results.
func (o GetBastionShareableLinkResultOutput) NextLink() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetBastionShareableLinkResult) *string { return v.NextLink }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetBastionShareableLinkResultOutput{})
}
