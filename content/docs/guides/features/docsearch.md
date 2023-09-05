---
weight: 525
title: "DocSearch"
description: "DocSearch is a free and powerful Server Side Search plugin integrated with Lotus Docs."
icon: search
date: 2023-07-01T14:09:15+00:00
lastmod: 2023-08-04T00:22:15+00:00
draft: false
images: []
---

![DocSearch Logo](https://res.cloudinary.com/lotuslabs/image/upload/v1691600620/Lotus%20Docs/images/docsearch_logo_mod_bikkhc.svg)

## What is DocSearch?

[DocSearch](https://docsearch.algolia.com/) is a unique, free search plugin, specifically designed for technical documentation for open-source projects or technical blogs. Providing fast, accurate search options, DocSearch empowers visitors to find the information they need as quickly as possible. With the DocSearch plugin enabled, integrating search into your Lotus Docs site takes just a few moments.

## How does DocSearch work?

Much like other search engines, DocSearch uses a scraper to index your site content; in simple terms, the scraper scans your website and stores the data, which it can then collate to make a custom search that is effective for your site. Uniquely, DocSearch is targeted at documentation specifically; this means it's designed to help users more effectively find answers to specific questions or subjects within a narrow scope rather than looking for more generalised relevance, and it also offers autocomplete functionality to help users locate the sections that will be more helpful in answering their query.

With the data collected, Algolia will automatically configure a search relevant to your site content, then provide methods to integrate this search into your site. The functionality for the search is handled by DocSearch itself; processing the search query and delivering results occurs separate from your site’s infrastructure.

## Why DocSearch?

DocSearch is designed purely to provide efficient, relevant documentation searches; this means that it will be more efficient and effective at answering specific queries and pointing you to relevant sections in the documentation, rather than the more general searches that Google or other search engines provide.

If you're running a website providing technical documentation on an open-source project, then DocSearch is the perfect choice as your search provider.

## DocSearch requirements

DocSearch's mission is to make finding relevant content in technical documentation easier, rather than to create a general search engine that any site can use. Therefore, in order to use DocSearch, each site must meet certain criteria.

### To be eligible to use DocSearch, your website must meet these conditions:

1. Your website must be publicly available so that DocSearch can index it.

2. Your website must be a documentation site for an open-source project or a technical blog. Algolia will reduce the scope of the data they collect for searches to helpful pages only.

3. Your website is production-ready; that is, already contains  relevant and useful documentation content. Algolia will not accept placeholder or lorem ipsum websites intended to be updated later.

## How to get started?

Once your website is online and ready to add search functionality, you should [submit an application to DocSearch](https://docsearch.algolia.com/apply/) via their frontpage; the form in the header of the site will allow you to do this. You only need provide the website URL and your email address so you can receive the search credentials once they are ready; note that you will also need to be the owner of the site in question and verify this when submitting your application. Once Algolia accepts your submission they will send you the credentials for enabling your search via email.

After receiving the confirmation email, you will need to copy the following data in order to add it into the plugin options:

- **Application ID**
- **API Key**
- **Index Name**

Once the plugin has been enabled and the relevant data added, DocSearch will crawl your website every 7 days to ensure your search is up-to-date. By default Lotus Docs generates a complete sitemap for you. DocSearch will make use of this sitemap to better track changes to content.

## Enabling the DocSearch Plugin

To enable DocSearch, set the values to parameters nested under `[params.docsearch]` in your configuration file using the credentials emailed to you by Algolia after the submitted site was approved.

{{< tabs tabTotal="3">}}
{{% tab tabName="hugo.toml" %}}

```toml
[params.docsearch] # Parameters for DocSearch
        appID     = "FLVV3WOCO5"                       # DocSearch Application ID (or set env variable HUGO_PARAM_DOCSEARCH_appID)
        apiKey    = "9eeee4fac1e6cf21438cc9736e5112fc" # DocSearch Search-Only API (Public) Key (or set env variable HUGO_PARAM_DOCSEARCH_apiKey)
        indexName = "lotusdocs.dev"                    # Index Name on which to perform search (or set env variable HUGO_PARAM_DOCSEARCH_indexName)
```

{{% /tab %}}
{{% tab tabName="hugo.yaml" %}}

```yaml
params:
    docsearch:
        appID: "FLVV3WOCO5"
        apiKey: "9eeee4fac1e6cf21438cc9736e5112fc"
        indexName: "lotusdocs.dev"
```

{{% /tab %}}
{{% tab tabName="hugo.json" %}}

```json
{
   "params": {
        "docsearch": {
            "appID": "FLVV3WOCO5",
            "apiKey": "9eeee4fac1e6cf21438cc9736e5112fc",
            "indexName": "lotusdocs.dev"
        }
   }
}
```

{{% /tab %}}
{{< /tabs >}}

{{% alert context="info" text="There's not much sense to having multiple search engines simultaneously active on a single website. Therefore, **FlexSearch** is automatically disabled whenever **DocSearch** is configured." /%}}