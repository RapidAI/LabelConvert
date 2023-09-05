---
weight: 515
title: "Plausible Analytics"
description: "How to add Plausible Analytics to your Lotus Docs site."
icon: trending_up
date: 2022-12-29T16:28:15+00:00
lastmod: 2023-07-27T23:28:15+00:00
draft: false
images: []
---

[Plausible Analytics](https://plausible.io) is a simple, open source, lightweight (< 1 KB), privacy-focused alternative to Google Analytics. Plausible is completely independent, self-funded and bootstrapped. Read more about [Plausible Analytics](https://plausible.io/about).

![Plausible Analytics Dashboard Screenshot](https://res.cloudinary.com/lotuslabs/image/upload/v1673015990/Lotus%20Docs/Social%20Media/plausible-analytics-screenshot_ds_rdd_c6bi3o.webp)

## Why use Plausible Analytics?

As previously mentioned, Plausible is an open source, privacy-focused Google Analytics alternative. So what are the benefits of this?

- **Privacy by design** - Plausible, by design complies with [strict privacy policies](https://plausible.io/data-policy). Including: GDPR, CCPA, and PECR.
- **You own your data** - Plausible does **not** sell or share your data, or abuse your visitor's privacy. When using Plausible Analytics, you 100% own and control all of your website data. Your data is not being shared with or sold to any third-parties.
- **No personal data collected** - Plausible does not track and collect any personal data or personally identifiable information.
- **Open Source** - Plausible Analytics is completely open source so anyone can view, review and inspect the code they're running to verify whether their actions match their claims of privacy.
- **Your data is encrypted** - Plausible minimize their data collection and whatever is tracked is kept **fully secured**, **encrypted** and hosted on servers **in the EU** (European Union) to ensure it's covered by strict laws on data privacy.

You can read more about [Plausible Analytics and their polices](https://plausible.io/about).

## Create an Account with plausible.io

Before enabling Plausible Analytics in Lotus Docs, make sure to [register an account](https://plausible.io/docs/register-account) with them and add your site domain to your account; without an active account, no data can be collected by Plausible.

Make a note of the domain name that you entered when [adding your website to Plausible](https://plausible.io/docs/add-website), as this is required when enabling Plausible Analytics in Lotus Docs.

## Enable Plausible Analytics

To enable Plausible Analytics, provide the following parameters in your configuration file under `[params.plausible]`:

- **`dataDomain`** - Enter the domain name that you will be tracking through Plausible Analytics, e.g. `yourdomain.com`; make sure it's the same domain you entered when adding your website to your Plausible account.

- **`scriptURL`** - **optional** - If you're self-hosting Plausible, enter the URL that points to your self-hosted `script.js` file here, e.g. `https://plausible.yourdomain.com/js/script.js`. When not set, the `scriptURL` value defaults to `https://plausible.io/js/script.js`.

- **`eventAPI`** - **optional** - If you're [proxying Plausible](#proxying-plausible-through-vercel) requests via another service (e.g. [Vercel](https://plausible.io/docs/proxy/guides/vercel), [Netlify](https://plausible.io/docs/proxy/guides/netlify), [Cloudflare](https://plausible.io/docs/proxy/guides/cloudflare)), enter the appropriate event API path here e.g. `https://plausible.yourdomain.com/api/event`

{{< tabs tabTotal="3">}}
{{% tab tabName="hugo.toml" %}}

```toml
[params.plausible] # Parameters for Plausible Analytics
        dataDomain = "yourdomain.com"
        scriptURL  = "https://plausible.yourdomain.com/js/script.js"    # optional
        eventAPI   = "https://plausible.yourdomain.com/stats/api/event" # optional
```

{{% /tab %}}
{{% tab tabName="hugo.yaml" %}}

```yaml
params:
    plausible: # Parameters for Plausible Analytics
        dataDomain: "yourdomain.com"
        scriptURL: "https://plausible.yourdomain.com/js/script.js"   # optional
        eventAPI: "https://plausible.yourdomain.com/stats/api/event" # optional
```

{{% /tab %}}
{{% tab tabName="hugo.json" %}}

```json
{
   "params": {
        "plausible": {
            "dataDomain": "yourdomain.com",
            "scriptURL": "https://plausible.yourdomain.com/js/script.js",
            "eventAPI": "https://plausible.yourdomain.com/stats/api/event"
        }
   }
}
```

{{% /tab %}}
{{< /tabs >}}

## Proxying Plausible through Vercel

Some adblockers/browsers block every tracking script, even privacy-focused analytics like plausible.io. You can mitigate this by [proxying the script](https://plausible.io/docs/proxy/introduction).

[Vercel](https://vercel.com) is the preferred platform on which to deploy Lotus Docs themed sites. Follow the instructions below to setup proxying the Plausible script when hosting your Lotus Docs site on Vercel:

1. Create a `vercel.json` file at the root of your site:
   ```
   /vercel.json
   ```

2. Add the following JSON to rewrite calls within your Lotus Docs site to Plausible's resources:
   ```json
   {
        "rewrites": [
            {
                "source": "/stats/js/script.js",
                "destination": "https://plausible.io/js/script.js"
            },
            {
                "source": "/stats/api/event",
                "destination": "https://plausible.io/api/event"
            }
        ]
   }
   ```
   {{% alert context="info" text="you can use whatever paths you like here (the above example is prefixed with `/stats/`)." /%}}

3. Set Lotus Docs' `[params.plausible]` parameters to use the values configured above:
   {{< tabs tabTotal="3">}}
   {{% tab tabName="hugo.toml" %}}

   ```toml
    [params.plausible] # Parameters for Plausible Analytics
        dataDomain = "yourdomain.com"
        scriptURL  = "/stats/js/script.js"
        eventAPI   = "/stats/api/event"    # optional
   ```

   {{% /tab %}}
   {{% tab tabName="hugo.yaml" %}}

   ```yaml
    params:
        plausible: # Parameters for Plausible Analytics
            dataDomain: "yourdomain.com"
            scriptURL: "/stats/js/script.js"
            eventAPI: "/stats/api/event"     # optional
   ```

   {{% /tab %}}
   {{% tab tabName="hugo.json" %}}

   ```json
    {
        "params": {
            "plausible": {
                "dataDomain": "yourdomain.com",
                "scriptURL": "/stats/js/script.js",
                "eventAPI": "/stats/api/event"
            }
        }
    }
   ```

   {{% /tab %}}
   {{< /tabs >}}

{{% alert context="info" text="Plausible's documentation has [guides to settting up proxying](https://plausible.io/docs/proxy/introduction#are-you-concerned-about-missing-data) on many different hosting platforms." /%}}