from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("blog", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('add/',views.PostAddView.as_view(),name='blog_add'),
    path('delete/<int:pk>',views.PostDeleteView.as_view(),name='blog_delete'),
    path('edit/<int:pk>',views.PostEditView.as_view(),name='blog_edit'),
    
    path("post/reaction/<int:post_id>/<action>", views.set_reaction, name="set_reaction")
]