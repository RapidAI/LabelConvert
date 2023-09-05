---
weight: 518
title: "Feedback Widget"
description: "How to configure the Feedback Widget so visitors can rate or/and comment on your site's content."
icon: reviews
date: 2023-08-08T23:33:15+00:00
lastmod: 2023-08-24T02:43:15+00:00
draft: false
images: []
---

The Lotus Docs feedback plugin integrates with Google or Plausible Analytics to allow you to collect visitor feedback on your sites' content.

![Lotus Docs Emoticon Feedback Widget Screenshot](https://res.cloudinary.com/lotuslabs/image/upload/v1692841008/Lotus%20Docs/images/lotusdocs_emoticon_feedback_widget_screenshot_rd_v2_mmoxca.webp)

## Why use web analytics to collect feedback?

Short answer? Because it's **FREE**! Other benefits include:

- No need to sign up to yet another service just to collect basic visitor feedback.
- Easy to configure. Once Google or Plausible Analytics (or both) are configured in `hugo.toml`, the Feedback Widget it ready to go.
- [No limit](https://support.google.com/analytics/answer/9267744) on the number of events that can be collected.


## How it works

Once enabled, the feedback widget appears at bottom of every content page. Whenever a site visitor interacts with it, their feedback is collected and sent to whichever web analytics you have configured in your `hugo.toml` file.

### Custom Events

The Feedback Widget works by leveraging custom events. What is a custom event?

> A custom event is an event that you define so you can collect information about an interaction that's important to your business.[^1]

Check out the links below for more information on how custom events work:

- **Google Analytics v4** - [Custom events](https://support.google.com/analytics/answer/12229021)
- **Plausible Analytics** - [Custom event goals](https://plausible.io/docs/custom-event-goals)

The feedback form uses these custom events to send visitor interactions to the corresponding analytics service.

### Templates

Lotus Docs currently offers two template styles for the feedback widget:

#### Emoticon

<div class="d-flex justify-content-center pb-4">
    <video width="90%" controls>
    <source src="https://res.cloudinary.com/lotuslabs/video/upload/v1692663574/Lotus%20Docs/video/lotusdocs_emoticon_feedback_template_sjk1rm.webm" type="video/webm">
    <source src="https://res.cloudinary.com/lotuslabs/video/upload/v1692663574/Lotus%20Docs/video/lotusdocs_emoticon_feedback_template_sjk1rm.mp4" type="video/mp4">
    </video>
</div>

#### Default (Classic)

<div class="d-flex justify-content-center pb-4">
    <video width="90%" controls>
    <source src="https://res.cloudinary.com/lotuslabs/video/upload/v1692664585/Lotus%20Docs/video/lotusdocs_default_feedback_template_ybut2q.webm" type="video/webm">
    <source src="https://res.cloudinary.com/lotuslabs/video/upload/v1692664585/Lotus%20Docs/video/lotusdocs_default_feedback_template_ybut2q.wmp4" type="video/mp4">
    </video>
</div>

## Configure Custom Events

Your web analytics service may require some preparation prior to receiving custom events from the feedback widget.

### Plausible

Custom events aren't automatically displayed in the Plausible dashboard. You'll have to configure the custom event goal for you feedback to show up.

To configure a goal, go to [your website's settings](https://plausible.io/docs/website-settings) in your Plausible account and visit the "Goals" section. You should see an empty list with a prompt to add a goal.

![Add Goal in Plausible](https://res.cloudinary.com/lotuslabs/image/upload/v1692654403/Lotus%20Docs/images/plausible_goals_setup_1_mod_bglw1y.webp)

Click on the "**+ Add goal**" button to go to the goal creation form.

Select `Custom event` as the goal trigger and enter the name of the custom event you are triggering e.g. `Feedback`, the default name of the emoticon template feedback event. The name must match the value you set for `[params.feedback.emoticonEventName]` in your `hugo.toml` config.

![Add Goal to Plausible Account](https://res.cloudinary.com/lotuslabs/image/upload/v1692655733/Lotus%20Docs/images/plausible_goals_setup_2_mod_uut38r.webp)

Head back to the stats page for your site and scroll to the bottom to view the `Goal Conversion` statistics. You'll see the Feedback goal along with the breakdown by `rating`. Next to it is a `message` link, which shows a breakdown of any messages received via the widget's text area.

![Lotus Docs Feedback Goal Conversion statistics](https://res.cloudinary.com/lotuslabs/image/upload/v1692656039/Lotus%20Docs/images/plausible_feedback_goal_conversions_mod_kcin8h.webp)

### Google

Once Google Analytics and the feedback widget are configured in your `hugo.toml` file, no additional configuration is required to view collected events in the Google Analytics dashboard. However, there are a couple of tasks that will help you better view and understand your feedback stats in Google Analytics:

- **See the events in your reports** - After you configure the feedback widget and Google Analytics collects the feedback event, you can use the [Events](https://support.google.com/analytics/answer/12926615) report in the Reports section to see how many times feedback was collected and other data (`ratings`, `messages`) about the event in the specified date range.

    You can also select the feedback event name to open a more detailed report, including details about the ratings and messages, and how many users triggered the event (and the associated parameters) in realtime.

- **Custom dimensions and metrics** - To access the different values assigned to the `ratings` and `message` event parameters in your reports, you should create a custom dimension or metric. A custom dimension or metric lets you see the information you collected from `ratings` and `message` parameters. For example, with the `rating` event parameter, you could create a custom metric called 'Rating' that allows you to see each value assigned to the event parameter. [Learn more about custom dimensions and metrics](https://support.google.com/analytics/answer/10075209).

## How to configure the Feedback Widget

The Feedback Widget is configured via the `[params.feedback]` parameter:

{{< tabs tabTotal="3">}}
   {{% tab tabName="hugo.toml" %}}

   ```toml
    [params.feedback]
        enabled = true                                                                   # default / not set = false
        emoticonTpl = true                                                               # optional
        eventDest = ["plausible","google"]                                               # optional
        emoticonEventName = "Feedback"                                                   # optional
        positiveEventName = "Positive Feedback"                                          # optional
        negativeEventName = "Negative Feedback"                                          # optional
        positiveFormTitle = "What did you like?"                                         # optional
        negativeFormTitle = "What went wrong?"                                           # optional
        successMsg = "Thank you for helping to improve our documentation!"               # optional
        errorMsg = "Sorry! There was an error while attempting to submit your feedback!" # optional
        positiveForm = [
          ["Accurate", "Accurately describes the feature or option."],
          ["Solved my problem", "Helped me resolve an issue."],
          ["Easy to understand", "Easy to follow and comprehend."],
          ["Something else"]
        ]
        negativeForm = [
          ["Inaccurate", "Doesn't accurately describe the feature or option."],
          ["Couldn't find what I was looking for", "Missing important information."],
          ["Hard to understand", "Too complicated or unclear."],
          ["Code sample errors", "One or more code samples are incorrect."],
          ["Something else"]
        ]
   ```

   {{% /tab %}}
   {{% tab tabName="hugo.yaml" %}}

   ```yaml
    params:
        feedback:
            enabled: true                                                                 # default / not set = false
            emoticonTpl: true                                                             # optional
            eventDest:                                                                    # optional
                - plausible
                - google
            emoticonEventName: Feedback                                                   # optional
            positiveEventName: Positive Feedback                                          # optional
            negativeEventName: Negative Feedback                                          # optional
            positiveFormTitle: What did you like?                                         # optional
            negativeFormTitle: What went wrong?                                           # optional
            successMsg: Thank you for helping to improve our documentation!               # optional
            errorMsg: Sorry! There was an error while attempting to submit your feedback! # optional
            positiveForm:
                - - Accurate
                  - Accurately describes the feature or option.
                - - Solved my problem
                  - Helped me resolve an issue.
                - - Easy to understand
                  - Easy to follow and comprehend.
                - - Something else
            negativeForm:
                - - Inaccurate
                  - Doesn't accurately describe the feature or option.
                - - Couldn't find what I was looking for
                  - Missing important information.
                - - Hard to understand
                  - Too complicated or unclear.
                - - Code sample errors
                  - One or more code samples are incorrect.
                - - Something else
   ```

   {{% /tab %}}
   {{% tab tabName="hugo.json" %}}

   ```json
    {
        "params": {
            "feedback": {
                "enabled": true,
                "emoticonTpl": true,
                "eventDest": [
                    "plausible",
                    "google"
                ],
                "emoticonEventName": "Feedback",
                "positiveEventName": "Positive Feedback",
                "negativeEventName": "Negative Feedback",
                "positiveFormTitle": "What did you like?",
                "negativeFormTitle": "What went wrong?",
                "successMsg": "Thank you for helping to improve our documentation!",
                "errorMsg": "Sorry! There was an error while attempting to submit your feedback!",
                "positiveForm": [
                    [
                        "Accurate",
                        "Accurately describes the feature or option."
                    ],
                    [
                        "Solved my problem",
                        "Helped me resolve an issue."
                    ],
                    [
                        "Easy to understand",
                        "Easy to follow and comprehend."
                    ],
                    [
                        "Something else"
                    ]
                ],
                "negativeForm": [
                    [
                        "Inaccurate",
                        "Doesn't accurately describe the feature or option."
                    ],
                    [
                        "Couldn't find what I was looking for",
                        "Missing important information."
                    ],
                    [
                        "Hard to understand",
                        "Too complicated or unclear."
                    ],
                    [
                        "Code sample errors",
                        "One or more code samples are incorrect."
                    ],
                    [
                        "Something else"
                    ]
                ]
            }
        }
    }
   ```

    {{% /tab %}}
{{< /tabs >}}

## Configuration Options

The following options are available for the Feedback Widget:

### Template

Choose which feedback template is displayed on your site:

- **`emoticonTpl`** - Set to `true` to enable the emoticon feedback template. (**default**) is `false`.

### Event Destination

This determines which of your configured web analytics services to send your collected feedback to:

{{% alert context="warning" %}}
If this parameter is not set, feedback will be sent to all web analytics configured in `hugo.toml`
{{% /alert %}}

- **`eventDest`** - A list of web analytics services to send visitor feedback to e.g. `["plausible", "google"]` (**default**)

### Event Name

Set the name of the feedback event that's sent to the web analytics service:

- **`emoticonEventName`** - The name of the event for the emoticon feedback template e.g. `Feedback` (**default**)

- **`positiveEventName`** - The name of the positive event for the default feedback template e.g. `Positive Feedback` (**default**)

- **`negativeEventName`** - The name of the negative event for the default feedback template e.g. `Negative Feedback` (**default**)

{{% alert context="info" text="**Note** - For **Google Analytics v4** (per [Google's recommendations](https://support.google.com/analytics/answer/13316687)), before an event is sent, Lotus Docs converts the event name to lowercase letters, and replaces spaces with an underscore. e.g. `Positive Feedback` is converted to `positive_feedback`." /%}}

### Form Title

This option sets the title for each form in the **default feedback template**:

- **`positiveFormTitle`** - The title of the positive feedback form e.g. `What did you like?` (**default**)

- **`negativeFormTitle`** - The title of the negative feedback form e.g. `What went wrong?` (**default**)

### Success / Error Messages

Messages displayed after feedback is submitted (applies to both templates):

- **`successMsg`** - The message displayed after feedback has been successfully sent e.g. `Thank you for helping to improve our documentation!` (**default**)

- **`errorMsg`** - The message displayed if the widget fails to submit feedback e.g. `Sorry! There was an error while attempting to submit your feedback!` (**default**)

### Ratings & Description Configuration

A nested array of options for each form in the **default feedback template**. The first string in each nested array sets the name of the feedback rating. The second string sets a description for that feedback rating.

- **`positiveForm`** - A nested array consisting of a positive rating name and description (optional) for each feedback radio option e.g. `[["Accurate", "Accurately describes the feature or option."]]`.

- **`negativeForm`** - A nested array consisting of a negative rating name and description (optional) for each feedback radio option e.g. `[["Code sample errors", "One or more code samples are incorrect."]]`.

So `["Solved my problem", "Helped me resolve an issue."]` results in:

![Feedback Form Option](https://res.cloudinary.com/lotuslabs/image/upload/v1692328347/Lotus%20Docs/images/lotusdocs_feedback_form_option_selected_ppf1hb.webp)

The feedback rating `Solved my problem` is sent as an [event parameter](https://developers.google.com/analytics/devguides/collection/ga4/event-parameters?client_type=gtag) value of a key named `rating`, and any text entered in the text area, is sent as a value of a key named `message`.

[^1]: [[GA4] Custom events - Analytics Help](https://support.google.com/analytics/answer/12229021)