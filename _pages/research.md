---
title: Research
permalink: /Research/
layout: page
---

I am interested in the theoretical physics of materials, called *Condensed Matter Physics*.  You can read about my recent research projects, in this area and others, below.

---

<div>
  {% for doc in site.research_projects | sort: "order" %}

      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
      <p style="text-align:center;position:relative;top:-0em;"><a href="{{ doc.url }}"> <i>(read more)</i></a></p>
  {% endfor %}
</div>
