---
title: "Markdown Crash Test"
icon: bug_report
description: "A crash test markdown example page for basic testing & development (via roneo.org)."
lead: "An example markdown page for testing purposes."
date: 2022-10-19T04:11:15+00:00
lastmod: 2022-10-19T04:12:15+00:00
draft: true
images: []
weight: 10030
toc: true
---

## Benchmark Markdown Support

Benchmarking the support of Markdown with a comprehensive checklist

**Are you working on a project featuring Markdown?**

Drop [the source of this page](https://raw.githubusercontent.com/RoneoOrg/markdown/main/README.md) wherever you want to test *or showcase* the support of Markdown, and check that every single feature is properly rendered.


**Table of Contents**

- [Basic formatting](#basic-formatting)
- [Blockquotes](#blockquotes)
- [Lists](#lists)
- [Linebreaks](#linebreaks)
- [Links](#links)
- [Code formatting](#code-formatting)
- [Images](#images)
- [Task lists](#task-lists)
- [Tables](#tables)
- [Footnotes](#footnotes)
- [Definition List](#definition-list)
- [Headings](#headings)


## Basic formatting

### **Bold** text

**Syntax:**

    You can mark some text as bold with **two asterisks**
    or __two underscores__.

**Output:**

You can mark some text as bold with **two asterisks**
or __two underscores__.

### *Italic*

    Use a *single asterisk* or a _single underscore_ for italic.

**Output:**

Use a *single asterisk* or a _single underscore_ for italic.

### ***Bold and italic***

    Three stars gives `***bold and italic***`

Three stars gives ***bold and italic***

### ~~Strikethrough~~

Using `~~two tildes~~` will strikethrough:  ~~two tildes~~



## Blockquotes

**Syntax:**

    > blockquote

**Output**:

> blockquote

### Nested blockquotes

**Syntax:**

    > First level
    >
    >> Second level

**Output:**

> First level
>> Second level

### Markdown in blockquotes

```
> **Markdown** can be used *inside quotes*
>
> 1.   This is the first list item.
> 1.   This is the second list item.
>
> ~~strikethrough~~
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");
```

**Output:**

> **Markdown** can be used *inside quotes*
> 1. This is the first list item.
> 1. This is the second list item.
>
> ~~strikethrough~~
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");


## Lists


### Unordered list

Cant be marked with `-`, `+` or `*`

```markdown
- First item
- Second item
- Third item
```

```markdown
+ First item
+ Second item
+ Third item
```

```markdown
* First item
* Second item
* Third item
```

**Output:**

- First item
- Second item
- Third item

+ First item
+ Second item
+ Third item

* First item
* Second item
* Third item

### Ordered lists

Incrementation is automatic, you can simply use `1.` everywhere

```
1. First item
1. Second item
1. Third item
```

**Output:**

1. First item
1. Second item
1. Third item



### Nested list

**Unordered**

```
- First item
- Second item
- Third item
  - Indented item
  - Indented item
- Fourth item
```

**Output:**

- First item
- Second item
- Third item
  - Indented item
  - Indented item
- Fourth item

**Ordered**

```
1. First item
1. Second item
1. Third item
    1. Indented item
    1. Indented item
1. Fourth item
1. Fifth item
    1. Indented item
    1. Indented item
        1. Indented item
```

**Output:**

1. First item
1. Second item
1. Third item
    1. Indented item
    1. Indented item
1. Fourth item
1. Fifth item
    1. Indented item
    1. Indented item
        1. Indented item

**Mixed**

```
1. First item
1. Second item
1. Third item
    * Indented item
    * Indented item
1. Fourth item
1. Fifth item
    1. Indented item
    1. Indented item
        1. Indented item
        1. Indented item
            * Indented
                1. Indented item
                    * Indented
                1. Indented item
            * Indented
        1. Indented item
1. Sixth item
```

**Output:**

1. First item
1. Second item
1. Third item
    * Indented item
    * Indented item
1. Fourth item
1. Fifth item
    1. Indented item
    1. Indented item
        1. Indented item
        1. Indented item
            * Indented
                1. Indented item
                    * Indented
                1. Indented item
            * Indented
        1. Indented item
1. Sixth item


## Linebreaks

**When you hit enter just once** between two lines, both lines are joined into a single paragraph.

But, if you **leave a blank line between them**, they will split into two paragraphs.

**Demonstration**:

```
This text is a paragraph.
This won't be another paragraph, it will join the line above it.

This will be another paragraph, as it has a blank line above it.
```

**Output:**

This text is a paragraph. This won't be another paragraph, it will join the line above it.

This will be another paragraph, as it has a blank line above it.

### Force line breaks

To force a line break, **end a line with two or more whitespaces**, and then type return.

```
This is the first line.··
Second line
```

**Output:**

This is the first line.
Second line

### Horizontal lines

Can be inserted with four `*`, `-` or `_`

```
----

****

____
```

**Output:**

----

****

____




## Links


### Basic links

```
[Semantic description](https://roneo.org/markdown)
<address@example.com>
<https://roneo.org/markdown> works too. Must be used for explicit links.
```

**Output:**

[Semantic description](https://roneo.org/markdown)
<address@example.com>
<https://roneo.org/markdown> works too. Must be used for explicit links.


### Links using text reference

```
[I'm a link][Reference text]

[This link] will do the same as well. It works as the identifier itself.


[reference text]: https://jamstack.club
[this link]: https://roneo.org/markdown
```

**Output:**

[I'm a link][Reference text]

[This link] will do the same as well. It works as the identifier itself.


[reference text]: https://jamstack.club
[this link]: https://roneo.org/markdown

**Note:** The reference text is *not* case sensitive


### Link with a title on hover

```
[Random text][random-identifier].
Hover the mouse over it to see the title.

Several syntaxes are accepted:
[One](https://eff.org "First site")
[Two](https://example.com 'Second site')
[Three](https://example.com (Third site))

[random-identifier]: https://roneo.org/markdown "This example has a title"
```

**Output:**

[Random text][random-identifier]. Hover the mouse over it to see the title.

Several syntaxes are accepted:
[One](https://eff.org "First site")
[Two](https://jamstack.club 'Second site')
[Three](https://debian.org (Third site))

[random-identifier]: https://roneo.org/markdown "This example has a title"


### Links with Markdown style

To ***emphasize*** links, add asterisks before and after the brackets and parentheses.

    I love supporting the **[EFF](https://eff.org)**.
    This is the *[Markdown Guide](https://www.markdownguide.org)*.

To denote links as `code`, add backticks *inside* the brackets:

    See the section on [`code`](#code).

**Output:**

I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](#code).


### Attribute a custom anchor to a heading

Anchors are automatically generated based on the heading's content. You can customize the anchor this way:

    ### Heading {#custom-id}

**Output:**

#### Heading {#custom-id}



## Code formatting


### Inline

Wrap with single backticks to highlight as`` `code` `` → `code`

### Codeblocks

Create a code block with three backticks `` ``` `` before and after your block of code.

**Output:**


```
sudo apt hello
cat /etc/apt/sources.list
```

Also possible with a tabulation or four empty spaces at the beginning of the lines:

**Tabulation**

	sudo apt hello
	echo "hi"

**Four whitespaces**

    sudo apt hello

Let's test the wrapping of a long line:

	apt install test apt install test apt install test apt install test apt install test apt install test apt install test apt install test apt install test apt install test apt install test apt install test apt install test apt install test

### Codeblocks with syntax highlighting

Set the language right after the first backticks (for example `` ```html  ``) to get syntax highlighting

#### Samples:


#### HTML

```html
<!DOCTYPE html>
<html lang="fr" itemscope itemtype="http://schema.org/WebPage">
  <head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
```

#### CSS

```css
/* Comment */
.blog-post h2, h3 {
  margin-top: 1.6em;
  margin-bottom: 0.8em;
}
```

#### Bash

```bash
# Comment

if [[ ! $system =~ Linux|MacOS|BSD ]]; then
	echo "This version of bashtop does not support $system platform."

sudo apt install test
```

#### Diff

```diff
- delete
+ add
! test
# comment
```

### Escaping with backslashes

Any ASCII punctuation character may be escaped using a single backslash.

Example:

    \*this is not italic*

**Output:**

\*this is not italic*

Markdown provides backslash escapes for the following characters:

    \   backslash
    `   backtick
    *   asterisk
    _   underscore
    {}  curly braces
    []  square brackets
    ()  parentheses
    #   hash mark
	+	plus sign
	-	minus sign (hyphen)
    .   dot
    !   exclamation mark


## Images

### Basic syntax

``` markdown
  ![Semantic description of the image](https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp)
```

![Semantic description of the image](https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp)

**Note: The text inside the square brackets is important!**

Screen reader users get informations about the image with this attribute called `ALT`, for _alternative text_.

Including **descriptive** alt text [helps maintain accessibility](https://webaim.org/techniques/alttext/) for every visitor and should always be included with an image. When you add alt text be sure to describe the content and function of the picture.
In addition to the accessibility benefits, `ALT` is useful for SEO. It's also displayed when, for some reason, the picture is not loaded by the browser.


### Image with title and caption

```
![Semantic description](https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp "Your title")*Your caption*
```

![Semantic description](https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp "Your title")*Your caption*


### Clickable images

For clickable images, simply wrap the image markup into a [link markup](#links):

```
[![Semantic description](https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp "Your title")](http://jamstack.club)
```

**Output:**

[![Semantic description](https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp "Your title")](http://jamstack.club)



### Image with an identifier

You can call the image with an identifier as we do for [links](#links)

```
![Semantic desc.][image identifier]

Lorem ipsum dolor sit amet consectetur adipisicing elit [...]

[image identifier]: https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp "Title"
```

![Semantic desc.][image identifier]

[image identifier]: https://res.cloudinary.com/qunux/image/upload/c_scale,w_200/v1666153179/Lotus%20Labs%20Assets/Logos/LotusLabs_Logo_v7.4.webp "Title"


## Task lists

```
- [X] Write the press release
- [ ] Update the website
```

**Output:**

- [x] Write the press release
- [ ] Update the website



## Tables


```
| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |
```

or

```
| Syntax | Description |
| - | --- |
| Header | Title |
| Paragraph | Text|
```

will render the same way:

| Syntax | Description |
| - | --- |
| Header | Title |
| Paragraph | Text|


### Text alignment in tables


```
| Syntax    | Description |   Test Text |
| :-------- | :---------: | ----------: |
| Header    |    Title    | Here's this |
| Paragraph |    Text     |    And more |
```

See the way the text is aligned, depending on the position of `':'`

| Syntax    | Description |   Test Text |
| :-------- | :---------: | ----------: |
| Header    |    Title    | Here's this |
| Paragraph |    Text     |    And more |



## Footnotes

```
Here's a sentence with a footnote[^1].
(see the result at the bottom of the page)

[^1]: This is the first footnote.
```

**Output:**

Here's a sentence with a footnote[^1].
(see the result at the bottom of the page)

[^1]: This is the first footnote.

### Long footnote

```
Here's a longer one.[^bignote]
(see the result at the bottom of the page)

[^bignote]: Here's one with multiple paragraphs and code.

	Indent paragraphs to include them in the footnote.

	`{ my code }`

	Note that you can place the footnote anywhere you want in your article
```

**Output:**

Here's a longer one.[^bignote]
(see the result at the bottom of the page)

[^bignote]: Here's one with multiple paragraphs and code.

	Indent paragraphs to include them in the footnote.

	`{ my code }`

	Note that you can place the footnote anywhere you want in your article



## Definition List


```
term
: definition

second term
: meaning

complex term
: long definition including **bold text**. Velit tempor cillum aute culpa pariatur enim laboris consectetur tempor. Aute elit non do ipsum. Nisi quis culpa magna esse ipsum. Ad aliquip ullamco minim cillum in ullamco.
```

**Output:**

term
: definition

second term
: meaning

complex term
: long definition including **bold text**. Velit tempor cillum aute culpa pariatur enim laboris consectetur tempor. Aute elit non do ipsum. Nisi quis culpa magna esse ipsum. Ad aliquip ullamco minim cillum in ullamco.


## Headings

Add `##` at the beginning of a line to set as Heading.
You can use up to 6 `#` symbols for the corresponding Heading levels


```
## Heading 1
[...]

###### Heading 6
```


## Heading 2

pedit quia voluptates atque nobis, perspiciatis deserunt perferendis, nostrum, voluptatem voluptas dolorem iure voluptatum? Accusantium a dolores dicta?Pariatur voluptates quam ut, cum aliquid eum, officiis laudantium totam suscipit, ducimus odit nobis! Corrupti, doloremque sed optio voluptatibus deserunt quas repellat eius minus quasi, ipsam unde esse sequi deleniti.


### Heading 3 ##################################

pedit quia voluptates atque nobis, perspiciatis deserunt perferendis, nostrum, voluptatem voluptas dolorem iure voluptatum? Accusantium a dolores dicta?Pariatur voluptates quam ut, cum aliquid eum, officiis laudantium totam suscipit, ducimus odit nobis! Corrupti, doloremque sed optio voluptatibus deserunt quas repellat eius minus quasi, ipsam unde esse sequi deleniti.

#### Heading 4

pedit quia voluptates atque nobis, perspiciatis deserunt perferendis, nostrum, voluptatem voluptas dolorem iure voluptatum? Accusantium a dolores dicta?Pariatur voluptates quam ut, cum aliquid eum, officiis laudantium totam suscipit, ducimus odit nobis! Corrupti, doloremque sed optio voluptatibus deserunt quas repellat eius minus quasi, ipsam unde esse sequi deleniti.

##### Heading 5

pedit quia voluptates atque nobis, perspiciatis deserunt perferendis, nostrum, voluptatem voluptas dolorem iure voluptatum? Accusantium a dolores dicta?Pariatur voluptates quam ut, cum aliquid eum, officiis laudantium totam suscipit, ducimus odit nobis! Corrupti, doloremque sed optio voluptatibus deserunt quas repellat eius minus quasi, ipsam unde esse sequi deleniti.

###### Heading 6

pedit quia voluptates atque nobis, perspiciatis deserunt perferendis, nostrum, voluptatem voluptas dolorem iure voluptatum? Accusantium a dolores dicta?Pariatur voluptates quam ut, cum aliquid eum, officiis laudantium totam suscipit, ducimus odit nobis! Corrupti, doloremque sed optio voluptatibus deserunt quas repellat eius minus quasi, ipsam unde esse sequi deleniti.


## References

- Source of this page: [github.com/RoneoOrg/markdown](https://github.com/RoneoOrg/markdown)
- [Markdown Guide - Basic Syntax](https://www.markdownguide.org/basic-syntax)
- [Markdown Guide - Extended Syntax](https://www.markdownguide.org/extended-syntax)
- [Daring Fireball: Markdown Syntax Documentation](https://daringfireball.net/projects/markdown/syntax)
- [Markdown Guide at Gitlab.com](https://about.gitlab.com/handbook/markdown-guide/)
- [CommonMark Spec](https://spec.commonmark.org/0.29/)

## Related projects

- https://github.com/ericwbailey/markdown-test-file
- https://scottspence.com/posts/writing-with-markdown
- https://codingnconcepts.com/markdown/markdown-syntax/
- https://codeit.suntprogramator.dev/basic-markdown-syntax/
- https://daringfireball.net/projects/markdown/syntax.text