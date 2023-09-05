---
weight: 10030
title: "Code Blocks"
icon: change_history
description: "Code Block features and settings."
date: 2022-11-27T07:08:15+00:00
lastmod: 2022-11-27T07:08:15+00:00
draft: true
images: []
toc: true
---

## Syntax Highlighting

Syntax highlighting is supported by [Prism](https://prismjs.com/index.html) (the default). It can be disabled in favour of Hugo's builtin syntax highlighter, [Chroma](https://github.com/alecthomas/chroma).

🡇 code fences - `bash`
```bash
curl -X POST -is "http://localhost:4242/create-checkout-session" -d ""
```

🡇 code fences - `javascript`
```javascript {linenos=inline,linenostart=19,hl_lines=[1,"4-5"],anchorlinenos=true}
function foo(bar) {
    var a = 42,
        b = 'Prism';
    return a + bar(b);
}
```

🡇 prism shortcode - `javascript`
{{< prism lang="javascript" linkable-line-numbers="true" line-numbers="true" start="19" line-offset="19" line="19,22-23" >}}
function foo(bar) {
    var a = 42,
        b = 'Prism';
    return a + bar(b);
}
{{< /prism >}}

🡇 code fences - `html`
```html
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```
🡇 code fences - `swift`
```swift
let cardParams = STPCardParams()
cardParams.name = "Jenny Rosen"
cardParams.number = "4242424242424242"
cardParams.expMonth = 12
cardParams.expYear = 18
cardParams.cvc = "424"

let sourceParams = STPSourceParams.cardParams(withCard: cardParams)
STPAPIClient.shared.createSource(with: sourceParams) { (source, error) in
    if let s = source, s.flow == .none && s.status == .chargeable {
        self.createBackendChargeWithSourceID(s.stripeID)
    }
}
```
🡇 prism shortcode - `go`
{{< prism lang="go" start="46" line="6-13,15-25,27-44,45,46,48-52" >}}
package main

import (
  "net/http"

  "github.com/labstack/echo"
  "github.com/labstack/echo/middleware"
  "github.com/stripe/stripe-go/v72"
  "github.com/stripe/stripe-go/v72/checkout/session"
)

// This example sets up an endpoint using the Echo framework.
// Watch this video to get started: https://youtu.be/ePmEVBu8w6Y.

func main() {
  stripe.Key = "UfXXWzQ2B1yVX57GU3QV8EQyTizMUvUm"

  e := echo.New()
  e.Use(middleware.Logger())
  e.Use(middleware.Recover())

  e.POST("/create-checkout-session", createCheckoutSession)

  e.Logger.Fatal(e.Start("localhost:4242"))
}

func createCheckoutSession(c echo.Context) (err error) {
  params := &stripe.CheckoutSessionParams{
    Mode: stripe.String(string(stripe.CheckoutSessionModePayment)),
    LineItems: []*stripe.CheckoutSessionLineItemParams{
      &stripe.CheckoutSessionLineItemParams{
        PriceData: &stripe.CheckoutSessionLineItemPriceDataParams{
          Currency: stripe.String("usd"),
          ProductData: &stripe.CheckoutSessionLineItemPriceDataProductDataParams{
            Name: stripe.String("T-shirt"),
          },
          UnitAmount: stripe.Int64(2000),
        },
        Quantity: stripe.Int64(1),
      },
    },
    SuccessURL: stripe.String("http://localhost:4242/success"),
    CancelURL:  stripe.String("http://localhost:4242/cancel"),
  }

  s, _ := session.New(params)

  if err != nil {
    return err
  }

  return c.Redirect(http.StatusSeeOther, s.URL)
}
{{< /prism >}}

🡇 code fences - `treeview`
```treeview
├── fonts/
├── images/
├── js/
│   ├── vendor/
│   ├── app.js
│   └── index.js
├── lambda/
└── scss/
    ├── common/
    ├── components/
    ├── layouts/
    ├── vendor/
    └── app.scss
```