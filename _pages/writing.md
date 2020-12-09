---
title: Writing
permalink: /writing/
layout: page
---
Please feel free to visit the [archive](/archive) to see all posts organized by category!

<ul>
  {% for post in site.categories.Other %}

     <li> <a href="{{ post.url }}"><div style="font-family: Roboto;font-size:16pt">{{ post.title }}</div></a>
      {{ post.excerpt }}
      <div style="text-align:right;position:relative;top:-1em;"><i>
({{ post.date | date: '%d %B, %Y' }})</i></div>
</li>
  {% endfor %}
</ul>
