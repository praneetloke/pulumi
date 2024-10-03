// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package example

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"plain-object-defaults/example/internal"
)

// Check codegen of functions with all optional inputs.
func FuncWithAllOptionalInputs(ctx *pulumi.Context, args *FuncWithAllOptionalInputsArgs, opts ...pulumi.InvokeOption) (*FuncWithAllOptionalInputsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv FuncWithAllOptionalInputsResult
	err := ctx.Invoke("example::funcWithAllOptionalInputs", args.Defaults(), &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type FuncWithAllOptionalInputsArgs struct {
	// Property A
	A *HelmReleaseSettings `pulumi:"a"`
	// Property B
	B *string `pulumi:"b"`
}

// Defaults sets the appropriate defaults for FuncWithAllOptionalInputsArgs
func (val *FuncWithAllOptionalInputsArgs) Defaults() *FuncWithAllOptionalInputsArgs {
	if val == nil {
		return nil
	}
	tmp := *val
	tmp.A = tmp.A.Defaults()

	if tmp.B == nil {
		b_ := "defValue"
		tmp.B = &b_
	}
	return &tmp
}

type FuncWithAllOptionalInputsResult struct {
	R string `pulumi:"r"`
}

func FuncWithAllOptionalInputsOutput(ctx *pulumi.Context, args FuncWithAllOptionalInputsOutputArgs, opts ...pulumi.InvokeOption) FuncWithAllOptionalInputsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (FuncWithAllOptionalInputsResultOutput, error) {
			args := v.(FuncWithAllOptionalInputsArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv FuncWithAllOptionalInputsResult
			secret, err := ctx.InvokePackageRaw("example::funcWithAllOptionalInputs", args.Defaults(), &rv, "", opts...)
			if err != nil {
				return FuncWithAllOptionalInputsResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(FuncWithAllOptionalInputsResultOutput)
			if secret {
				return pulumi.ToSecret(output).(FuncWithAllOptionalInputsResultOutput), nil
			}
			return output, nil
		}).(FuncWithAllOptionalInputsResultOutput)
}

type FuncWithAllOptionalInputsOutputArgs struct {
	// Property A
	A HelmReleaseSettingsPtrInput `pulumi:"a"`
	// Property B
	B pulumi.StringPtrInput `pulumi:"b"`
}

func (FuncWithAllOptionalInputsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FuncWithAllOptionalInputsArgs)(nil)).Elem()
}

type FuncWithAllOptionalInputsResultOutput struct{ *pulumi.OutputState }

func (FuncWithAllOptionalInputsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FuncWithAllOptionalInputsResult)(nil)).Elem()
}

func (o FuncWithAllOptionalInputsResultOutput) ToFuncWithAllOptionalInputsResultOutput() FuncWithAllOptionalInputsResultOutput {
	return o
}

func (o FuncWithAllOptionalInputsResultOutput) ToFuncWithAllOptionalInputsResultOutputWithContext(ctx context.Context) FuncWithAllOptionalInputsResultOutput {
	return o
}

func (o FuncWithAllOptionalInputsResultOutput) R() pulumi.StringOutput {
	return o.ApplyT(func(v FuncWithAllOptionalInputsResult) string { return v.R }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(FuncWithAllOptionalInputsResultOutput{})
}