---
layout: page
title: Film
permalink: /film/
---
In addition to research, I am also an independent/freelance film-maker.  All of my publically-available projects are included below.

## Nonfiction
<ul>
  {% for post in site.categories.film %}
    <li>
      <a href="{{ post.url }}"> <i>{{ post.title }}</i></a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
