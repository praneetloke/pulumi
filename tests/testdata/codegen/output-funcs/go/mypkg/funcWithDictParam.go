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

// Check codegen of functions with a Dict<str,str> parameter.
func FuncWithDictParam(ctx *pulumi.Context, args *FuncWithDictParamArgs, opts ...pulumi.InvokeOption) (*FuncWithDictParamResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv FuncWithDictParamResult
	err := ctx.Invoke("mypkg::funcWithDictParam", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type FuncWithDictParamArgs struct {
	A map[string]string `pulumi:"a"`
	B *string           `pulumi:"b"`
}

type FuncWithDictParamResult struct {
	R string `pulumi:"r"`
}

func FuncWithDictParamOutput(ctx *pulumi.Context, args FuncWithDictParamOutputArgs, opts ...pulumi.InvokeOption) FuncWithDictParamResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (FuncWithDictParamResultOutput, error) {
			args := v.(FuncWithDictParamArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv FuncWithDictParamResult
			secret, err := ctx.InvokePackageRaw("mypkg::funcWithDictParam", args, &rv, "", opts...)
			if err != nil {
				return FuncWithDictParamResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(FuncWithDictParamResultOutput)
			if secret {
				return pulumi.ToSecret(output).(FuncWithDictParamResultOutput), nil
			}
			return output, nil
		}).(FuncWithDictParamResultOutput)
}

type FuncWithDictParamOutputArgs struct {
	A pulumi.StringMapInput `pulumi:"a"`
	B pulumi.StringPtrInput `pulumi:"b"`
}

func (FuncWithDictParamOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FuncWithDictParamArgs)(nil)).Elem()
}

type FuncWithDictParamResultOutput struct{ *pulumi.OutputState }

func (FuncWithDictParamResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FuncWithDictParamResult)(nil)).Elem()
}

func (o FuncWithDictParamResultOutput) ToFuncWithDictParamResultOutput() FuncWithDictParamResultOutput {
	return o
}

func (o FuncWithDictParamResultOutput) ToFuncWithDictParamResultOutputWithContext(ctx context.Context) FuncWithDictParamResultOutput {
	return o
}

func (o FuncWithDictParamResultOutput) ToOutput(ctx context.Context) pulumix.Output[FuncWithDictParamResult] {
	return pulumix.Output[FuncWithDictParamResult]{
		OutputState: o.OutputState,
	}
}

func (o FuncWithDictParamResultOutput) R() pulumi.StringOutput {
	return o.ApplyT(func(v FuncWithDictParamResult) string { return v.R }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(FuncWithDictParamResultOutput{})
}
