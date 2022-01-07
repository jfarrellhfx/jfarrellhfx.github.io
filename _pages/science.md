---
title: Research
permalink: /research/
layout: page
---
<div>
  {% assign projects = (site.research_projects | sort: "order") %}
  {% for doc in projects %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
  {% endfor %}
</div>
