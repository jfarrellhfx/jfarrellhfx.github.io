---
title: Film
permalink: /film/
layout: page
---
In addition to research, I am also an independent/freelance film-maker.  All of my publically-available projects are included below.

---

## Nonfiction
<div>
  {% for post in site.categories.nonfiction %}

      <a href="{{ post.url }}"> <i><h3>{{ post.title }}</h3></i></a>
      {{ post.excerpt }}

      <p style="text-align:center;position:relative;top:-1em;"><a href="{{ post.url }}"> <i>(read more)</i></a></p>

  {% endfor %}
</div>

---
