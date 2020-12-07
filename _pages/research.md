---
title: Research
permalink: /Research/
layout: page
---

I am interested in the theoretical physics of materials, called *Condensed Matter Physics*.  You can read about my recent research projects, in this area and others, below.

---

<div>
  {% for post in site.categories.research %}

      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
      <p style="text-align:left;position:relative;top:-1em;"><a href="{{ post.url }}"> <i>(read more)</i></a></p>
  {% endfor %}
</div>

interested
