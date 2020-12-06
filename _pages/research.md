---
title: Research
permalink: /Research/
layout: page
---
<div style = "text-align: justify; text-justify: inter-word;">
I am interested in the theoretical physics of materials, *Condensed Matter Physics*.  You can read about my recent research projects, in this area and others, below.
<ul>
  {% for post in site.categories.research %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
</div>
