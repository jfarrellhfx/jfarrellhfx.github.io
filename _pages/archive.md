---
title: Archive
permalink: /archive/
layout: page
---

## Notes on Physics and Math
<div>
{% assign subjects = site.notes| group_by:"subject" %}
{% for subject in subjects %}
    <h3>{{ subject.name }}</h3>
    <ul>
    {% for item in subject.items %}
    <li> <a href="{{ item.url }}"><div style="font-family: Roboto;font-size:14pt">{{ item.title }}</div></a>
    {{ item.excerpt }}
    </li>

    {% endfor %}
    </ul>
{% endfor %}

</div>

{% for tag in site.tags %}
  <h2>{{ tag[0] }}</h2>
  <ul>
    {% for post in tag[1] %}
    <li> <a href="{{ post.url }}"><div style="font-family: Roboto;font-size:14pt">{{ post.title }}</div></a></li>
    {% endfor %}
  </ul>
{% endfor %}
