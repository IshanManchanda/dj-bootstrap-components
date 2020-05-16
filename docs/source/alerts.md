# Alerts

It is important to reference the bootstrap documentation for how alerts work.
This is how to include alerts in your code

### Examples
Add any one of the  the following in your code, to show an alert

```
    {% include 'bootstrap_components/alert.html' with content='<strong> bold </strong> sample text' color='primary' %}
    {% include 'bootstrap_components/alert.html' with content='sample alert text' color='danger' %}
    {% include 'bootstrap_components/alert.html' with heading='sample heading' content='sample alert text' color='warning' dismiss=1%}
    {% include 'bootstrap_components/alert.html' with heading='sample heading' heading_size=1 content='sample alert text' color='success' dismiss=1%}
```
#### Which look like this: 
![demo](img/alerts.jpg)


### Arguments 

* **Required: content**      
    - the content of the alert. Keep in mind that this string can be html for additional formatting
    - _string_ 
* **Required: color** 
    - accepts bootstrap colors like: primary, success, danger, etc. 
    - _string_ 
* **heading** 
    - creates a `<h4>` heading by default in the alert
    - _string_ 
* **heading_size** 
    - overrides `<h4>` default, allows 1-6
    - _int_ 
* **dismiss** 
    - allows alert to be dismissible, requires bootstrap js
    - _bool (Enter 'True' or 1)_
