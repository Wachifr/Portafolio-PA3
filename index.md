layout: default
title: Bienvenido
# Portafolio de Washington Olarte Velasquez

{% for post in site.data.posts %}
### {{ post.title }} - por {{ post.author }}
> {{ post.content }}
Etiquetas: {{ post.tags | join: ", " }}
{% endfor %}
