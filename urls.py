from django.conf.urls import url
from api import views

app_name = 'api'


urlpatterns = [
    url(r'^ticket_stats/tickets_all.csv', views.ticket_stats_total_api, name='ticket_stats_total_api'),
    url(r'^ticket_stats/tickets_office.csv', views.ticket_stats_office_api, name='ticket_stats_office_api'),
    url(r'^projects_list/', views.projects_list, name='projects_list'),
    url(r"^projects_details/(?P<pk>\d+)/$", views.projects_detailed_api, name="projects_detailed_api"),
]
