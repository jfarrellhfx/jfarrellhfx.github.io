---
title: Research
permalink: /Research/
layout: page
---

I am interested in the theoretical physics of materials, called *Condensed Matter Physics*.  You can read about my recent research projects, in this area and others, below.
<ul>
  {% for post in site.categories.research %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>

interested
