from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^exceptions$',
        view=views.BatchExceptionDatatableView.as_view(),
        name='exceptions'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),

]
