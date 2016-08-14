from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'events.views.home', name='home'),
    url(r'^events/$', 'events.views.list', name='event_list'),
    url(r'^events/(?P<id>\d+)/$', 'events.views.detail', name='event_detail'),
    url(r'^register/$', 'events.views.register', name='register'),
    url(r'^login/$', auth_view.login, name='login', kwargs={'template_name': 'users/login.html'}),
    url(r'^logout/$', auth_view.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^events/join/(?P<event_id>\d+)/$', 'events.views.join', name='event_join'),
    url(r'^events/cancel/(?P<event_id>\d+)/$', 'events.views.cancel', name='event_cancel'),
    url(r'^user_event/(?P<user_id>\d+)/$', 'events.views.user_event', name='user_event')
]
