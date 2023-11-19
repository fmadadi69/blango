import blog.views
from django.urls import path
app_name='blog'
urlpatterns =[
  path("", blog.views.index, name = "index_view"),
  path("post/<slug>", blog.views.post_detail, name="post_detail_view")
]