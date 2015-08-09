from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^$','school.views.index',name='index'),

	url(r'^school$','school.views.school',name='school'),
	url(r'^add_school$','school.views.add_school',name='add_school'),
	
	url(r'^process$','school.views.process',name='process'),
	url(r'^add_process$','school.views.add_process',name='add_process'),
	
	url(r'^student$','school.views.student',name='student'),
	url(r'^add_student$','school.views.add_student',name='add_student'),
    
    url(r'^admin/', include(admin.site.urls)),
)
