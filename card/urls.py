from django.urls import path
from .views import index, blog, blog_detail, contact

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
]