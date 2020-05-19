from django.urls import path
from.import views

urlpatterns = [
    path("",views.home,name='home'),
    path("piano",views.piano,name='piano'),
    path("drum",views.drum,name='drum'),
    path("fm",views.fm,name='fm'),
    path("guitar",views.guitar,name='guitar'),
    path("pad",views.pad,name='pad'),
    path("music",views.music,name='music')
]