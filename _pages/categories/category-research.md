---
title: "Category: Research"
permalink: /categories/test
layout: page
---

<div>
  {% for post in site.categories.nonfiction %}
    <ul>
      <li><a href="{{ post.url }}"> <i>{{ post.title }}</i></a></li> ({{ post.date }})
     </ul>



  {% endfor %}
</div>
