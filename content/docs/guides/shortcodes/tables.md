---
weight: 555
title: "Tables"
icon: table_chart
description: "How to use the Lotus Docs table shortcode to render great looking markdown tables"
lead: "Use the Lotus docs table shortcode to render various table styles."
date: 2022-11-05T04:41:15+00:00
lastmod: 2022-11-05T04:41:15+00:00
draft: false
images: []
toc: true
---

The `table` shortcode enables Lotus Docs to take advantage of [Bootstrap's opt-in table styling](https://getbootstrap.com/docs/5.2/content/tables).
## Regular Tables

By default Lotus Docs renders regular Markdown tables with some very basic styling:

```
| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |
```

Result:

| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |

## Shortcode Tables

The the table shortcode allows you to implement a number of Bootstrap's table styling classes. The `table` shortcode without any options will render a basic bordered table with a borderless floating table head:

```go
{{</* table >}}
| Animal | Sounds | Legs |
|---------|--------|-----|
| `Cat` | Meow | 4 |
| `Dog` | Woof | 4 |
| `Cricket` | Chirp | 6 |
{{< /table */>}}
```

{{< table >}}
| Animal | Sounds | Legs |
|---------|--------|-----|
| `Cat` | Meow | 4 |
| `Dog` | Woof | 4 |
| `Cricket` | Chirp | 6 |
{{< /table >}}

{{% alert context="warning" %}}
Since the `table` shortcode works by implementing [Bootstrap's opt-in table styling](https://getbootstrap.com/docs/5.2/content/tables), not all Bootstrap's table styles are compatible with Lotus Docs. All compatible options are documented on this page.
{{% /alert %}}

### Striped Rows

Use the `table-striped` option to add zebra-striping to the table rows.

```go
{{</* table "table-striped" >}}
...
..
{{< /table */>}}
```

{{< table "table-striped" >}}
| Parameter | Default Value | Description |
|---------|--------|------|
| `google_fonts` | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Poppins", "300, 400, 600, 700"],["Source Code Pro", "500, 700"]]`<br> This will load the Google [Poppins](https://fonts.google.com/specimen/Poppins) and [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) fonts in the specified sizes. |
| `sans_serif_font` | System Font | Set the Sans Serif font. e.g. `"Poppins"` |
| `secondary_font` | System Font | Set the Secondary font. e.g. `"Poppins"` |
{{< /table >}}

### Striped Columns

Use the `table-striped-columns` option to add zebra-striping to the table columns.

```go
{{</* table "table-striped-columns" >}}
...
..
{{< /table */>}}
```

{{< table "table-striped-columns" >}}
| Parameter | Default Value | Description |
|---------|--------|------|
| `google_fonts` | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Poppins", "300, 400, 600, 700"],["Source Code Pro", "500, 700"]]`<br> This will load the Google [Poppins](https://fonts.google.com/specimen/Poppins) and [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) fonts in the specified sizes. |
| `sans_serif_font` | System Font | Set the Sans Serif font. e.g. `"Poppins"` |
| `secondary_font` | System Font | Set the Secondary font. e.g. `"Poppins"` |
{{< /table >}}

### Hoverable Rows

Use the `table-hover` option to enable a hover state on the table rows.

```go
{{</* table "table-hover" >}}
...
..
{{< /table */>}}
```

{{< table "table-hover" >}}
| Parameter | Default Value | Description |
|---------|--------|------|
| `google_fonts` | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Poppins", "300, 400, 600, 700"],["Source Code Pro", "500, 700"]]`<br> This will load the Google [Poppins](https://fonts.google.com/specimen/Poppins) and [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) fonts in the specified sizes. |
| `sans_serif_font` | System Font | Set the Sans Serif font. e.g. `"Poppins"` |
| `secondary_font` | System Font | Set the Secondary font. e.g. `"Poppins"` |
{{< /table >}}

### Tables without borders

Use the `table-borderless` option a table without borders.

```go
{{</* table "table-borderless" >}}
...
..
{{< /table */>}}
```

{{< table "table-borderless" >}}
| Parameter | Default Value | Description |
|---------|--------|------|
| `google_fonts` | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Poppins", "300, 400, 600, 700"],["Source Code Pro", "500, 700"]]`<br> This will load the Google [Poppins](https://fonts.google.com/specimen/Poppins) and [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) fonts in the specified sizes. |
| `sans_serif_font` | System Font | Set the Sans Serif font. e.g. `"Poppins"` |
| `secondary_font` | System Font | Set the Secondary font. e.g. `"Poppins"` |
{{< /table >}}


### Small Tables

Add `table-sm` or `table-xs` to make any table more compact by reducing the cell padding.

{{< table "table-sm" >}}
| Parameter | Default Value | Description |
|---------|--------|------|
| `google_fonts` | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Poppins", "300, 400, 600, 700"],["Source Code Pro", "500, 700"]]`<br> This will load the Google [Poppins](https://fonts.google.com/specimen/Poppins) and [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) fonts in the specified sizes. |
| `sans_serif_font` | System Font | Set the Sans Serif font. e.g. `"Poppins"` |
| `secondary_font` | System Font | Set the Secondary font. e.g. `"Poppins"` |
{{< /table >}}

{{< table "table-xs" >}}
| Parameter | Default Value | Description |
|---------|--------|------|
| `google_fonts` | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Poppins", "300, 400, 600, 700"],["Source Code Pro", "500, 700"]]`<br> This will load the Google [Poppins](https://fonts.google.com/specimen/Poppins) and [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) fonts in the specified sizes. |
| `sans_serif_font` | System Font | Set the Sans Serif font. e.g. `"Poppins"` |
| `secondary_font` | System Font | Set the Secondary font. e.g. `"Poppins"` |
{{< /table >}}

### Responsive Tables

Add the `table-responsive` option to make a table responsive:

{{< table "table-responsive" >}}
| Animal | Sounds | Legs |
|---------|--------|-----|
| `Cat` | Meow | 4 |
| `Dog` | Woof | 4 |
| `Cricket` | Chirp | 6 |
{{< /table >}}

### Combining Table Options

Combine `table` shortcode options to create your desired effect:

```go
{{</* table "table-striped table-sm table-borderless" >}}
...
..
{{< /table */>}}
```

{{< table "table-striped table-sm table-borderless" >}}
| Parameter | Default Value | Description |
|---------|--------|------|
| `google_fonts` | N/A | An array of Google fonts and sizes to load. e.g.<br>`google_fonts = [["Poppins", "300, 400, 600, 700"],["Source Code Pro", "500, 700"]]`<br> This will load the Google [Poppins](https://fonts.google.com/specimen/Poppins) and [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) fonts in the specified sizes. |
| `sans_serif_font` | System Font | Set the Sans Serif font. e.g. `"Poppins"` |
| `secondary_font` | System Font | Set the Secondary font. e.g. `"Poppins"` |
{{< /table >}}