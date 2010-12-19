from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
            url(r'^login/$',
                'login', {'template_name': 'admin/login.html'},
                name='login'),
            url(r'^logout/$',
                'logout',
                name='logout'),
            url(r'^password_change/$',
                'password_change',
                name='password_change'),
            url(r'^password_change/done/$',
                'password_change_done',
                name='password_change_done'),
        )
