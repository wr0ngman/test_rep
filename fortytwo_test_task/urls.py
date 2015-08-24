from django.conf.urls import patterns, include, url

from django.contrib import admin

#List_view_use#import hello.views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'hello.views.devinfo_view', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
