---
weight: 520
title: "FlexSearch"
description: "Search your Lotus Docs site using the FlexSearch Static site Search plugin."
icon: search
date: 2023-06-20T15:30:15+00:00
lastmod: 2023-06-20T15:30:15+00:00
draft: false
images: []
---

{{% alert context="warning" text="**Caution** - This documentation is in progress" /%}}

## What is FlexSearch?

FlexSearch is a Static Search plugin that provides a fast and simple search experience for your Lotus Docs site. Static Search provides instant, dynamic results for any search terms, and includes a wealth of options and settings to fine-tune the functionality to best suit the needs of your site visitors.

## How does FlexSearch work?

FlexSearch works via a mechanism known as **Contextual Search** (invented by [Thomas Wilkerling](https://github.com/ts-thomas)). A Contextual Search [boosts queries to a complete new level](https://nextapps-de.github.io/flexsearch/bench/) but also requires some additional memory (depending on depth). The basic idea of this concept is to limit relevance by its context instead of calculating relevance through the whole distance of its corresponding document. This way contextual search also [improves the results of relevance-based queries](https://nextapps-de.github.io/flexsearch/bench/match.html) on large Lotus Docs sites with many pages.

![Model of Contextual-based Scoring](https://res.cloudinary.com/lotuslabs/image/upload/v1688597756/Lotus%20Docs/images/contextual-index_gnhpqm.webp "**Model of Contextual-based Scoring** - Copyright 2018-2021 Thomas Wilkerling Nextapps GmbH - [*source*](https://github.com/nextapps-de/flexsearch/blob/master/README.md#contextual-search)")

## Enabling FlexSearch

{{% alert context="info" text="**FlexSearch is enabled by default**" /%}}

To disable it, simply set the `enabled` parameter nested under `[params.flexsearch]` in your configuration file to `false`. That's it!

{{< tabs tabTotal="3">}}
{{% tab tabName="hugo.toml" %}}

```toml
[params.flexsearch]
    enabled = false
```

{{% /tab %}}
{{% tab tabName="hugo.yaml" %}}

```yaml
params:
    flexsearch:
        enabled: false
```

{{% /tab %}}
{{% tab tabName="hugo.json" %}}

```json
{
   "params": {
        "flexsearch": {
            "enabled": false
        }
   }
}
```

{{% /tab %}}
{{< /tabs >}}

## How to search your site using FlexSearch

With FlexSearch enabled you should see a search button in the top navigation bar:

![FlexSearch Screenshot | Lotus Docs](https://res.cloudinary.com/lotuslabs/image/upload/v1688442518/Lotus%20Docs/images/lotus_docs_flexsearch_ui_components_diagram_v1.1_jp2f0l.webp "FlexSearch components: **1.** Search Button **2.** Search Input Bar **3.** Search Result | Lotus Docs")

Click on the search button (or use `ctrl` + `/`) to reveal and activate the search input bar. Start typing a search query and the result(s) will automatically appear in a 'suggestions' panel underneath. Click a search result to navigate to said page.

## Advanced options

The various settings below offer more advanced control over how FlexSearch indexes your site content.

{{% alert context="info" %}}
**Note:** Since the default settings[^1] for FlexSearch are capable of providing accurate search results, most Lotus Docs users can ignore all the options in this section. However, if your site has a large number of posts, the generated index file can be relatively large; in such cases it may be beneficial to limit indexing to specific elements to reduce the overall size of the file.
{{% /alert %}}

All FlexSearch options should be declared under `[params.flexsearch]`:

```toml
[params.flexsearch]
    enabled             = true
    tokenize            = "full" # default is "forward"
    cache               = 100    # default is 100
    optimize            = true   # default is true
    minQueryChar        = 3      # default is 0 (disabled)
    maxResult           = 5      # default is 5
    searchSectionsIndex = []
```

The following FlexSearch options are available:
### Tokenize

This option sets the behaviour for the search process; that is, how it looks for the words that are being searched for and how effective the search is. Generally-speaking, the `full` setting will provide the most effective search experience, but alternative, simpler options may be used on large websites to limit the amount of memory required for the search. The available settings for this option are:

- **`strict`** - Only exact matches for the search term will be shown in the results.

- **`forward`** (**default**) - Words are searched for starting from the first letter in a forward order, allowing partial matches to be displayed; unfinished words or words with mispellings at the end will still display results e.g. if searching for 'Testing', entering only 'Tes' will provide some results.

- **`reverse`** - A result will be shown when the letters of the search term occur in both forward or reverse order, provide even more support for mispellings or incomplete searches e.g. if searching for 'Testing', entering either 'Tes' or 'ing' will provide some results.

- **`full`** - Combines all of the above, plus partial matches for the middle section of the search term e.g. if searching for 'Testing', entering either 'Tes', 'ing' or 'sti', or other combinations thereof will provide some results.

### Cache

If enabled, FlexSearch will use the available cache to store popular searches in order to provide instant search when typing in the search bar. The options available in this section are:

- **`true`** - **no size limit** - Searches will be saved to provide dynamic searches when typing and autocomplete suggestions if enabled.

- **`false`** - **Disabled** - No searches will be stored; searches may run slower than when the cache is enabled.

- **`<number>`** - **with size limit** - The number entered in this field defines the maximum number of searches that FlexSearch should save for dynamic searches and suggestions. By default, this is set to `100`.

### Optimize

When enabled it uses a memory-optimized stack flow for the index.

- **`true`** - Enable memory-optimized stack flow for the index.

- **`false`** - Disabled

### Minimum query character count

The `minQueryChar` parameter defines the minimum number of characters typed before any search results are rendered. A higher number decreases memory allocation:

- **`0`** - **Disabled** - (**default**) Search suggestions are presented as soon as an entry is made in the search input.

- **`<number>`** - The minimum number of characters required before search suggestions are presented.

### Maximum number of results

You can control the maximum number of results presented per a search via the `maxResult` parameter:

- **`<number>`** - Maximum number of results displayed in the suggestions box for a search query. The default is `5`.

[^1]: [https://github.com/colinwilson/lotusdocs](https://github.com/colinwilson/lotusdocs/blob/release/layouts/partials/docs/footer/flexsearch.html#L90-L93)