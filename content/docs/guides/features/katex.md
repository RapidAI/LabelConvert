---
weight: 530
title: "KaTex"
description: "Fast Tex math rendering for your Lotus Docs site"
icon: "function"
date: "2023-08-26T20:43:23+01:00"
lastmod: "2023-08-26T20:43:23+01:00"
draft: false
toc: true
katex: true
---

$$
f\relax{x} = \int_{-\infty}^\infty
    \hat f\(\xi)\ e^{2 \pi i \xi x}
    \ d\xi
$$

<!-- $$
\begin{equation*}
   n \sim  10^{18} \mathrm{cm^{-3}} \left(\frac{100\mathrm{km}}{R}\right)^2 \left(\frac{10\mathrm{MeV}}{\langle E \rangle}\right).
\end{equation*}
$$ -->

<!-- $$
\int \frac{1}{x} dx = \ln \left| x \right| + C
$$ -->

## How to use KaTex with Lotus Docs

[KaTex](https://katex.org/) support is controlled by the `katex` parameter in your [front matter](https://gohugo.io/content-management/front-matter/) (**line 10 below**). Add and set it to `true` in your front matter to enable KaTex support for that page. This means KaTex support and resources are active only for pages that require it.

{{< prism lang="yaml" line="10" >}}
---
weight: 530
title: "KaTex"
description: "Fast Tex math rendering for your Lotus Docs site"
icon: "function"
date: "2023-08-26T20:43:23+01:00"
lastmod: "2023-08-26T20:43:23+01:00"
draft: true
toc: true
katex: true
---
{{< /prism >}}

## Writing LaTex in Markdown

Equations can be displayed either in block level or inline.

### Block display

Type an equation using double dollar signs as the delimiter:

```md
$$
\int \frac{1}{x} dx = \ln \left| x \right| + C
$$
```

**renders as**:

$$
\int \frac{1}{x} dx = \ln \left| x \right| + C
$$

### Inline display

Type an equation using single dollar signs as the delimiter:

```md
$
\int \frac{1}{x} dx = \ln \left| x \right| + C
$
```

**renders as**:

$
\int \frac{1}{x} dx = \ln \left| x \right| + C
$

## Syntax Rendering  Issues

As a consequence of Hugo rendering to HTML before KaTex renders to math[^1], there are some instances in which the KaTex equation syntax requires heavy escaping or alterations before rendering correctly. This can be time-consuming and frustrating (especially for inexperienced users). To avoid this, a [KaTex Shortcode]({{< ref "/docs/guides/shortcodes/katex" >}}) is available.

```go
{{</* katex >}}
$$
\begin{array} {lcl}
  L(p,w_i) &=& \dfrac{1}{N}\Sigma_{i=1}^N(\underbrace{f_r(x_2
  \rightarrow x_1
  \rightarrow x_0)G(x_1
  \longleftrightarrow x_2)f_r(x_3
  \rightarrow x_2
  \rightarrow x_1)}_{sample\, radiance\, evaluation\, in\, stage2}
  \\\\\\ &=&
  \prod_{i=3}^{k-1}(\underbrace{\dfrac{f_r(x_{i+1}
  \rightarrow x_i
  \rightarrow x_{i-1})G(x_i
  \longleftrightarrow x_{i-1})}{p_a(x_{i-1})}}_{stored\,in\,vertex\, during\,light\, path\, tracing\, in\, stage1})\dfrac{G(x_k
  \longleftrightarrow x_{k-1})L_e(x_k
  \rightarrow x_{k-1})}{p_a(x_{k-1})p_a(x_k)})
\end{array}
$$
{{< /katex */>}}
```
**renders as**:

{{< katex >}}
$$
\begin{array} {lcl}
  L(p,w_i) &=& \dfrac{1}{N}\Sigma_{i=1}^N(\underbrace{f_r(x_2
  \rightarrow x_1
  \rightarrow x_0)G(x_1
  \longleftrightarrow x_2)f_r(x_3
  \rightarrow x_2
  \rightarrow x_1)}_{sample\, radiance\, evaluation\, in\, stage2}
  \\\\\\ &=&
  \prod_{i=3}^{k-1}(\underbrace{\dfrac{f_r(x_{i+1}
  \rightarrow x_i
  \rightarrow x_{i-1})G(x_i
  \longleftrightarrow x_{i-1})}{p_a(x_{i-1})}}_{stored\,in\,vertex\, during\,light\, path\, tracing\, in\, stage1})\dfrac{G(x_k
  \longleftrightarrow x_{k-1})L_e(x_k
  \rightarrow x_{k-1})}{p_a(x_{k-1})p_a(x_k)})
\end{array}
$$
{{< /katex >}}

[^1]: [How to render math equations properly with KaTeX](https://discourse.gohugo.io/t/how-to-render-math-equations-properly-with-katex/40998/4)