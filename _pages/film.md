---
title: Film
permalink: /film/
layout: page
---
In addition to research, I am also an independent/freelance film-maker.  All of my publically-available projects are included below.

## Nonfiction
<ul>
  {% for post in site.categories.nonfiction %}
    <li>
      <a href="{{ post.url }}"> <i>{{ post.title }}</i></a>
      {{ post.excerpt }}

      <p style="text-align:left;position:relative;top:-1em;"><a href="{{ post.url }}"> <i>(read more)</i></a></p>
    </li>
  {% endfor %}
</ul>
