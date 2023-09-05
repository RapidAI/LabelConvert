---
weight: 565
title: "Prism"
icon: change_history
description: "How to use the Prism Shortcode for syntax highlighting code blocks."
date: 2022-11-28T04:05:31+00:00
lastmod: 2022-11-28T04:05:31+00:00
draft: false
images: []
toc: true
---

## Prism Shortcode

When Prism is enabled in `hugo.toml` syntax highlighting can also be achieved using a paired Prism shortcode. The code language is declared using the `lang` parameter:

```go
{{</* prism lang="html" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism */>}}
```

All code blocks highlighted by Prism feature the [Copy to Clipboard Button](https://prismjs.com/plugins/copy-to-clipboard/) plugin. Hover over (or tap if on mobile) the examples above and the copy button appears in the top right hand corner of the code block. Click this button to copy the code to your clipboard.

## Line Highlighting

The Prism shortcode can highlight specific lines and/or line ranges in code blocks using the `line` parameter:
```go
{{</* prism lang="html" line="2-4,6" >}}
<html>
  <head>
  ...
{{< /prism */>}}
```
See the rendered example below:

{{< prism lang="html" line="2-4,6" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism >}}

## Line Numbers

Add line numbers to your code with the `line-numbers="true"` parameter:

{{< prism lang="html" line-numbers="true" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism >}}

The number at which the line starts can be specified by the `start` parameter. e.g. `start="48"`:

{{< prism lang="html" line-numbers="true" start="48" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism >}}

## Line Number Anchors

Specific lines in highlighted code blocks can be linked when both the `line-numbers` and `linkable-line-numbers` options are `true`:

```go
{{</* prism lang="html" linkable-line-numbers="true" line-numbers="true" >}}
<html>
  <head>
  ...
{{< /prism */>}}
```
Rendered code block:

{{< prism lang="html" linkable-line-numbers="true" line-numbers="true" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism >}}

Clicking on any of the line numbers above will update the hash of the current page to link to that specific line.

{{% alert context="info" %}}
All `<pre>` elements of Prism code blocks have an auto-generated id attribute. This id is a combination of the unique hash of the code block content plus it's unique position on the page. The generated hash can be overridden using a Custom id set via the `id` option.

The url format follows `#{hash-id}.{lines}`, where `{hash-id}` is the auto-generated hash value of the code block and `{lines}` is one or more lines or line ranges that follows the [line highlighting format](#line-highlighting).

For example, `line 8` in the code block below can be linked using the following anchor [#adea9eb.8](#adea9eb.8):

{{% /alert %}}

{{< prism lang="html" line="2-4,6" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism >}}


## Combined Line Parameters

Prism's [Line Highlighting](https://prismjs.com/plugins/line-highlight/) & [Line Numbers](https://prismjs.com/plugins/line-numbers/) plugins are compatible with each other. So the `line` & `line-numbers` options can be combined to display both, line numbers and highlight specified lines in a code block:

```go
{{</* prism lang="html" line-numbers="true" line="2-4,6" >}}
<html>
  <head>
  ...
{{< /prism */>}}
```
This renders the following code block:

{{< prism lang="html" line-numbers="true" line="2-4,6" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism >}}

Combining `line` & `start` options requires the use of the `line-offset` option:

```go
{{</* prism lang="html" line-numbers="true" start="48" line="49-51,54" line-offset="48" >}}
<html>
  <head>
  ...
{{< /prism */>}}
```
This renders the following code block:

{{< prism lang="html" line-numbers="true" start="48" line="49-51,54" line-offset="48" >}}
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
{{< /prism >}}

## File Highlight

External files can be fetched and highlighted using the File Highlight option. Use the `src` parameter to retrieve an external file, like so:
```go
{{</* prism src="https://raw.githubusercontent.com/colinwilson/lotusdocs/release/SECURITY.md" /*/>}}
```
Result:

{{< prism src="https://raw.githubusercontent.com/colinwilson/lotusdocs/release/SECURITY.md" />}}

Use the `src-range` parameter to retrieve a specific line range from an external file. `src-range="32,46"` will fetch lines 32 to 46 of the file specified by the `src` parameter:
```go
{{</* prism src-range="32,46" src="https://raw.githubusercontent.com/colinwilson/lotusdocs/release/data/landing.yaml" line-numbers="true" /*/>}}
```
`src-range` can be used with the [`line-numbers`](#line-numbers) option to number the retrieved range. So the above shortcode produces the following code block:

{{< prism src="https://raw.githubusercontent.com/colinwilson/lotusdocs/release/data/landing.yaml" src-range="32,46" line-numbers="true" />}}

{{% alert context="info" %}}
See Prism's docs for more info on the [File Highlight](https://prismjs.com/plugins/file-highlight/) plugin.
{{% /alert %}}

## Disable Prism

Prism syntax highlighting can be disabled by setting `[params.docs.prism]` to `false` in the `hugo.toml` configuration file.

## Command Line

TBC