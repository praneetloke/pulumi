// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package simpleinvoke

import (
	"context"
	"reflect"

	"example.com/pulumi-simple-invoke/sdk/go/v10/simpleinvoke/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type StringResource struct {
	pulumi.CustomResourceState

	Text pulumi.StringOutput `pulumi:"text"`
}

// NewStringResource registers a new resource with the given unique name, arguments, and options.
func NewStringResource(ctx *pulumi.Context,
	name string, args *StringResourceArgs, opts ...pulumi.ResourceOption) (*StringResource, error) {
	if args == nil {
		args = &StringResourceArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource StringResource
	err := ctx.RegisterResource("simple-invoke:index:StringResource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStringResource gets an existing StringResource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStringResource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StringResourceState, opts ...pulumi.ResourceOption) (*StringResource, error) {
	var resource StringResource
	err := ctx.ReadResource("simple-invoke:index:StringResource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StringResource resources.
type stringResourceState struct {
}

type StringResourceState struct {
}

func (StringResourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*stringResourceState)(nil)).Elem()
}

type stringResourceArgs struct {
}

// The set of arguments for constructing a StringResource resource.
type StringResourceArgs struct {
}

func (StringResourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stringResourceArgs)(nil)).Elem()
}

type StringResourceInput interface {
	pulumi.Input

	ToStringResourceOutput() StringResourceOutput
	ToStringResourceOutputWithContext(ctx context.Context) StringResourceOutput
}

func (*StringResource) ElementType() reflect.Type {
	return reflect.TypeOf((**StringResource)(nil)).Elem()
}

func (i *StringResource) ToStringResourceOutput() StringResourceOutput {
	return i.ToStringResourceOutputWithContext(context.Background())
}

func (i *StringResource) ToStringResourceOutputWithContext(ctx context.Context) StringResourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StringResourceOutput)
}

type StringResourceOutput struct{ *pulumi.OutputState }

func (StringResourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StringResource)(nil)).Elem()
}

func (o StringResourceOutput) ToStringResourceOutput() StringResourceOutput {
	return o
}

func (o StringResourceOutput) ToStringResourceOutputWithContext(ctx context.Context) StringResourceOutput {
	return o
}

func (o StringResourceOutput) Text() pulumi.StringOutput {
	return o.ApplyT(func(v *StringResource) pulumi.StringOutput { return v.Text }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StringResourceInput)(nil)).Elem(), &StringResource{})
	pulumi.RegisterOutputType(StringResourceOutput{})
}
