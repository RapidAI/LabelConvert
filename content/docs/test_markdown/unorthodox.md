---
title: "Unorthodox Cases 🦄"
icon: fingerprint
description: "A custom markdown example page for testing of specific or rare styling cases."
lead: "An example markdown page for testing purposes."
date: 2022-10-20T00:29:15+00:00
lastmod: 2022-10-20T00:29:15+00:00
draft: true
images: []
weight: 10040
toc: true
---

## Shortcode Notifications/Alerts

Various alert notification styles:

{{% alert %}}
This is the default alert without any options.<br>No `context` or `icon` parameter defined.
{{% /alert %}}

{{% alert  context="info" %}}
**Markdown** and <em>HTML</em> will be rendered. This next sentence [demonstrates](https://colinwilson.uk) the colour of a link inside an alert box. We’re currently designing a new way to integrate the Payment Element, which allows you to create the PaymentIntent or SetupIntent after you render the Payment Element. If you’re interested in learning more about this feature.

*Beginning* of a second paragraph.
{{% /alert %}}

{{% alert icon="🎃" context="info" %}}
The default <strong>context</strong> icon can be overridden with an emoji by setting the named parameter <code>icon</code> to the emoji of choice. e.g. <code>{{\< alert icon="🎃" text="Make sure to always self-close the alert shortcode." />}}</code>
{{% /alert %}}

{{% alert icon=" " context="primary" %}}
The default <strong>context</strong> icon can be overridden to display no icon by setting the named parameter <code>icon</code> to an empty space. e.g.
```
{{\< alert icon=" " text="Make sure to always self-close the alert shortcode." />}}
```
{{% /alert %}}

{{% alert icon="🌕" context="light" text="An <strong>light</strong> context alert using an emoji (:full_moon:) instead of the default <strong>icon</strong>." /%}}

{{< alert icon="🌑" context="dark" text="An alert using an emoji (:jack_o_lantern:) instead of the default <strong>context</strong> icon." />}}

{{% alert context="primary" %}}
The Tutorial is intended for beginner to intermediate users.

This next sentence [demonstrates](https://colinwilson.uk) the colour of a link inside an alert box.
{{% /alert %}}

{{< alert context="success" text="The Tutorial is intended for novice to intermediate users.<br> Hello World" />}}

{{< alert context="warning" text="The Tutorial is intended for novice to intermediate users.<br> Hello World" />}}

{{< alert context="danger" text="The Tutorial is intended for novice to intermediate users.<br> Hello World" />}}

{{% alert context="light" %}}
The Tutorial is intended for novice to intermediate users.<br> Hello World
This next sentence [demonstrates](https://colinwilson.uk) the colour of a link inside an alert box.
{{% /alert %}}

## Small Image

![Redis](https://res.cloudinary.com/qunux/image/upload/v1643320066/isometric_redis_proxy_icon_nmf5dm.webp)
## Large Image

![Argo CD Vault Plugin](https://res.cloudinary.com/qunux/image/upload/c_scale,w_1200/v1651719756/argocd_vault_plugin_lg_v2.7b_prz2ad.webp)
## Super Large Image

![External Secrets with Argo CD](https://res.cloudinary.com/qunux/image/upload/v1660827109/argocd_eso_how_it_works_v1.3_lg_yw7zen.webp)

## Ordered/Unordered Heading lists

1. # Heading \<h1\>
2. #  Heading \<h1\>

- # Heading \<h1\>

<!-- -->
1. ## Heading \<h2\>
2. ##  Heading \<h2\>

- ## Heading \<h2\>

<!-- -->
1. ### Heading \<h3\>
2. ###  Heading \<h3\>

- ### Heading \<h3\>

<!-- -->
1. #### Heading \<h4\>
2. ####  Heading \<h4\>

- #### Heading \<h4\>

<!-- -->
1. ##### Heading \<h5\>
2. #####  Heading \<h5\>

- ##### Heading \<h5\>

<!-- -->
1. ###### Heading \<h6\>
2. ######  Heading \<h6\>

- ###### Heading \<h6\>
