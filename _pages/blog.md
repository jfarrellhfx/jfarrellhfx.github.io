---
title: Blog
permalink: /blog/
layout: page
---
Topics include physics, filmmaking, programming, science communication, and more. For a full list of posts by category, feel free to visit the <a href = "/archive">blog archive</a>.

---

{% if site.paginate %}
  {% assign posts = paginator.posts %}
{% else %}
  {% assign posts = site.posts %}
{% endif %}


{%- if posts.size > 0 -%}
  <ul class="post-list">
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    {%- for post in posts -%}
    <li>
      <span class="post-meta">{{ post.date | date: date_format }}</span>
      <h3 style="margin-top:0">
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h3>
      {%- if site.show_excerpts -%}
        {{ post.excerpt }}
        <p style="text-align:center;position:relative;top:-0.75em;"><a href="{{ post.url }}"> <i>(read more)</i></a></p>
      {%- endif -%}
    </li>
    {%- endfor -%}
  </ul>

  {% if site.paginate %}
    <div class="pager">
      <ul class="pagination">
      {%- if paginator.previous_page %}
        <li><a href="{{ paginator.previous_page_path | relative_url }}" class="previous-page">{{ paginator.previous_page }}</a></li>
      {%- else %}
        <li><div class="pager-edge">•</div></li>
      {%- endif %}
        <li><div class="current-page">{{ paginator.page }}</div></li>
      {%- if paginator.next_page %}
        <li><a href="{{ paginator.next_page_path | relative_url }}" class="next-page">{{ paginator.next_page }}</a></li>
      {%- else %}
        <li><div class="pager-edge">•</div></li>
      {%- endif %}
      </ul>
    </div>
  {%- endif %}

{%- endif -%}
