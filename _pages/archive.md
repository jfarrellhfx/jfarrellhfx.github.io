---
title: Archive
permalink: /archive/
layout: page
---

{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
    <li> <a href="{{ post.url }}"><div style="font-family: Roboto;font-size:16pt">{{ post.title }}</div></a></li>
    {% endfor %}
  </ul>
{% endfor %}