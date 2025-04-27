---
layout: default
title: Portafolio
---

{% for item in site.data.portfolio %}
<div class="project">
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
  <ul>
    {% for tech in item.technologies %}
    <li>{{ tech }}</li>
    {% endfor %}
  </ul>
  <small>{{ item.date | date_to_string }}</small>
</div>
{% endfor %}
