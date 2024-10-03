// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package simpleinvoke

import (
	"context"
	"reflect"

	"example.com/pulumi-simple-invoke/sdk/go/v10/simpleinvoke/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func MyInvoke(ctx *pulumi.Context, args *MyInvokeArgs, opts ...pulumi.InvokeOption) (*MyInvokeResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv MyInvokeResult
	err := ctx.Invoke("simple-invoke:index:myInvoke", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type MyInvokeArgs struct {
	Value string `pulumi:"value"`
}

type MyInvokeResult struct {
	Result string `pulumi:"result"`
}

func MyInvokeOutput(ctx *pulumi.Context, args MyInvokeOutputArgs, opts ...pulumi.InvokeOption) MyInvokeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (MyInvokeResultOutput, error) {
			args := v.(MyInvokeArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv MyInvokeResult
			secret, err := ctx.InvokePackageRaw("simple-invoke:index:myInvoke", args, &rv, "", opts...)
			if err != nil {
				return MyInvokeResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(MyInvokeResultOutput)
			if secret {
				return pulumi.ToSecret(output).(MyInvokeResultOutput), nil
			}
			return output, nil
		}).(MyInvokeResultOutput)
}

type MyInvokeOutputArgs struct {
	Value pulumi.StringInput `pulumi:"value"`
}

func (MyInvokeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*MyInvokeArgs)(nil)).Elem()
}

type MyInvokeResultOutput struct{ *pulumi.OutputState }

func (MyInvokeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MyInvokeResult)(nil)).Elem()
}

func (o MyInvokeResultOutput) ToMyInvokeResultOutput() MyInvokeResultOutput {
	return o
}

func (o MyInvokeResultOutput) ToMyInvokeResultOutputWithContext(ctx context.Context) MyInvokeResultOutput {
	return o
}

func (o MyInvokeResultOutput) Result() pulumi.StringOutput {
	return o.ApplyT(func(v MyInvokeResult) string { return v.Result }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(MyInvokeResultOutput{})
}
