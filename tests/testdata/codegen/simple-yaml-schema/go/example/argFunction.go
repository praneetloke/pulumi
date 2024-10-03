// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package example

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"simple-yaml-schema/example/internal"
)

func ArgFunction(ctx *pulumi.Context, args *ArgFunctionArgs, opts ...pulumi.InvokeOption) (*ArgFunctionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv ArgFunctionResult
	err := ctx.Invoke("example::argFunction", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type ArgFunctionArgs struct {
	Arg1 *Resource `pulumi:"arg1"`
}

type ArgFunctionResult struct {
	Result *Resource `pulumi:"result"`
}

func ArgFunctionOutput(ctx *pulumi.Context, args ArgFunctionOutputArgs, opts ...pulumi.InvokeOption) ArgFunctionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ArgFunctionResultOutput, error) {
			args := v.(ArgFunctionArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv ArgFunctionResult
			secret, err := ctx.InvokePackageRaw("example::argFunction", args, &rv, "", opts...)
			if err != nil {
				return ArgFunctionResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(ArgFunctionResultOutput)
			if secret {
				return pulumi.ToSecret(output).(ArgFunctionResultOutput), nil
			}
			return output, nil
		}).(ArgFunctionResultOutput)
}

type ArgFunctionOutputArgs struct {
	Arg1 ResourceInput `pulumi:"arg1"`
}

func (ArgFunctionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ArgFunctionArgs)(nil)).Elem()
}

type ArgFunctionResultOutput struct{ *pulumi.OutputState }

func (ArgFunctionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ArgFunctionResult)(nil)).Elem()
}

func (o ArgFunctionResultOutput) ToArgFunctionResultOutput() ArgFunctionResultOutput {
	return o
}

func (o ArgFunctionResultOutput) ToArgFunctionResultOutputWithContext(ctx context.Context) ArgFunctionResultOutput {
	return o
}

func (o ArgFunctionResultOutput) Result() ResourceOutput {
	return o.ApplyT(func(v ArgFunctionResult) *Resource { return v.Result }).(ResourceOutput)
}

func init() {
	pulumi.RegisterOutputType(ArgFunctionResultOutput{})
}