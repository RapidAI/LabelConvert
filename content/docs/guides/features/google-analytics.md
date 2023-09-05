---
weight: 517
title: "Google Analytics v4"
description: "How to enable Google Analytics on your Lotus Docs site."
icon: trending_up
date: 2023-07-05T23:48:15+00:00
lastmod: 2023-07-05T23:48:15+00:00
draft: false
images: []
---

Lotus Docs utilises Hugo's internal [Google Analytics v4](https://support.google.com/analytics/#topic=9143232) template[^1].

{{% alert context="info" text="Starting **July 1, 2023**, Universal Analytics (UA) was **deprecated** and is [no longer processed](https://support.google.com/analytics/answer/11583528) by Google. Lotus Docs does not include support for UA." /%}}

## Enabling Google Analytics

To enable Google Analytics v4, simply provide your tracking ID in your configuration file:

{{< tabs tabTotal="3">}}
{{% tab tabName="hugo.toml" %}}

```toml
googleAnalytics = 'G-MEASUREMENT_ID'
```

{{% /tab %}}
{{% tab tabName="hugo.yaml" %}}

```yaml
googleAnalytics: G-MEASUREMENT_ID
```

{{% /tab %}}
{{% tab tabName="hugo.json" %}}

```json
{
   "googleAnalytics": "G-MEASUREMENT_ID"
}
```

{{% /tab %}}
{{< /tabs >}}

[^1]: [Hugo Google Analytics v4 Internal Template - gohugo.io](https://gohugo.io/templates/internal/#google-analytics)