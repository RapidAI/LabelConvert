---
weight: 705
title: "Configuration"
icon: settings
description: "Reference table of configuration options for the Lotus Docs theme."
lead: ""
date: 2023-01-21T16:16:15+00:00
lastmod: 2023-01-21T16:16:15+00:00
draft: false
images: []
toc: true
---

A list of available configuration settings in the site configuration file, `hugo.toml`, `hugo.yaml`, or `hugo.json`:

## [params]

### Google Fonts

{{< table "table table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|--------|------|
| `google_fonts` | array | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Inter", "300, 400, 600, 700"],["Fira Code", "500, 700"]]`<br> This will load the Google [Inter](https://fonts.google.com/specimen/Inter) and [Fira Code](https://fonts.google.com/specimen/Fira+Code) fonts in the specified sizes. |
| `sans_serif_font` | string | System Font | Set the Sans Serif font. e.g. `"Inter"` |
| `secondary_font` | string | System Font | Set the Secondary font. e.g. `"Inter"` |
| `mono_font` | string | System Font | Set the Mono font. e.g. `"Fira Code"` |
{{</ table >}}

## [params.footer]

### Footer

{{< table "table table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `copyright` | string | N/A | Sets the footer copyright text for both the landing page and documentation site (**supports Markdown**) |
| `version` | boolean | `false` | Display the site's truncated `git` commit hash in the footer? **TBC** |
{{</ table >}}

## [params.social]

Social links are displayed as icons in the top left corner of the Lotus Docs theme. This goes for the landing page and docs site.

### Social Icon Links

{{< table "table table-responsive table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `github` | string | N/A | Enables the GitHub social icon link using the GitHub URL value set here e.g. `colinwilson` or `colinwilson/lotusdocs` |
| `twitter` | string | N/A | Enables the Twitter / X social icon link using the username value set here e.g. `lotusdocs` |
| `instagram` | string | N/A | Enables the Instagram social icon link using the username value set here e.g. `lotusdocs` |
| `rss` | boolean | `false` | Display an RSS icon link? |
{{</ table >}}

## [params.docs]

Options to help you configure Lotus Docs to suite your needs.

### Core Site Options

{{< table "table table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `title` | string | N/A | Set the default HTML title for your documentation pages/sections e.g. `Lotus Docs` (This parameter is separate from the root Hugo [`title`](https://gohugo.io/getting-started/configuration/#title) parameter that sets the title for your site overall e.g the landing page.) |
| `pathName` | string | `docs` | Pathname for the documentation site. A few additional changes to the Lotus Docs theme are required when this value is updated. See the **Installation** guide for more details. |
| `themeColor` | string | `blue` | Set the sites accent color. This affects links, buttons and icons. Available options/colors include, `blue` (default), `green`, `red`, `yellow`, `emerald`, `cardinal`, `magenta`, `cyan`. |
| `darkMode` | boolean | `false` | Enable Dark Mode? |
| `prism` | boolean | `true` | Enable the PrismJS syntax highlighting plugin? See the [Syntax Highlighting](../../guides/features/syntax-highlighting/#prism-features) and [Prism Shortcode](../../guides/shortcodes/prism/) guides for more details. |
{{</ table >}}

### UI Options

{{< table "table table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `breadcrumbs` | boolean | `true` | Enable breadcrumb navigation links above the content title? |
| `descriptions` | boolean | `true` | Enable front matter descriptions under content title? |
| `backToTop` | boolean | `true` | Enable back-to-top button? |
| `navDesc` | boolean | `true` | Enable front matter descriptions in content Prev/Next navigation card links? |
| `navDescTrunc` | integer | `40` | Number of characters by which to truncate the Prev/Next link front matter descriptions. |
| `listDescTrunc` | integer | `100` | Number of characters by which to truncate card front matter description. |
{{</ table >}}

### Icon Options

{{< table "table table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `sidebarIcons` | boolean | `false` | Enable icons for menu items in the sidebar?. |
| `titleIcon` | boolean | `false` | Prefix content titles with an icon? When enabled and no icon is set in front matter, a the default [Material Symbol icon `article`](https://fonts.google.com/icons?icon.style=Outlined&icon.query=article&icon.platform=web&selected=Material+Symbols+Outlined:article:) is set. |
{{</ table >}}

### GitInfo Options

{{< table "table table-responsive table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `repoURL` | string | N/A | Set the Git repository URL for your site e.g. `https://github.com/colinwilson/lotusdocs.dev` |
| `repoBranch` | string | `main` for GitHub and GitLab. `master` for BitBucket | Set the branch name of your Git repository to use for your site e.g. `main` |
| `editPage` | boolean | `false` | Enable '**Edit this page**' link at the bottom of documentation pages? Links to the Git repository set by the `ghrepo` parameter. |
| `lastMod` | boolean | `false` | Enable '**Last updated**' date at the bottom of documentation pages? |
| `lastModRelative` | boolean | `true` | Format the `lastMod` (if enabled) date parameter as relative? e.g. 8 hours ago, 2 months ago |
{{</ table >}}

### Table of Contents

{{< table "table table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `toc` | boolean | `true` | Enable a Table of Contents for all documentation pages? (Activates only if a documentation page generates a ToC). |
| `tocMobile` | boolean | `true` | Enable a Table of Contents menu in mobile view? Helps navigate pages with a lot of headings/sections. |
| `scrollSpy` | boolean | `true` | Enable [scrollSpy](https://getbootstrap.com/docs/5.3/components/scrollspy/) on the Table of Contents menus? |
{{</ table >}}

## [params.flexsearch]

### FlexSearch Options

See the the [FlexSearch Guide](../../guides/features/flexsearch/) for more information regarding the options below.

{{< table "table table-responsive table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `enabled` | boolean | `true` | Enable FlexSearch? <br><br> **Note:** If `[params.docsearch]` is configured, FlexSearch is automatically disabled regardless of the value set here. |
| `tokenize` | string | `forward` | Set the behaviour for the search process. Options include: `full`, `strict`, `forward`, and `reverse`. |
| `optimize` | boolean | `false` | Enabled to uses a memory-optimized stack flow for the FlexSearch index? |
| `cache` | integer/boolean | `100` | Enable of set cache behaviour. FlexSearch will use the available cache to store popular searches. |
| `minQueryChar` | integer | `0` | Set the minimum number of entered characters required before any search results are rendered. `0` disables this requirement and results are shown as soon as any character is entered. |
| `maxResult` | integer | `5` | Set the maximum number of results presented for a search query. |
| `searchSectionsIndex` | array | `[]` | **TBD**. |
{{</ table >}}

## [params.docsearch]

### DocSearch Options

See the the [DocSearch Guide](../../guides/features/docsearch/) for more information about DocSearch.

{{< table "table table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `appID` | string | N/A | DocSearch / Algolia Application ID. |
| `apiKey` | string | N/A | DocSearch Algolia Search-Only API (Public) Key. |
| `indexName` | string | N/A | Index Name to perform search on. |
{{</ table >}}

## [params.plausible]

### Plausible Analytics Options

See the the [Plausible Analytics Guide](../../guides/features/plausible-analytics/) for more information about how to configure Plausible Analytics for your Lotus Docs site.

{{< table "table table-responsive table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `dataDomain` | string | N/A | Set the domain name that you wish to track via Plausible Analytics, e.g. `lotusdocs.dev`. |
| `scriptURL` | string | `https://plausible.io/js/script.js` | **optional** - Set the URL (domain/subdomain name) where your `script.js` file is self-hosted, e.g. `https://plausible.lotusdocs.dev/js/script.js`. |
| `eventAPI` | string | N/A | **optional** - Set the event API path. e.g. `https://plausible.lotusdocs.dev/api/event` |
{{</ table >}}

## [params.feedback]

### Feedback Widget

See the the [Feedback Widget Guide](../../guides/features/feedback-widget/) for detailed information about how to configure the widget for Plausible and Google Analytics.

{{< table "table table-responsive table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `enabled` | boolean | false | Enable the Feedback Widget? <br><br> **Note:** Either Google or Plausible Analytics need to be configured for the Feedback Widget to function. |
| `emoticonTpl` | boolean | false | **optional** - Enable the emoticon Feedback Widget template? |
| `eventDest` | array | N/A | **optional** - An array to define which configured web analytics services to send feedback events to. Available options currently include, `google` and `plausible`. <br><br> **Note:** If not set, the feedback widget will send feedback events to all web analytics services configured in `hugo.toml`. |
| `successMsg` | string | `Thank you for helping to improve our documentation!` | **optional** - Set the message that's displayed when feedback is successfully submitted. |
| `errorMsg` | string | `Sorry! There was an error while attempting to submit your feedback!` | **optional** - Set the message that's displayed when there is an error in submitting feedback. |
{{</ table >}}

### Emoticon Feedback Template

Parameters specific to the emoticon feedback widget template.

{{< table "table table-responsive table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `emoticonEventName` | string | `Feedback` | **optional** - Set the feedback event name for the emoticon template. |
{{</ table >}}

### Default Feedback Template

Parameters specific to the default feedback template.

{{< table "table table-responsive table-striped" >}}
| Parameter | Type | Default Value | Description |
|---------|-----|-----|------|
| `positiveEventName` | string | `Positive Feedback` | **optional** - Set the name for the positive feedback event. |
| `negativeEventName` | string | `Negative Feedback` | **optional** - Set the name for the negative feedback event. |
| `positiveFormTitle` | string | `What did you like?` | **optional** - Set the title for the positive feedback form. |
| `negativeFormTitle` | string | `What went wrong?` | **optional** - Set the title for the negative feedback form. |
| `positiveForm` | array | N/A | **optional** - A nested array of ratings and descriptions for the positive feedback form. e.g. `[["Easy to understand","Easy to follow and comprehend."]]`, the first element in the nested array represents the rating, and the second, the description. |
| `negativeForm` | array | N/A | **optional** - A nested array of ratings and descriptions for the negative feedback form. e.g. `[["Hard to understand","Too complicated or unclear."]]`, the first element in the nested array represents the rating, and the second, the description. |
{{</ table >}}