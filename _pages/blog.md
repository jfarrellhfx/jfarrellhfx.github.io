---
title: Blog
permalink: /blog/
layout: page
---





# Latest:
<div>
  {% for post in site.posts offset:1 limit:2 %}

      <a href="{{ post.url }}"> <i><h3>{{ post.title }}</h3></i></a>
      {{ post.excerpt }}

      <p style="text-align:center;position:relative;top:-1em;"><a href="{{ post.url }}"> <i>(read more)</i></a></p>

  {% endfor %}
</div>

# All:
<div>
{% for category in site.categories %}
    <h3>{{ category[0] }}</h3>
    <ul>
        {% for post in category[1] %}
         <li>
        <a href = "{{ post.url }}">{{ post.title }}</a>
        </li>

        {% endfor %}

</ul>


 {% endfor %}

</div>


---
