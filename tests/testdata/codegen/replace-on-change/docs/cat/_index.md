
---
title: "Cat"
title_tag: "example.Cat"
meta_desc: "Documentation for the example.Cat resource with examples, input properties, output properties, lookup functions, and supporting types."
layout: api
no_edit_this_page: true
---



<!-- WARNING: this file was generated by test. -->
<!-- Do not edit by hand unless you're certain you know what you are doing! -->




## Create Cat Resource {#create}

Resources are created with functions called constructors. To learn more about declaring and configuring resources, see [Resources](/docs/concepts/resources/).

### Constructor syntax
<div>
<pulumi-chooser type="language" options="csharp,go,typescript,python,yaml,java"></pulumi-chooser>
</div>


<div>
<pulumi-choosable type="language" values="javascript,typescript">
<div class="no-copy"><div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx">Cat</span><span class="p">(</span><span class="nx">name</span><span class="p">:</span> <span class="nx">string</span><span class="p">,</span> <span class="nx">args</span><span class="p">?:</span> <span class="nx"><a href="#inputs">CatArgs</a></span><span class="p">,</span> <span class="nx">opts</span><span class="p">?:</span> <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
</div></pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="python">
<div class="no-copy"><div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class=nd>@overload</span>
<span class="k">def </span><span class="nx">Cat</span><span class="p">(</span><span class="nx">resource_name</span><span class="p">:</span> <span class="nx">str</span><span class="p">,</span>
        <span class="nx">args</span><span class="p">:</span> <span class="nx"><a href="#inputs">Optional[CatArgs]</a></span> = None<span class="p">,</span>
        <span class="nx">opts</span><span class="p">:</span> <span class="nx"><a href="/docs/reference/pkg/python/pulumi/#pulumi.ResourceOptions">Optional[ResourceOptions]</a></span> = None<span class="p">)</span>
<span></span>
<span class=nd>@overload</span>
<span class="k">def </span><span class="nx">Cat</span><span class="p">(</span><span class="nx">resource_name</span><span class="p">:</span> <span class="nx">str</span><span class="p">,</span>
        <span class="nx">opts</span><span class="p">:</span> <span class="nx"><a href="/docs/reference/pkg/python/pulumi/#pulumi.ResourceOptions">Optional[ResourceOptions]</a></span> = None<span class="p">)</span></code></pre></div>
