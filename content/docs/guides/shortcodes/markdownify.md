---
weight: 570
title: "Markdownify"
icon: edit_note
description: "A simple shortcode to render content as Markdown."
lead: "A shortcode to render Markdown."
date: 2023-04-28T16:35:15+00:00
lastmod: 2023-08-04T00:23:15+00:00
draft: false
images: []
toc: true
---

This shortcode parses its content as markdown.

## Usage

The following:

```go
{{</* markdownify >}}

**Bold Text**: Above a code block.

```html
<!-- An example HTML code block -->
<h1>Hello World</h1>

{{< /markdownify */>}}
```
Renders:

{{< markdownify >}}

**Bold Text**: Above a code block.

```html
<!-- An example HTML code block -->
<h1>Hello World</h1>
```

{{< /markdownify >}}

## Nested Shortcodes

The `markdownify` shortcode is especially useful in cases where you require portions of content nested inside another shortcode be parsed as Markdown.

For example, here's a paragraph of markdown text and a `prism` shortcode codeblock nested within a `tabs` shortcode:

```go
{{</* tabs tabTotal="1" >}}
{{< tab tabName="Tab 1" >}}

{{< markdownify >}}
### Markdownified Text

Some `markdownified` text inside a `tabs` shortcode

{{< /markdownify >}}

{{< prism lang="html" line="3,6" >}}
<html>
  <head>
    <title>A code block using the Prism Shortcode</title>
  </head>
  <p>
    This shortcode is nested inside a Tabs shortcode
  </p>
</html>
{{< /prism >}}

{{< /tab >}}
{{< /tabs */>}}
```

Renders:

{{< tabs tabTotal="1" >}}
{{< tab tabName="Tab 1" >}}

{{< markdownify >}}

***Markdownified Text***

Some `markdownified` text inside a `tabs` shortcode

{{< /markdownify >}}

{{< prism lang="html" line="3,6" >}}
<html>
  <head>
    <title>A code block using the Prism Shortcode</title>
  </head>
  <p>
    This shortcode is nested inside a Tabs shortcode
  </p>
</html>
{{< /prism >}}

{{< /tab >}}
{{< /tabs >}}