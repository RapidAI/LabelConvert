---
weight: 550
title: "Alerts"
icon: notification_important
description: "How to use Alert Shortcodes to render custom page alerts in markdown."
lead: "Alerts."
date: 2022-11-22T13:42:31+00:00
lastmod: 2022-11-22T13:42:31+00:00
draft: false
images: []
toc: true
---

## Adding a Page Alert

Page alerts can be added to your markdown using the following shortcode:

```go
{{</* alert text="This is the default alert. It consists of a default theme colour and icon." /*/>}}
```

The above code results in the following alert:

{{< alert text="This is the default alert. It consists of a default theme colour and icon." />}}

## Alert with Context

Add context to an alert via the `context` parameter:

```go
{{</* alert context="info" text="This is an alert with an <strong>info</strong> context. It consists of the info theme colour and icon." /*/>}}
```

Here's what is rendered:

{{< alert context="info" text="This is an alert with an <strong>info</strong> context. It consists of the info theme colour and icon." />}}

Additional alert contexts include `success`, `danger`, `warning`, `primary`, `light` and `dark`:

{{< alert context="success" text="This is an alert with a <strong>success</strong> context. It consists of the success theme colour and icon." />}}

{{< alert context="danger" text="This is an alert with a <strong>danger</strong> context. It consists of the danger theme colour and icon." />}}

{{< alert context="warning" text="This is an alert with a <strong>warning</strong> context. It consists of the warning theme colour and icon." />}}

{{< alert context="primary" text="This is an alert with a <strong>primary</strong> context. Its theme and icon colors match those of the current primary theme colour." />}}

{{< alert context="light" text="This is an alert with a <strong>light</strong> context. It consists of the light theme colour. The light alert has no default icon." />}}

{{< alert context="dark" text="This is an alert with a <strong>dark</strong> context. It consists of the dark theme colour. The dark alert has no default icon." />}}

## Alert with Custom Emoji Icon

The default icon for an alert context can be substituted with an emoji using the `icon` parameter:

```go
{{</* alert icon="🍅" context="info" text="This is an <strong>info</strong> context alert with a tomato emoji replacing the default icon. The info theme colour remains unchanged." /*/>}}
```

{{< alert icon="🍅" context="info" text="This is an <strong>info</strong> context alert with a tomato emoji replacing the default icon. The info theme colour remains unchanged." />}}

## Alert with No Icon

Setting the `icon` parameter to an empty space, `icon=" "`, will render an alert with no icon:

```go
{{</* alert icon=" " context="info" text="This <strong>info</strong> context alert has no icon." /*/>}}
```

{{< alert icon=" " context="info" text="This <strong>info</strong> context alert has no icon." />}}

{{% alert context="warning" %}}
**N.B.** The icon parameter **must** contain a space. Setting it to `icon=""` will render the default icon.
{{% /alert %}}

## Render Markdown & HTML inside an Alert

{{% alert context="warning" %}}
So `%` delimited alerts render correctly, ensure you have `unsafe = true` set under `[markup.goldmark.renderer]` in your `hugo.toml` configuration file[^1].
{{% /alert %}}

Use a [paired shortcode](https://gohugo.io/content-management/shortcodes/) with the `%` delimiter[^2] to render Markdown and HTML inside an alert:

```go
{{%/* alert icon="🛒" context="success" %}}
This ***paired shortcode*** alert contains a **markdown** list and header:

#### My Shopping List:
1. Tomatoes
2. Bananas
3. Pineapples

and a sentence <em>styled</em> using <strong>HTML</strong> tags such as \<strong\> and \<em\>
{{% /alert */%}}
```

{{% alert icon="🛒" context="success" %}}
This ***paired shortcode*** alert contains a **markdown** list and header:

#### My Shopping List:
1. Tomatoes
2. Bananas
3. Pineapples

and a sentence <em>styled</em> using <strong>HTML</strong> tags such as \<strong\> and \<em\>
{{% /alert %}}

[^1]: [Markdown alerts do not seem to display background color](https://github.com/colinwilson/lotusdocs/issues/49#issuecomment-1701170810)
[^2]: [Shortcodes with Markdown - gohugo.io](https://gohugo.io/content-management/shortcodes/#shortcodes-with-markdown)