</div></pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="go">
<div class="no-copy"><div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span><span class="nx">NewCat</span><span class="p">(</span><span class="nx">ctx</span><span class="p"> *</span><span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">,</span> <span class="nx">name</span><span class="p"> </span><span class="nx">string</span><span class="p">,</span> <span class="nx">args</span><span class="p"> *</span><span class="nx"><a href="#inputs">CatArgs</a></span><span class="p">,</span> <span class="nx">opts</span><span class="p"> ...</span><span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx">Cat</span>, error)</span></code></pre></div>
</div></pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="csharp">
<div class="no-copy"><div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx">Cat</span><span class="p">(</span><span class="nx">string</span><span class="p"> </span><span class="nx">name<span class="p">,</span> <span class="nx"><a href="#inputs">CatArgs</a></span><span class="p">? </span><span class="nx">args = null<span class="p">,</span> <span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span><span class="p">? </span><span class="nx">opts = null<span class="p">)</span></code></pre></div>
</div></pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="java">
<div class="no-copy"><div class="highlight"><pre class="chroma">
<code class="language-java" data-lang="java"><span class="k">public </span><span class="nx">Cat</span><span class="p">(</span><span class="nx">String</span><span class="p"> </span><span class="nx">name<span class="p">,</span> <span class="nx"><a href="#inputs">CatArgs</a></span><span class="p"> </span><span class="nx">args<span class="p">)</span>
<span class="k">public </span><span class="nx">Cat</span><span class="p">(</span><span class="nx">String</span><span class="p"> </span><span class="nx">name<span class="p">,</span> <span class="nx"><a href="#inputs">CatArgs</a></span><span class="p"> </span><span class="nx">args<span class="p">,</span> <span class="nx">CustomResourceOptions</span><span class="p"> </span><span class="nx">options<span class="p">)</span>
</code></pre></div></div>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="yaml">
<div class="no-copy"><div class="highlight"><pre class="chroma"><code class="language-yaml" data-lang="yaml">type: <span class="nx">example:Cat</span><span class="p"></span>
<span class="p">properties</span><span class="p">: </span><span class="c">#&nbsp;The arguments to resource properties.</span>
<span class="p"></span><span class="p">options</span><span class="p">: </span><span class="c">#&nbsp;Bag of options to control resource&#39;s behavior.</span>
<span class="p"></span>
</code></pre></div></div>
</pulumi-choosable>
</div>

#### Parameters

<div>
<pulumi-choosable type="language" values="javascript,typescript">

<dl class="resources-properties"><dt
        class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>The unique name of the resource.</dd><dt
        class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#inputs">CatArgs</a></span>
    </dt>
    <dd>The arguments to resource properties.</dd><dt
        class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span>
    </dt>
    <dd>Bag of options to control resource&#39;s behavior.</dd></dl>

</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="python">

<dl class="resources-properties"><dt
        class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>The unique name of the resource.</dd><dt
        class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#inputs">CatArgs</a></span>
    </dt>
    <dd>The arguments to resource properties.</dd><dt
        class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="/docs/reference/pkg/python/pulumi/#pulumi.ResourceOptions">ResourceOptions</a></span>
    </dt>
    <dd>Bag of options to control resource&#39;s behavior.</dd></dl>

</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="go">

<dl class="resources-properties"><dt
        class="property-optional" title="Optional">
        <span>ctx</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span>
    </dt>
    <dd>Context object for the current deployment.</dd><dt
        class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>The unique name of the resource.</dd><dt
        class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#inputs">CatArgs</a></span>
    </dt>
    <dd>The arguments to resource properties.</dd><dt
        class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span>
    </dt>
    <dd>Bag of options to control resource&#39;s behavior.</dd></dl>

</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="csharp">

<dl class="resources-properties"><dt
        class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>The unique name of the resource.</dd><dt
        class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#inputs">CatArgs</a></span>
    </dt>
    <dd>The arguments to resource properties.</dd><dt
        class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>
    </dt>
    <dd>Bag of options to control resource&#39;s behavior.</dd></dl>

</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="java">

<dl class="resources-properties"><dt
        class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">String</span>
    </dt>
    <dd>The unique name of the resource.</dd><dt
        class="property-required" title="Required">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#inputs">CatArgs</a></span>
    </dt>
    <dd>The arguments to resource properties.</dd><dt
        class="property-optional" title="Optional">
        <span>options</span>
        <span class="property-indicator"></span>
        <span class="property-type">CustomResourceOptions</span>
    </dt>
    <dd>Bag of options to control resource&#39;s behavior.</dd></dl>

</pulumi-choosable>
</div>



### Constructor example

The following reference example uses placeholder values for all [input properties](#inputs).
<div>
<pulumi-chooser type="language" options="csharp,go,typescript,python,yaml,java"></pulumi-chooser>
</div>


<div>
<pulumi-choosable type="language" values="csharp">

```csharp
var catResource = new Example.Cat("catResource");
```

</pulumi-choosable>
</div>


<div>
<pulumi-choosable type="language" values="go">

```go
example, err := example.NewCat(ctx, "catResource", nil)
```

</pulumi-choosable>
</div>


<div>
<pulumi-choosable type="language" values="java">

```java
var catResource = new Cat("catResource");
```

</pulumi-choosable>
</div>


<div>
<pulumi-choosable type="language" values="python">

```python
cat_resource = example.Cat("catResource")
```

</pulumi-choosable>
</div>


<div>
<pulumi-choosable type="language" values="typescript">

```typescript
const catResource = new example.Cat("catResource", {});
```

</pulumi-choosable>
</div>


<div>
<pulumi-choosable type="language" values="yaml">

```yaml
type: example:Cat
properties: {}
```

</pulumi-choosable>
</div>



## Cat Resource Properties {#properties}

To learn more about resource properties and how to use them, see [Inputs and Outputs](/docs/intro/concepts/inputs-outputs) in the Architecture and Concepts docs.

### Inputs

<pulumi-choosable type="language" values="python">
<p>
In Python, inputs that are objects can be passed either as <a href="/docs/languages-sdks/python/#inputs-and-outputs">argument classes or as dictionary literals</a>.
</p>
</pulumi-choosable>

The Cat resource accepts the following [input](/docs/intro/concepts/inputs-outputs) properties:



<div>
<pulumi-choosable type="language" values="csharp">
<dl class="resources-properties"></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="go">
<dl class="resources-properties"></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="java">
<dl class="resources-properties"></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="javascript,typescript">
<dl class="resources-properties"></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="python">
<dl class="resources-properties"></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="yaml">
<dl class="resources-properties"></dl>
</pulumi-choosable>
</div>


### Outputs

All [input](#inputs) properties are implicitly available as output properties. Additionally, the Cat resource produces the following output properties:



<div>
<pulumi-choosable type="language" values="csharp">
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="id_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#id_csharp" style="color: inherit; text-decoration: inherit;">Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>The provider-assigned unique ID for this managed resource.</dd><dt class="property-"
            title="">
        <span id="foes_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#foes_csharp" style="color: inherit; text-decoration: inherit;">Foes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, Toy&gt;</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="friends_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#friends_csharp" style="color: inherit; text-decoration: inherit;">Friends</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">List&lt;Toy&gt;</a></span>
    </dt>
    <dd></dd><dt class="property- property-replacement"
            title="">
        <span id="name_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#name_csharp" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="other_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#other_csharp" style="color: inherit; text-decoration: inherit;">Other</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">Pulumi.<wbr>Example.<wbr>God</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="toy_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#toy_csharp" style="color: inherit; text-decoration: inherit;">Toy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="go">
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="id_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#id_go" style="color: inherit; text-decoration: inherit;">Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>The provider-assigned unique ID for this managed resource.</dd><dt class="property-"
            title="">
        <span id="foes_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#foes_go" style="color: inherit; text-decoration: inherit;">Foes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]Toy</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="friends_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#friends_go" style="color: inherit; text-decoration: inherit;">Friends</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">[]Toy</a></span>
    </dt>
    <dd></dd><dt class="property- property-replacement"
            title="">
        <span id="name_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#name_go" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="other_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#other_go" style="color: inherit; text-decoration: inherit;">Other</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">God</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="toy_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#toy_go" style="color: inherit; text-decoration: inherit;">Toy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="java">
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="id_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#id_java" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">String</span>
    </dt>
    <dd>The provider-assigned unique ID for this managed resource.</dd><dt class="property-"
            title="">
        <span id="foes_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#foes_java" style="color: inherit; text-decoration: inherit;">foes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">Map&lt;String,Toy&gt;</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="friends_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#friends_java" style="color: inherit; text-decoration: inherit;">friends</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">List&lt;Toy&gt;</a></span>
    </dt>
    <dd></dd><dt class="property- property-replacement"
            title="">
        <span id="name_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#name_java" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">String</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="other_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#other_java" style="color: inherit; text-decoration: inherit;">other</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">God</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="toy_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#toy_java" style="color: inherit; text-decoration: inherit;">toy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="javascript,typescript">
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="id_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#id_nodejs" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>The provider-assigned unique ID for this managed resource.</dd><dt class="property-"
            title="">
        <span id="foes_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#foes_nodejs" style="color: inherit; text-decoration: inherit;">foes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: Toy}</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="friends_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#friends_nodejs" style="color: inherit; text-decoration: inherit;">friends</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy[]</a></span>
    </dt>
    <dd></dd><dt class="property- property-replacement"
            title="">
        <span id="name_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#name_nodejs" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="other_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#other_nodejs" style="color: inherit; text-decoration: inherit;">other</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">God</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="toy_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#toy_nodejs" style="color: inherit; text-decoration: inherit;">toy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="python">
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="id_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#id_python" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>The provider-assigned unique ID for this managed resource.</dd><dt class="property-"
            title="">
        <span id="foes_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#foes_python" style="color: inherit; text-decoration: inherit;">foes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">Mapping[str, Toy]</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="friends_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#friends_python" style="color: inherit; text-decoration: inherit;">friends</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Sequence[Toy]</a></span>
    </dt>
    <dd></dd><dt class="property- property-replacement"
            title="">
        <span id="name_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#name_python" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="other_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#other_python" style="color: inherit; text-decoration: inherit;">other</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">God</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="toy_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#toy_python" style="color: inherit; text-decoration: inherit;">toy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="yaml">
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="id_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#id_yaml" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">String</span>
    </dt>
    <dd>The provider-assigned unique ID for this managed resource.</dd><dt class="property-"
            title="">
        <span id="foes_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#foes_yaml" style="color: inherit; text-decoration: inherit;">foes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">Map&lt;Property Map&gt;</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="friends_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#friends_yaml" style="color: inherit; text-decoration: inherit;">friends</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">List&lt;Property Map&gt;</a></span>
    </dt>
    <dd></dd><dt class="property- property-replacement"
            title="">
        <span id="name_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#name_yaml" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">String</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="other_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#other_yaml" style="color: inherit; text-decoration: inherit;">other</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">example:God</span>
    </dt>
    <dd></dd><dt class="property-"
            title="">
        <span id="toy_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#toy_yaml" style="color: inherit; text-decoration: inherit;">toy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Property Map</a></span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>







## Supporting Types



<h4 id="toy">
Toy<pulumi-choosable type="language" values="python,go" class="inline">, Toy<wbr>Args</pulumi-choosable>
</h4>

<div>
<pulumi-choosable type="language" values="csharp">
<dl class="resources-properties"><dt class="property-optional"
            title="Optional">
        <span id="associated_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#associated_csharp" style="color: inherit; text-decoration: inherit;">Associated</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd><dt class="property-optional property-replacement"
            title="Optional">
        <span id="color_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#color_csharp" style="color: inherit; text-decoration: inherit;">Color</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd></dd><dt class="property-optional"
            title="Optional">
        <span id="wear_csharp">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#wear_csharp" style="color: inherit; text-decoration: inherit;">Wear</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="go">
<dl class="resources-properties"><dt class="property-optional"
            title="Optional">
        <span id="associated_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#associated_go" style="color: inherit; text-decoration: inherit;">Associated</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd><dt class="property-optional property-replacement"
            title="Optional">
        <span id="color_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#color_go" style="color: inherit; text-decoration: inherit;">Color</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd></dd><dt class="property-optional"
            title="Optional">
        <span id="wear_go">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#wear_go" style="color: inherit; text-decoration: inherit;">Wear</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="java">
<dl class="resources-properties"><dt class="property-optional"
            title="Optional">
        <span id="associated_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#associated_java" style="color: inherit; text-decoration: inherit;">associated</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd><dt class="property-optional property-replacement"
            title="Optional">
        <span id="color_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#color_java" style="color: inherit; text-decoration: inherit;">color</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">String</span>
    </dt>
    <dd></dd><dt class="property-optional"
            title="Optional">
        <span id="wear_java">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#wear_java" style="color: inherit; text-decoration: inherit;">wear</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">Double</span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="javascript,typescript">
<dl class="resources-properties"><dt class="property-optional"
            title="Optional">
        <span id="associated_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#associated_nodejs" style="color: inherit; text-decoration: inherit;">associated</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd><dt class="property-optional property-replacement"
            title="Optional">
        <span id="color_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#color_nodejs" style="color: inherit; text-decoration: inherit;">color</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd></dd><dt class="property-optional"
            title="Optional">
        <span id="wear_nodejs">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#wear_nodejs" style="color: inherit; text-decoration: inherit;">wear</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="python">
<dl class="resources-properties"><dt class="property-optional"
            title="Optional">
        <span id="associated_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#associated_python" style="color: inherit; text-decoration: inherit;">associated</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Toy</a></span>
    </dt>
    <dd></dd><dt class="property-optional property-replacement"
            title="Optional">
        <span id="color_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#color_python" style="color: inherit; text-decoration: inherit;">color</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd></dd><dt class="property-optional"
            title="Optional">
        <span id="wear_python">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#wear_python" style="color: inherit; text-decoration: inherit;">wear</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>

<div>
<pulumi-choosable type="language" values="yaml">
<dl class="resources-properties"><dt class="property-optional"
            title="Optional">
        <span id="associated_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#associated_yaml" style="color: inherit; text-decoration: inherit;">associated</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#toy">Property Map</a></span>
    </dt>
    <dd></dd><dt class="property-optional property-replacement"
            title="Optional">
        <span id="color_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#color_yaml" style="color: inherit; text-decoration: inherit;">color</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">String</span>
    </dt>
    <dd></dd><dt class="property-optional"
            title="Optional">
        <span id="wear_yaml">
<a data-swiftype-name="resource-property" data-swiftype-type="text" href="#wear_yaml" style="color: inherit; text-decoration: inherit;">wear</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">Number</span>
    </dt>
    <dd></dd></dl>
</pulumi-choosable>
</div>


<h2 id="package-details">Package Details</h2>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="">example </a></dd>
	<dt>License</dt>
	<dd></dd>
</dl>
