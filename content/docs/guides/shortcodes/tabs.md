---
weight: 560
title: "Tabs"
icon: tab
description: "How to use the Lotus Docs tabs shortcode to render Bootstrap Tabs"
lead: "Use the Lotus docs tabs shortcode to render various tabs styles."
date: 2023-04-25T03:51:15+00:00
lastmod: 2023-04-25T22:08:15+00:00
draft: false
images: []
toc: true
---

The `tabs` shortcode leverages [Bootstrap's Tabs styling](https://getbootstrap.com/docs/5.3/components/navs-tabs/#tabs) to easily add Tabs to your markdown content. The shortcode is actually a combination of two separate shortcodes (`tab` and `tabs`) working together.

You need a minimum of one `tab` shortcode nested inside a `tabs` shortcode for the component to function:

```go
{{</* tabs tabTotal="1">}}
{{% tab tabName="Tab 1" %}}

**Tab 1 Content**

{{% /tab %}}
{{< /tabs */>}}
```

## Basic Tabs

The following example demonstrates how to create a basic multi tab navigation component using the `tabs` and `tab` shortcodes.

```go
{{</* tabs tabTotal="3">}}
{{% tab tabName="Windows" %}}

**Windows Content**

Example content specific to **Windows** operating systems

{{% /tab %}}
{{% tab tabName="MacOS" %}}

**MacOS Content**

Example content specific to **Mac** operating systems

{{% /tab %}}
{{% tab tabName="Linux" %}}

**Linux Content**

Example content specific to **Linux** operating systems

{{% /tab %}}
{{< /tabs */>}}
```

Renders:

{{< tabs tabTotal="3">}}
{{% tab tabName="Windows" %}}

**Windows Content**

Example content specific to **Windows** operating systems

{{% /tab %}}
{{% tab tabName="MacOS" %}}

**MacOS Content**

Example content specific to **Mac** operating systems

{{% /tab %}}
{{% tab tabName="Linux" %}}

**Linux Content**

Example content specific to **Linux** operating systems

{{% /tab %}}
{{< /tabs >}}

## Right Aligned Tabs

```go
{{</* tabs tabTotal="3" tabRightAlign="2">}}
{{% tab tabName="Tab 1" %}}

**Tab 1 Content**

{{% /tab %}}
{{% tab tabName="Tab 2" %}}

**Tab 2 Content**

{{% /tab %}}
{{% tab tabName="Tab 3" %}}

**Tab 3 Content**

{{% /tab %}}
{{< /tabs */>}}
```

Renders:

{{< tabs tabTotal="3" tabRightAlign="2">}}
{{% tab tabName="Tab 1" %}}

**Tab 1 Content**

{{% /tab %}}
{{% tab tabName="Tab 2" %}}

**Tab 2 Content**

{{% /tab %}}
{{% tab tabName="Tab 3"%}}

**Tab 3 Content**

{{% /tab %}}
{{< /tabs >}}

## How does it work?

### tabs.html

This is the parent shortcode that wraps around all nested tab shortcodes in the tab group and generates the tab navigation.

{{< table "table-striped" >}}
| Variable | Description |
|---------|------|
| `tabTotal` | This variable is used to generate the tab navigation. Simply set it to the amount of tab shortcodes you have. In the above example, since there are **three** nested tab shortcodes, you would set `tabTotal` to `3`. |
| `tabRightAlign` | This is an optional variable that if used will right align the tab number you inputted and all tabs after it. In the above example, since `tabRightAlign` is set to **two**, tabs 2 and 3 will be right aligned. |
{{< /table >}}

### tab.html

This is a child shortcode that is nested inside `tabs` shortcodes. Each tab shortcode equals one tab so add as many as you need. Please note, make sure `tabTotal` in the `tabs` shortcode is equal to the amount of tab shortcodes you define.

{{< table "table-striped" >}}
| Variable | Description |
|---------|------|
| `tabName` | This variable defines the title of the tab. |
{{< /table >}}

## Credit

Both `tab` and `tabs` shortcodes documented above are a modified versions of the open source [Hugo Dynamic Tabs](https://github.com/rvanhorn/hugo-dynamic-tabs/tree/bootstrap5) shortcodes. Thank you [rvanhorn](https://github.com/rvanhorn) 👍.