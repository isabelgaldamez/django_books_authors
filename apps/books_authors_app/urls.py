from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<book_id>\d+)$', views.book_info),
    url(r'^assign_author/$', views.assign_author)
]