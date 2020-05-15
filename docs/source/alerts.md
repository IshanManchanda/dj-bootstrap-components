# Alerts

It is important to refrence the bootstrap documentation for how alerts work.
This is how to include alerts in your code

### Examples
Add any one of the  the following in your code, to show an alert

```
    {% include 'alert.html' with content='sample alert text' color='primary' %}
    {% include 'alert.html' with content='sample alert text' color='danger' %}
    {% include 'alert.html' with heading='sample heading' content='sample alert text' color='warning' dismiss=1%}
    {% include 'alert.html' with heading='sample heading' heading_size=1 content='sample alert text' color='success' dismiss=1%}
```
#### Which look like this: 
![demo](img/alerts.jpg)


### Arguments 

* **Argument | Description | Type/Accepted Values |**
* _content_      | the content of the alert                              | string |
* _heading_      | creates a `<h4>` heading by default in the alert      | string | 
* _heading_size_ | overrides `<h4>` default, allows 1-6                  | int | 
* _dismiss_      | allows alert to be dismissable, requires bootstrap js | bool (Enter 'True' or 1)| 
